# Generated by Django 4.2.6 on 2023-10-20 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_book_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='created_by',
        ),
    ]