# Generated by Django 3.0.2 on 2020-08-26 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20200826_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdesc',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]