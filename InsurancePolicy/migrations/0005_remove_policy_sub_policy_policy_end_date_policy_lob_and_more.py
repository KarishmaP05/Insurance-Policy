# Generated by Django 5.0.2 on 2024-02-24 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurancePolicy', '0004_policy_alter_customer_follow_up_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policy',
            name='Sub_Policy',
        ),
        migrations.AddField(
            model_name='policy',
            name='End_Date',
            field=models.DateField(default=datetime.date(2024, 2, 24)),
        ),
        migrations.AddField(
            model_name='policy',
            name='LOB',
            field=models.CharField(default='Engineering', max_length=50),
        ),
        migrations.AddField(
            model_name='policy',
            name='Start_Date',
            field=models.DateField(default=datetime.date(2024, 2, 24)),
        ),
    ]