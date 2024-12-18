# Generated by Django 5.1.1 on 2024-09-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_company_intro_img_alter_company_location_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='intro_img',
            field=models.ImageField(blank=True, default='../Company/static/images/intro.jpg', help_text='картинка города (где базируется компания)', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='location_image',
            field=models.ImageField(blank=True, default='../Company/static/images/jurmala.jpg', help_text='картинка города (где базируется компания)', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение товара'),
        ),
    ]
