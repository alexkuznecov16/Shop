# Generated by Django 5.1.1 on 2024-09-05 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_product_description_af_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_lv',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_lv',
        ),
        migrations.AddField(
            model_name='product',
            name='descriptionLv',
            field=models.TextField(default='Описание по умолчанию', verbose_name='Описание товара на латышском'),
        ),
        migrations.AddField(
            model_name='product',
            name='nameLv',
            field=models.CharField(default='Наименование по умолчанию', max_length=255, verbose_name='Наименование товара на латышском'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='Описание по умолчанию', verbose_name='Описание товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='Наименование по умолчанию', max_length=255, verbose_name='Наименование товара'),
        ),
    ]
