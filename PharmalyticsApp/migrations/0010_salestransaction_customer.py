# Generated by Django 3.2.24 on 2024-03-03 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PharmalyticsApp', '0009_auto_20240303_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='salestransaction',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PharmalyticsApp.customers'),
        ),
    ]
