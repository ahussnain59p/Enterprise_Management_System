# Generated by Django 5.0.7 on 2024-07-17 15:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=90, unique=True)),
                ('password', models.CharField(max_length=95, validators=[django.core.validators.RegexValidator(message='Password must contain at least one lowercase letter.', regex='^.*[a-z].*$'), django.core.validators.RegexValidator(message='Password must contain at least one uppercase letter.', regex='^.*[A-Z].*$'), django.core.validators.RegexValidator(message='Password must contain at least one special character.', regex='^.*[\\W_].*$')])),
            ],
        ),
    ]
