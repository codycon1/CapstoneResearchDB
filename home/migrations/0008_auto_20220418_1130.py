# Generated by Django 3.2.12 on 2022-04-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_project_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectAuthor',
            field=models.CharField(max_length=128),
        ),
    ]
