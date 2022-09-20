from django.conf import settings
from facebook import GraphAPI
from google.auth.transport.requests import Request
from google.oauth2.id_token import verify_oauth2_token
from twitter import Api
from twitter import User as TwitterUser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.serializers import CharField
from rest_framework.serializers import Serializer
from rest_framework.serializers import ValidationError

from SocialAuth.user_handler import RegisterOrLoginViaFacebook
from SocialAuth.user_handler import RegisterOrLoginViaGoogle


class GoogleOAuthSerializer(Serializer):
    token: CharField = CharField()

    def validate_token(self, token: str) -> dict:
        user_data: dict = self.get_user_data(token)
        self.validate_aud(user_data["aud"])
        return RegisterOrLoginViaGoogle(user_data).serialized_user

    def get_user_data(self, token: str) -> dict:
        try:
            return verify_oauth2_token(token, Request())
        except:
            raise ValidationError("Token is invalid or expired. Try again.")

    def validate_aud(self, aud: str) -> None:
        if aud != settings.GOOGLE_CLIENT_ID:
            raise AuthenticationFailed("Google client id is invalid")


class FacebookOAuthSerializer(Serializer):
    token: CharField = CharField()

    def validate_token(self, token: str) -> dict:
        user_data = self.get_user_data(token)
        return RegisterOrLoginViaFacebook(user_data).serialized_user

    def get_user_data(self, token: str) -> dict:
        try:
            graph: GraphAPI = GraphAPI(access_token=token)
            graph_query: str = "/me?fields=first_name,last_name,email"
            user_data: dict = graph.request(graph_query)
            return user_data
        except:
            raise ValidationError("Token is invalid or expired. Try again.")


class TwitterOAuthSerializer(Serializer):
    access_token_key: CharField = CharField()
    access_token_secret: CharField = CharField()

    def validate(self, attributes: dict) -> dict:
        twitter_user: TwitterUser = self.get_user_data(attributes)
        user_data: dict = self.get_dictionary_of_user_data(twitter_user)
        return RegisterOrLoginViaFacebook(user_data).serialized_user

    def get_user_data(self, attributes: dict) -> TwitterUser:
        try:
            api = Api(
                consumer_key=settings.TWITTER_API_KEY,
                consumer_secret=settings.TWITTER_API_SECRET_KEY,
                access_token_key=attributes.get('access_token_key', None),
                access_token_secret=attributes.get('access_token_secret', None)
            )
            return api.VerifyCredentials(include_email=True)
        except Exception :
            raise ValidationError("Token is invalid or expired. Try again.")

    def get_dictionary_of_user_data(user: TwitterUser) -> dict:
        if not getattr(user, 'email', None):
            raise ValidationError("Email is not available and is required.")
        return {
            "email": getattr(user, 'email'),
            "name": getattr(user, 'name', None)
        }
