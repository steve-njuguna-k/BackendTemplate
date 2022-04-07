import base64
import hashlib
from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django_prometheus.models import ExportModelOperationsMixin
from django_rest_passwordreset.signals import reset_password_token_created
from phonenumber_field.modelfields import PhoneNumberField

from App.storage import image_file_upload
from Users.choices import GenderChoices


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(
        self, email, password, first_name, last_name, **extra_fields
    ):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, first_name, last_name, password, **extra_fields
    ):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.is_admin = True
        user.is_verified = True
        user.is_premium = True
        user.save(using=self._db)
        return user


class User(
    ExportModelOperationsMixin('dataset'), AbstractBaseUser, PermissionsMixin
):
    username = None
    is_superuser = None
    last_login = None

    email = models.EmailField(
        'Email address',
        unique=True,
        error_messages={'unique': 'This email already exists.'},
    )
    first_name = models.CharField('First name', blank=False, max_length=50)
    last_name = models.CharField('Last name', blank=False, max_length=50)
    phone_number = PhoneNumberField('User number', blank=True, max_length=22)
    is_verified = models.BooleanField('Verification status', default=False)
    is_premium = models.BooleanField('Premium status', default=False)
    is_admin = models.BooleanField('Admin status', default=False)
    created_at = models.DateTimeField('Creation date', auto_now_add=True)
    updated_at = models.DateTimeField('Update date', auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_permission(self, object=None):
        if isinstance(object, User):
            return object.id == self.id
        else:
            return object.user.id == self.id

    def has_module_perms(self, app_label):
        return True

    def generate_verification_token(self):
        string_user = self.email + settings.EMAIL_VERIFICATION_TOKEN_SECRET
        hashed = hashlib.md5(string_user.encode())
        decoded = base64.b64encode(hashed.digest()).decode('utf-8')
        token = (
            decoded.replace('\+', '-')
            .replace('/', '_')
            .replace('=', "")
            .replace('+', "")
        )
        return token

    def verify(self):
        self.is_verified = True
        self.save()

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True,
    )
    nickname = models.CharField(
        'Nick',
        unique=True,
        error_messages={'unique': 'This nickname already exists.'},
        blank=True,
        null=True,
        max_length=50,
    )
    bio = models.TextField('Bio', blank=True)
    profile_image = models.ImageField(
        'Profile image', upload_to=image_file_upload, blank=True, null=True,
    )
    gender = models.CharField(
        'Gender',
        max_length=1,
        choices=GenderChoices.choices,
        default=GenderChoices.NOT_SAID,
        blank=True,
        null=True,
    )
    birth_date = models.DateField(
        'Birth date', blank=True, null=True, auto_now_add=False
    )
    created_at = models.DateTimeField('Creation date', auto_now_add=True)
    updated_at = models.DateTimeField('Update date', auto_now=True)

    def __str__(self):
        return f'User ({self.user_id}) profile ({self.pk})'

    def is_adult(self):
        adultness = (datetime.now() - relativedelta(years=18))
        return datetime.strptime(self.birth_date, '%Y-%m-%d') < adultness

@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):
    from Emails.utils import send_email

    send_email('reset_password', reset_password_token)
