# Generated by Django 4.2.5 on 2023-11-30 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PharmalyticsApp', '0006_remove_medication_substitute_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='chemicalcomposition',
            field=models.CharField(max_length=200),
        ),
    ]