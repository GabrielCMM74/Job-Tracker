# Generated by Django 4.0.4 on 2022-05-01 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_application_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='link',
            field=models.URLField(),
        ),
    ]