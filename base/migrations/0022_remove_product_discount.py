# Generated by Django 5.1.1 on 2024-10-05 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_company_about_lv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
    ]