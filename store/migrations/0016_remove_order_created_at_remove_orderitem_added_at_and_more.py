# Generated by Django 4.0.1 on 2022-02-09 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_remove_product_created_at_alter_customer_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='added_at',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='created_at',
        ),
    ]
