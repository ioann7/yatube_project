# Generated by Django 2.2.9 on 2022-09-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220903_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
