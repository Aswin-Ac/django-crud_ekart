# Generated by Django 4.2.6 on 2023-11-09 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eKart_admin', '0002_category'),
        ('seller', '0002_alter_product_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eKart_admin.category'),
        ),
    ]