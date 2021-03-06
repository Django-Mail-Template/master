# Generated by Django 2.2.9 on 2020-07-12 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title', models.CharField(
                    help_text='A title to identify the mail template.',
                    max_length=100, verbose_name='Title')),
                ('to', models.CharField(
                    blank=True,
                    help_text='A list with destiny email addresses '
                              'separated with coma.',
                    max_length=1000, null=True)),
                ('from_email', models.EmailField(
                    help_text="Sender's email address.", max_length=254)),
                ('subject', models.CharField(
                    help_text='Subject text for the mail. Context '
                              'variable can be used.', max_length=140)),
                ('body', models.TextField(
                    blank=True,
                    help_text='The content of the mail. Context '
                              'variable can be used.', max_length=5000,
                    null=True)),
                ('description', models.TextField(
                    blank=True,
                    help_text='Description of the mail template.',
                    null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Mail Template',
                'verbose_name_plural': 'Mails Templates',
            },
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID')),
                ('process', models.CharField(max_length=200)),
                ('description', models.TextField(
                    blank=True,
                    help_text='Description for configuration. This '
                              'description can contain the contextual '
                              'variables that are expected to be used in '
                              'associated MailTemplates.', null=True,
                    verbose_name='Description')),
                ('mail_template', models.ForeignKey(
                    blank=True, null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    to='django_mail_template.MailTemplate')),
            ],
            options={
                'verbose_name': 'Configuration',
                'verbose_name_plural': 'Configurations',
            },
        ),
    ]
