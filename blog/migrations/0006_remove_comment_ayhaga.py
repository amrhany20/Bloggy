# Generated by Django 4.1.6 on 2023-02-22 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_ayhaga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='ayhaga',
        ),
    ]
