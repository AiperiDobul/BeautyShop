# Generated by Django 3.1 on 2021-12-23 10:51

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='KG', unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('activation_code', models.CharField(blank=True, max_length=8)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]