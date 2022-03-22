from django.conf import settings
from django_rest_passwordreset.models import ResetPasswordToken

from Emails.factories.email import EmailFactory
from Emails.factories.email import get_subject_for_suggestion
from Emails.factories.email import ResetEmailFactory
from Emails.factories.email import SuggestionEmailFactory
from Emails.factories.email import VerifyEmailFactory
from Emails.models import Block
from Emails.models import Email
from Emails.tests.abstract_test_classes import EmailsAbstractUtils
from Users.factories.user import UserFactory


class TestEmailFactories(EmailsAbstractUtils):
    def test_email_factory_creates_email_with_block(self):
        assert Email.objects.count() == 0
        assert Block.objects.count() == 0
        email = EmailFactory(
            subject='Test subject',
            header='Test header',
        )
        assert Email.objects.count() == 1
        assert Block.objects.count() == 1
        assert email.subject == 'Test subject'
        assert email.header == 'Test header'
        assert email.is_test is False
        assert email.to_all_users is False
        assert email.to is not None
        assert email.programed_send_date is not None
        assert email.blocks is not None
        block = email.blocks.first()
        assert block.title is not None
        assert block.content is not None
        assert block.show_link is not None
        assert block.link_text is not None
        assert block.link is not None

    def test_reset_password_email_factory_raises_exception(self):
        assert Email.objects.count() == 0
        assert Block.objects.count() == 0
        with self.assertRaises(AttributeError):
            ResetEmailFactory()
        assert Email.objects.count() == 0
        assert Block.objects.count() == 0

    def test_reset_password_email_factory_creates_email_with_block(self):
        user = UserFactory()
        instance = ResetPasswordToken.objects.create(user=user)
        assert Email.objects.count() == 0
        assert Block.objects.count() == 0
        email = ResetEmailFactory(instance=instance)
        assert Email.objects.count() == 1
        assert Block.objects.count() == 1
        assert email.subject == settings.RESET_PASSWORD_EMAIL_SUBJECT
        assert email.header == settings.RESET_PASSWORD_EMAIL_HEADER
        assert email.is_test is False
        assert email.to_all_users is False
        assert email.to == user.email
        assert email.programed_send_date is not None
        assert email.blocks is not None
        block = email.blocks.first()
        assert settings.EMAIL_GREETING in block.title
        assert user.first_name in block.title
        assert block.content == settings.RESET_PASSWORD_EMAIL_CONTENT
        assert block.show_link
        assert block.link_text == settings.RESET_PASSWORD_EMAIL_LINK_TEXT
        assert settings.RESET_PASSWORD_URL in block.link

    def test_verify_email_factory_raises_exception(self):
        assert Email.objects.count() == 0
        assert Block.objects.count() == 0
        with self.assertRaises(AttributeError):
            VerifyEmailFactory()
        assert Email.objects.count() == 0
        assert Block.objects.count() == 0

    def test_verify_email_factory_creates_email_with_block(self):
        user = UserFactory()
        assert Email.objects.count() == 0
        assert Block.objects.count() == 0
        email = VerifyEmailFactory(instance=user)
        assert Email.objects.count() == 1
        assert Block.objects.count() == 1
        assert email.subject == settings.VERIFY_EMAIL_SUBJECT
        assert email.header == settings.VERIFY_EMAIL_HEADER
        assert email.is_test is False
        assert email.to_all_users is False
        assert email.to == user.email
        assert email.programed_send_date is not None
        assert email.blocks is not None
        block = email.blocks.first()
        assert settings.EMAIL_GREETING in block.title
        assert user.first_name in block.title
        assert block.content == settings.VERIFY_EMAIL_CONTENT
        assert block.show_link
        assert block.link_text == settings.VERIFY_EMAIL_LINK_TEXT
        assert settings.VERIFY_EMAIL_URL in block.link
        assert user.generate_verification_token() in block.link
        assert f'{user.id}' in block.link

    def test_get_subject_for_suggestion_raises_an_exception(self):
        content = 'I found a bug'
        type = 'wrong_suggestion_type'
        with self.assertRaises(ValueError):
            get_subject_for_suggestion(type, content)

    def test_get_subject_for_suggestion_returns_subject(self):
        content = 'I found a bug'
        type = 'Error'
        subject = get_subject_for_suggestion(type, content)
        assert subject == f'{type} || {content}'

    def test_get_subject_for_suggestion_returns_subject_without_vertical(self):
        content = 'I found a bug ||'
        type = 'Error'
        subject = get_subject_for_suggestion(type, content)
        assert subject == f'{type} || I found a bug '

    def test_suggestion_email_factory_raises_exception_without_params(self):
        assert Email.objects.count() == 0
        assert Block.objects.count() == 0
        with self.assertRaises(ValueError):
            SuggestionEmailFactory()
        assert Email.objects.count() == 0
        assert Block.objects.count() == 0

    def test_suggestion_email_factory_raises_exception_due_wrong_type(self):
        user = UserFactory()
        content = 'I found a bug'
        type = 'wrong_suggestion_type'
        assert Email.objects.count() == 0
        assert Block.objects.count() == 0
        with self.assertRaises(ValueError):
            SuggestionEmailFactory(type=type, content=content, instance=user)
        assert Email.objects.count() == 0
        assert Block.objects.count() == 0

    def test_suggestion_email_factor_creates_email_with_block(self):
        user = UserFactory()
        content = 'I found a bug'
        type = 'Error'
        assert Email.objects.count() == 0
        assert Block.objects.count() == 0
        email = SuggestionEmailFactory(type=type, content=content, instance=user)
        assert Email.objects.count() == 1
        assert Block.objects.count() == 1
        assert email.subject == 'Error'
        assert email.header == (
            f'Error {settings.SUGGESTIONS_EMAIL_HEADER} {user.id}'
        )
        assert email.is_test is False
        assert email.to_all_users is False
        assert email.to == settings.SUGGESTIONS_EMAIL
        assert email.programed_send_date is not None
        assert email.blocks is not None
        block = email.blocks.first()
        assert email.header == block.title
        assert block.content == content
        assert block.show_link is False
