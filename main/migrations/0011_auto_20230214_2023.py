# Generated by Django 3.2.5 on 2023-02-14 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_subplan_highlight_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subplanfeature',
            name='subplan',
        ),
        migrations.AddField(
            model_name='subplanfeature',
            name='subplan',
            field=models.ManyToManyField(to='main.SubPlan'),
        ),
    ]