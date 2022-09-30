from django.contrib.auth import authenticate
from django.contrib.auth import password_validation
from django.db.models import Field
from django.db.models import Model
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.tokens import RefreshToken

from Emails.utils import send_email
from Users.models import User
from Users.serializers import ProfileSerializer


class UserAuthSerializer(serializers.Serializer):
    """
    User authentication serializer
    """

    id: Field = serializers.IntegerField(read_only=True)
    first_name: Field = serializers.CharField(required=False, max_length=255)
    last_name: Field = serializers.CharField(required=False, max_length=255)
    email: Field = serializers.EmailField(required=True)
    phone_number: PhoneNumberField = PhoneNumberField(
        required=False, max_length=22
    )
    is_verified: Field = serializers.BooleanField(read_only=True)
    is_premium: Field = serializers.BooleanField(read_only=True)
    is_admin: Field = serializers.BooleanField(read_only=True)
    created_at: Field = serializers.DateTimeField(read_only=True)
    updated_at: Field = serializers.DateTimeField(read_only=True)
    profile: ProfileSerializer = ProfileSerializer(read_only=True)
    token: Field = serializers.SerializerMethodField(read_only=True)
    refresh_token: Field = serializers.SerializerMethodField(read_only=True)

    def get_token(self, object: User) -> str:
        return str(AccessToken.for_user(object))

    def get_refresh_token(self, object: User) -> str:
        return str(RefreshToken.for_user(object).access_token)

    class Meta:
        model: Model = User


class UserLoginSerializer(serializers.Serializer):
    """
    User login serializer
    """

    email: Field = serializers.EmailField(required=True)
    password: Field = serializers.CharField(write_only=True, required=True)

    def is_valid(self, raise_exception: bool = True) -> bool:
        super().is_valid(raise_exception=raise_exception)
        self.validate_login(self.initial_data)
        self._data = UserAuthSerializer(self.user).data
        return True

    def validate_login(self, data: dict) -> None:
        user: User = authenticate(
            email=data["email"], password=data["password"]
        )
        if not user:
            raise ValidationError("Invalid credentials")
        if not user.is_verified:
            raise ValidationError("User is not verified")
        self.user: User = user

    class Meta:
        model: Model = User


class UserSignUpSerializer(serializers.Serializer):
    """
    User sign up serializer
    """

    first_name = serializers.CharField(required=True, max_length=255)
    last_name = serializers.CharField(required=True, max_length=255)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only=True, min_length=8, max_length=64, required=True
    )
    password_confirmation = serializers.CharField(
        write_only=True, min_length=8, max_length=64, required=True
    )

    def validate_password(self, password: str) -> str:
        password_confirmation = self.initial_data["password_confirmation"]
        if password != password_confirmation:
            raise ValidationError("Password confirmation does not match")
        password_validation.validate_password(password)
        return password

    def create(self, data):
        data.pop("password_confirmation")
        user = User.objects.create_user(**data, is_verified=False)
        send_email("verify_email", user)
        return user
