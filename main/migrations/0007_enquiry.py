# Generated by Django 3.2.7 on 2023-02-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('detail', models.TextField()),
                ('send_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
