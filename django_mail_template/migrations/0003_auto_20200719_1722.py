# Generated by Django 2.2.9 on 2020-07-19 17:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_mail_template', '0002_auto_20200713_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailtemplate',
            name='body',
            field=ckeditor.fields.RichTextField(
                blank=True,
                help_text='The content of the mail. '
                          'Context variable can be used.',
                max_length=5000, null=True, verbose_name='Body'),
        ),
    ]
