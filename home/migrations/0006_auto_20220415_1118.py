# Generated by Django 3.2.12 on 2022-04-15 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20220415_1111'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Proposal',
        ),
        migrations.AlterField(
            model_name='project',
            name='projectDescription',
            field=models.CharField(max_length=256, verbose_name='Project Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectTitle',
            field=models.CharField(max_length=100, verbose_name='Project Title'),
        ),
        migrations.AlterField(
            model_name='project',
            name='proposalFile',
            field=models.FileField(null=True, upload_to='projects/proposals', verbose_name='Proposal'),
        ),
    ]
