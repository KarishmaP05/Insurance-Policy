# Generated by Django 5.0.2 on 2024-02-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurancePolicy', '0002_lead'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='Assign_to',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='Customer_Type',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='Email_Id',
        ),
        migrations.AddField(
            model_name='lead',
            name='LOB',
            field=models.CharField(default='Engineering', max_length=50),
        ),
    ]
