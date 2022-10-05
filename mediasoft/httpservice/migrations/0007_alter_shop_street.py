# Generated by Django 4.1.1 on 2022-10-05 03:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("httpservice", "0001_squashed_0006_shop_street_alter_shop_city"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop",
            name="street",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="httpservice.street"
            ),
        ),
    ]