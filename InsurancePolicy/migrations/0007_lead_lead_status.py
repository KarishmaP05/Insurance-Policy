# Generated by Django 5.0.2 on 2024-02-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsurancePolicy', '0006_policy_policy_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='Lead_Status',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=50),
        ),
    ]
