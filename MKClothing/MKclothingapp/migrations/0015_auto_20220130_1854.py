# Generated by Django 3.2.8 on 2022-01-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MKclothingapp', '0014_auto_20220130_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderc',
            name='cancels',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orderc',
            name='success',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orderc',
            name='totalorders',
            field=models.IntegerField(default=0),
        ),
    ]
