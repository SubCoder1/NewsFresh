# Generated by Django 3.0.2 on 2020-02-08 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0007_auto_20200208_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdatamodel',
            name='voted_news',
        ),
    ]
