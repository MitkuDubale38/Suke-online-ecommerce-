# Generated by Django 2.2.14 on 2021-08-04 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sukeachin', '0017_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Payment_method',
            field=models.CharField(choices=[('cash_on_delivery', 'cash_on_delivery'), ('paypal', 'paypal'), ('payoneer', 'payoneer'), ('direct_bank_transfer', 'direct_bank_transfer')], default='Cash on Delivery', max_length=50),
        ),
    ]
