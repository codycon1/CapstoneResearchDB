# Generated by Django 3.2.12 on 2022-04-29 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectfile',
            old_name='dataFile',
            new_name='file',
        ),
        migrations.DeleteModel(
            name='ResultFile',
        ),
    ]