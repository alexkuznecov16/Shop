# Generated by Django 5.1.1 on 2024-09-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_product_description_lv_product_name_lv'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='about_lv',
            field=models.TextField(default='Par kompaniju', help_text='О компании текст на латышском'),
        ),
    ]