# Generated by Django 4.0.1 on 2022-01-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_shippingaddress_zipcode_order_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=200),
        ),
    ]
