# Generated by Django 4.2.7 on 2024-02-01 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_remove_billing_model_client_balance_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='billing_model',
        ),
    ]
