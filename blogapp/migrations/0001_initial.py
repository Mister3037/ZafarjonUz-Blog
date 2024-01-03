# Generated by Django 5.0.1 on 2024-01-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=100)),
                ('rasm', models.ImageField(blank=True, null=True, upload_to='')),
                ('matn', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomePostNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250)),
                ('matn', models.TextField()),
                ('rasm', models.ImageField(upload_to='media')),
                ('url', models.URLField(blank=True)),
                ('yaratilgan_sana', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-yaratilgan_sana'],
            },
        ),
    ]
