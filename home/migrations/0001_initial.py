# Generated by Django 3.2.12 on 2022-04-22 17:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=256)),
                ('date', models.DateField(auto_now=True)),
                ('projectAuthor', models.CharField(max_length=128)),
                ('projectTitle', models.CharField(max_length=100, verbose_name='Project Title')),
                ('projectDescription', models.CharField(max_length=256, verbose_name='Project Description')),
                ('proposalFile', models.FileField(upload_to='projects/proposals', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'csv', 'xlsx', 'docx'])], verbose_name='Proposal')),
                ('dataFile', models.FileField(null=True, upload_to='projects/datasets', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'csv', 'xlsx', 'docx'])], verbose_name='Data')),
                ('resultFile', models.FileField(null=True, upload_to='projects/results', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'csv', 'xlsx', 'docx'])], verbose_name='Results')),
                ('approval', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userEmail', models.EmailField(max_length=256)),
                ('file', models.FileField(upload_to='projects/')),
                ('type', models.IntegerField(blank=True, default=0)),
                ('uploadDate', models.DateTimeField(auto_now=True)),
                ('projectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.project')),
            ],
        ),
    ]
