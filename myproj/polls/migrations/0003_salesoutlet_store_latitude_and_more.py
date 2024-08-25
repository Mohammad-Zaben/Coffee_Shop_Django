# Generated by Django 4.2.15 on 2024-08-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_customer_customer_id_alter_product_product_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesoutlet',
            name='store_latitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='salesoutlet',
            name='store_longitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
    ]
