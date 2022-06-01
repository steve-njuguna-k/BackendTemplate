# Generated by Django 4.0 on 2022-05-25 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractEmailClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100, null=True)),
                ('sent_date', models.DateTimeField(null=True)),
                ('was_sent', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlackList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(null=True)),
                ('show_link', models.BooleanField(default=False)),
                ('link_text', models.CharField(max_length=100, null=True)),
                ('link', models.URLField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('abstractemailclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Emails.abstractemailclass')),
                ('subject', models.CharField(max_length=100)),
                ('is_test', models.BooleanField(default=False)),
                ('programed_send_date', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('Emails.abstractemailclass',),
        ),
        migrations.AddField(
            model_name='abstractemailclass',
            name='blocks',
            field=models.ManyToManyField(related_name='%(class)s_blocks', to='Emails.Block'),
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('abstractemailclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Emails.abstractemailclass')),
                ('subject', models.CharField(choices=[('SUGGESTION', 'Suggestion'), ('BUG', 'Bug'), ('ERROR', 'Error'), ('OTHER', 'Other')], default='SUGGESTION', max_length=100)),
                ('was_read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggestion', to='Users.user')),
            ],
            options={
                'abstract': False,
            },
            bases=('Emails.abstractemailclass',),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('abstractemailclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Emails.abstractemailclass')),
                ('subject', models.CharField(max_length=100)),
                ('is_test', models.BooleanField(default=False)),
                ('programed_send_date', models.DateTimeField(null=True)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='Users.user')),
            ],
            options={
                'abstract': False,
            },
            bases=('Emails.abstractemailclass',),
        ),
    ]
