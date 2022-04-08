# Generated by Django 4.0.3 on 2022-04-05 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0005_alter_buycoins_price_alter_buycoins_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buycoins',
            name='qty',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
