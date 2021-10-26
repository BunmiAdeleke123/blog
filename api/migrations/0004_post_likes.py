# Generated by Django 3.2.8 on 2021-10-26 11:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None),
        ),
    ]