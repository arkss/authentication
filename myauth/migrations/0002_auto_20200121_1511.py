# Generated by Django 3.0.2 on 2020-01-21 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='nickname',
            new_name='username',
        ),
    ]