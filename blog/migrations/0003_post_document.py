# Generated by Django 2.2.13 on 2020-10-25 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201026_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='document',
            field=models.FileField(default='placeholder.pdf', upload_to='media'),
        ),
    ]
