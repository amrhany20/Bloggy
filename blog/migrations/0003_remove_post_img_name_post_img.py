# Generated by Django 4.1.6 on 2023-02-22 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_tag_remove_post_img_post_img_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img_name',
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
