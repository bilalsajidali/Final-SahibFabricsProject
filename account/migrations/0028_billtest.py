# Generated by Django 4.2.7 on 2024-02-02 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0027_delete_billing_testm'),
    ]

    operations = [
        migrations.CreateModel(
            name='billtest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.client_model')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.thaans_model')),
            ],
        ),
    ]
