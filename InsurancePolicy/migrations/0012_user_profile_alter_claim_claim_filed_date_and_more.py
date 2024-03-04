# Generated by Django 5.0.2 on 2024-03-03 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurancePolicy', '0011_employee_alter_claim_claim_filed_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Email_Id', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Date_of_Birth', models.DateField(default=datetime.date(2024, 3, 3))),
                ('Gender', models.CharField(max_length=50)),
                ('FatherName', models.CharField(max_length=50)),
                ('FatherDOB', models.DateField(default=datetime.date(2024, 3, 3))),
                ('MotherName', models.CharField(max_length=50)),
                ('MotherDOB', models.DateField(default=datetime.date(2024, 3, 3))),
                ('MaritalStatus', models.CharField(max_length=50)),
                ('LinkedIn', models.CharField(max_length=50)),
                ('Twitter', models.CharField(max_length=50)),
                ('Instagram', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='claim',
            name='Claim_Filed_Date',
            field=models.DateField(default=datetime.date(2024, 3, 3)),
        ),
        migrations.AlterField(
            model_name='claim',
            name='Claim_Incident_Date',
            field=models.DateField(default=datetime.date(2024, 3, 3)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Follow_up_date',
            field=models.DateField(default=datetime.date(2024, 3, 3)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Date_Of_Birth',
            field=models.DateField(default=datetime.date(2024, 3, 3)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Joining_Date',
            field=models.DateField(default=datetime.date(2024, 3, 3)),
        ),
        migrations.AlterField(
            model_name='lead',
            name='Follow_up_date',
            field=models.DateField(default=datetime.date(2024, 3, 3)),
        ),
        migrations.AlterField(
            model_name='policy',
            name='End_Date',
            field=models.DateField(default=datetime.date(2024, 3, 3)),
        ),
        migrations.AlterField(
            model_name='policy',
            name='Start_Date',
            field=models.DateField(default=datetime.date(2024, 3, 3)),
        ),
    ]