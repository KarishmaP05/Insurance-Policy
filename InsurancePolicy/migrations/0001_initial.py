# Generated by Django 5.0.2 on 2024-02-23 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Phone_No', models.IntegerField()),
                ('Email_Id', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=50)),
                ('Reference', models.CharField(max_length=50)),
                ('Follow_up_date', models.DateField(default=datetime.date(2024, 2, 23))),
                ('Notes', models.CharField(max_length=1000)),
                ('Customer_Type', models.CharField(max_length=50)),
                ('Assign_to', models.CharField(max_length=50)),
            ],
        ),
    ]
