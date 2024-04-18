# Generated by Django 4.2.6 on 2023-10-27 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_book_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0006_favourite'),
    ]

    operations = [
        migrations.CreateModel(
            name='read',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]