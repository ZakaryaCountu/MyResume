# Generated by Django 3.1.2 on 2020-10-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_profile_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
