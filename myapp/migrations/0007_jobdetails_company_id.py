# Generated by Django 4.1.3 on 2022-11-09 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_jobdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetails',
            name='company_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.company'),
        ),
    ]
