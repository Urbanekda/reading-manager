# Generated by Django 4.2.7 on 2024-12-17 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading_manager', '0006_alter_book_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
