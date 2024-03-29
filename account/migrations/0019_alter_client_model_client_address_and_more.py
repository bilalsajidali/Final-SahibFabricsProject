# Generated by Django 4.2.7 on 2024-02-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_remove_billing_model_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_model',
            name='client_address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='client_model',
            name='client_balance',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='client_model',
            name='client_city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client_model',
            name='client_cnic',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client_model',
            name='client_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client_model',
            name='client_ph',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='thaans_model',
            name='Thaan_Category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='thaans_model',
            name='Thaan_Gazana',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='thaans_model',
            name='Thaan_Model',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='thaans_model',
            name='Thaan_Price_Per_Meter',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='thaans_model',
            name='Thaan_Qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='thaans_model',
            name='Thaan_Shop_No',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
