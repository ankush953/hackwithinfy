# Generated by Django 2.1.7 on 2019-08-18 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frame', '0002_framemodel_imagetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framemodel',
            name='variance',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
