# Generated by Django 3.2.7 on 2021-10-12 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='resource',
            field=models.FileField(upload_to='resource'),
        ),
    ]
