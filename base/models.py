from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=255, verbose_name=("Наименование товара"), default='Наименование по умолчанию')
  
  description = models.TextField(verbose_name=("Описание товара"), default='Описание по умолчанию')
  
  price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=("Стоимость товара в евро"))
  available = models.BooleanField(default=True, verbose_name=("Доступность товара"))
  
  image = models.ImageField(upload_to='media/', verbose_name=("Изображение товара"), null=True, blank=True)

  def __str__(self) -> str:
      return self.name

  class Meta:
      verbose_name = ("Товар")
      verbose_name_plural = ("Товары")