# Generated by Django 2.2 on 2022-03-03 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_auto_20220228_0744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='count',
        ),
    ]
