# Generated by Django 4.0.3 on 2022-04-04 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_alter_recommended_graphx_alter_recommended_graphy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='feedback',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
