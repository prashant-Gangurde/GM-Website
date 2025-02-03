# Generated by Django 5.1.3 on 2025-02-03 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('mobile', models.IntegerField(unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=40)),
                ('email_add', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GmServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_name', models.CharField(max_length=100)),
                ('services_period', models.IntegerField()),
                ('services_fess', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=100)),
                ('vacancies', models.IntegerField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fees', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('adhar', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=30)),
                ('avatar', models.ImageField(upload_to='avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Family_lead', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Mukhiya', to='home.person')),
                ('members', models.ManyToManyField(related_name='families', to='home.person')),
            ],
        ),
    ]
