# Generated by Django 5.1.2 on 2024-10-29 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]