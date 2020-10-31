# Generated by Django 3.1.2 on 2020-10-28 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_education_experience_experience_benefits_sumary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to='Project/')),
                ('created_at', models.DateField()),
                ('url', models.URLField()),
                ('description', models.TextField(max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.category')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.client')),
            ],
        ),
    ]
