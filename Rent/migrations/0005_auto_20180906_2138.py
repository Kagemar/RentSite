# Generated by Django 2.0.5 on 2018-09-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent', '0004_auto_20180906_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='latitude',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='longitude',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
