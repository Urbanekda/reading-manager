# Generated by Django 4.2.7 on 2024-12-13 14:23

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('reading_manager', '0003_book_status_alter_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='notes',
            field=tinymce.models.HTMLField(),
        ),
    ]
