# Generated by Django 3.0.3 on 2020-10-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20201008_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
