# Generated by Django 3.1.1 on 2020-09-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200914_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=models.TextField(max_length=2500),
        ),
    ]
