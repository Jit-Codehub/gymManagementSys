# Generated by Django 3.2.5 on 2023-02-01 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_service_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='img',
            field=models.ImageField(upload_to='services/'),
        ),
    ]