# Generated by Django 4.2.6 on 2023-10-13 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('picture', models.ImageField(upload_to='seller/')),
                ('account_number', models.CharField(max_length=30)),
                ('ifsc', models.CharField(max_length=20)),
                ('login_id', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('status', models.CharField(default='pending', max_length=50)),
            ],
        ),
    ]
