# Generated by Django 5.0.7 on 2024-08-04 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="license_number",
            field=models.CharField(max_length=43, unique=True),
        ),
    ]
