# Generated by Django 4.0.6 on 2022-08-04 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_rename_phone (ddd + number)_company_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.address'),
        ),
    ]
