# Generated by Django 4.2.9 on 2024-01-28 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlackListedToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='token_user', to='userauth.usermodel')),
            ],
            options={
                'unique_together': {('token', 'user')},
            },
        ),
    ]
