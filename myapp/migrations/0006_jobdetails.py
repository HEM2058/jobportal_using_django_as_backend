# Generated by Django 4.1.3 on 2022-11-09 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_company_firstname_company_lastname'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(max_length=250)),
                ('companyname', models.CharField(max_length=250)),
                ('jobdescription', models.CharField(max_length=250)),
                ('qualification', models.CharField(max_length=250)),
                ('responsibilities', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('companyemail', models.CharField(max_length=50)),
                ('companycontact', models.CharField(max_length=50)),
                ('salarypackage', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
            ],
        ),
    ]
