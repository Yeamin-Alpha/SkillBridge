# Generated by Django 5.1.2 on 2024-10-31 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_profile_name_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]