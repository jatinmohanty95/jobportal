# Generated by Django 3.0.2 on 2020-08-26 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantdata',
            name='resume',
            field=models.FileField(null=True, upload_to='D:\\dj8amdec\\jobportal1\\media'),
        ),
    ]