# Generated by Django 5.0.1 on 2024-01-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='rasm',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
