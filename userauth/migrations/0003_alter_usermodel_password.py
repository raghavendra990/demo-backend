# Generated by Django 4.2.9 on 2024-01-28 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_blacklistedtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
