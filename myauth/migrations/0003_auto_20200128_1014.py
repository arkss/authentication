# Generated by Django 3.0.2 on 2020-01-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0002_auto_20200121_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
