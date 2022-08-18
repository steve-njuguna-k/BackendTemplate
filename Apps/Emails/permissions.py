from django.http import HttpRequest
from django.views import View
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission

from Emails.models.models import BlackList
from Users.models import User


class IsBlacklistOwner(BasePermission):
    message: str = "You don't have permission to modify this blacklist item"

    def has_permission(self, request: HttpRequest, view: View) -> bool:
        user: User = request.user
        kwargs: dict = request.parser_context["kwargs"]
        blacklist_id: int = kwargs.get("pk", None)
        blacklist: BlackList = get_object_or_404(BlackList, id=blacklist_id)
        return user.has_permission(blacklist)


class HasListBlacklistPermission(BasePermission):
    message: str = "You don't have permission to list blacklist"

    def is_a_list_request(self, request) -> bool:
        is_get_method: bool = request.method == "GET"
        has_empty_kwargs: bool = request.parser_context["kwargs"] == {}
        return is_get_method and has_empty_kwargs

    def has_permission(self, request: HttpRequest, view: View) -> bool:
        if self.is_a_list_request(request):
            user: User = request.user
            return user.is_admin
        return True
