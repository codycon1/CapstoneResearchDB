# Generated by Django 3.2.12 on 2022-04-29 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectfile',
            name='type',
        ),
        migrations.RemoveField(
            model_name='resultfile',
            name='type',
        ),
    ]
