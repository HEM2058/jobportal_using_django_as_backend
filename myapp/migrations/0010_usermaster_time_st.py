# Generated by Django 4.1.3 on 2022-11-11 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_jobdetails_companyaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermaster',
            name='time_st',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
