# Generated by Django 5.0.1 on 2024-03-02 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='area',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
