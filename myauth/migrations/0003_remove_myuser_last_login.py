# Generated by Django 3.0.2 on 2020-01-21 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0002_auto_20200121_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='last_login',
        ),
    ]