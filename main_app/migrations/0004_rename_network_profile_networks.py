# Generated by Django 4.0.4 on 2022-05-01 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_network_request_from_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='network',
            new_name='networks',
        ),
    ]
