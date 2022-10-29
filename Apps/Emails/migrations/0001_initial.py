# Generated by Django 4.1.1 on 2022-09-20 23:36

import Emails.abstracts
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Block",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, null=True)),
                ("content", models.TextField(null=True)),
                ("show_link", models.BooleanField(default=False)),
                ("link_text", models.CharField(
                        max_length=100,
                        null=True,
                        blank=True
                    )
                ),
                ("link", models.URLField(
                        max_length=100,
                        null=True,
                        blank=True
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name="Suggestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("header", models.CharField(max_length=100, null=True)),
                (
                    "affair",
                    models.CharField(
                        choices=[
                            ("NOTIFICATION", "Notification"),
                            ("PROMOTION", "Promotion"),
                            ("GENERAL", "General"),
                            ("SETTINGS", "Settings"),
                            ("INVOICE", "Invoice"),
                            ("SUGGESTION", "Suggestion"),
                        ],
                        default="NOTIFICATION",
                        max_length=100,
                    ),
                ),
                ("sent_date", models.DateTimeField(null=True)),
                ("was_sent", models.BooleanField(default=False, editable=False)),
                (
                    "subject",
                    models.CharField(
                        choices=[
                            ("SUGGESTION", "Suggestion"),
                            ("BUG", "Bug"),
                            ("ERROR", "Error"),
                            ("OTHER", "Other"),
                        ],
                        default="SUGGESTION",
                        max_length=100,
                    ),
                ),
                ("was_read", models.BooleanField(default=False)),
                (
                    "blocks",
                    models.ManyToManyField(
                        related_name="%(class)s_blocks", to="Emails.block"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="suggestion",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=(models.Model, Emails.abstracts.AbstractEmailFunctionClass),
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("header", models.CharField(max_length=100, null=True)),
                (
                    "affair",
                    models.CharField(
                        choices=[
                            ("NOTIFICATION", "Notification"),
                            ("PROMOTION", "Promotion"),
                            ("GENERAL", "General"),
                            ("SETTINGS", "Settings"),
                            ("INVOICE", "Invoice"),
                            ("SUGGESTION", "Suggestion"),
                        ],
                        default="NOTIFICATION",
                        max_length=100,
                    ),
                ),
                ("sent_date", models.DateTimeField(null=True)),
                ("was_sent", models.BooleanField(default=False, editable=False)),
                ("subject", models.CharField(max_length=100)),
                ("is_test", models.BooleanField(default=False)),
                ("programed_send_date", models.DateTimeField(null=True)),
                (
                    "blocks",
                    models.ManyToManyField(
                        related_name="%(class)s_blocks", to="Emails.block"
                    ),
                ),
            ],
            bases=(models.Model, Emails.abstracts.AbstractEmailFunctionClass),
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("header", models.CharField(max_length=100, null=True)),
                (
                    "affair",
                    models.CharField(
                        choices=[
                            ("NOTIFICATION", "Notification"),
                            ("PROMOTION", "Promotion"),
                            ("GENERAL", "General"),
                            ("SETTINGS", "Settings"),
                            ("INVOICE", "Invoice"),
                            ("SUGGESTION", "Suggestion"),
                        ],
                        default="NOTIFICATION",
                        max_length=100,
                    ),
                ),
                ("sent_date", models.DateTimeField(null=True)),
                ("was_sent", models.BooleanField(default=False, editable=False)),
                ("subject", models.CharField(max_length=100)),
                ("is_test", models.BooleanField(default=False)),
                ("programed_send_date", models.DateTimeField(null=True)),
                (
                    "blocks",
                    models.ManyToManyField(
                        related_name="%(class)s_blocks", to="Emails.block"
                    ),
                ),
                (
                    "to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="to_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("EN", "English"),
                            ("ES", "Spanish"),
                            ("FR", "French"),
                            ("OT", "Other"),
                        ],
                        default="EN",
                        max_length=2,
                        null=True,
                        verbose_name="Preferred language",
                    ),
                ),
            ],
            bases=(models.Model, Emails.abstracts.AbstractEmailFunctionClass),
        ),
        migrations.CreateModel(
            name="BlackList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "affairs",
                    django_mysql.models.ListCharField(
                        models.CharField(
                            choices=[
                                ("NOTIFICATION", "Notification"),
                                ("PROMOTION", "Promotion"),
                                ("GENERAL", "General"),
                                ("SETTINGS", "Settings"),
                                ("INVOICE", "Invoice"),
                                ("SUGGESTION", "Suggestion"),
                            ],
                            default="GENERAL",
                            max_length=15,
                        ),
                        max_length=79,
                        size=5,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blacklist",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
