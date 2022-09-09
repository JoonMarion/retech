# Generated by Django 4.1.1 on 2022-09-09 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0013_address_cep"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="cep",
            field=models.CharField(default="", max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="complement",
            field=models.CharField(default="", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="district",
            field=models.CharField(default="", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="number",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="address",
            name="state",
            field=models.CharField(default="", max_length=2),
        ),
        migrations.AlterField(
            model_name="address",
            name="street",
            field=models.CharField(default="", max_length=100, null=True),
        ),
    ]