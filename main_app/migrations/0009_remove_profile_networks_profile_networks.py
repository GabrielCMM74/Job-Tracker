# Generated by Django 4.0.4 on 2022-05-01 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_remove_profile_networks_profile_networks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='networks',
        ),
        migrations.AddField(
            model_name='profile',
            name='networks',
            field=models.ManyToManyField(blank=True, to='main_app.profile'),
        ),
    ]
