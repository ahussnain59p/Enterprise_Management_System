# Generated by Django 5.0.7 on 2024-07-17 11:22
from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.CharField(max_length=50)),
                ('service_title', models.CharField(max_length=90)),
                ('service_des', models.TextField()),
            ],
        ),
    ]
