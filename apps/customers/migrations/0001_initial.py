# Generated by Django 2.2.3 on 2019-07-21 18:36

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('last_name', models.TextField()),
                ('tax_id', models.TextField(blank=True, default='C/F')),
                ('address', models.TextField(blank=True, default='Ciudad')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
