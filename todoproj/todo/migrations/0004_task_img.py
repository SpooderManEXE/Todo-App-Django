# Generated by Django 3.0.3 on 2020-10-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20201008_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='img',
            field=models.ImageField(default='ss', upload_to='images/'),
            preserve_default=False,
        ),
    ]
