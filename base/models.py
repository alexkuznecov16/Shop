from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=("Наименование товара"), default='Наименование по умолчанию')
    
    description = models.TextField(verbose_name=("Описание товара"), default='Описание по умолчанию')
    
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=("Стоимость товара в евро"))
    startPrice = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Начальная стоимость товара", default=0.00)
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Скидка в процентах", default=0.00)
    available = models.BooleanField(default=True, verbose_name=("Доступность товара"))
    
    image = models.ImageField(upload_to='images/', verbose_name=("Изображение товара"), null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = ("Товар")
        verbose_name_plural = ("Товары")
      
      
class Company(models.Model):
    name = models.CharField(max_length=255, help_text="название компании", default="Название компании")
    phone_number = models.CharField(max_length=20, help_text="номер телефона", default="Номер телефона")
    email = models.EmailField(help_text="gmail почта", default="example@example.com")
    telegram_link = models.URLField(blank=True, null=True, help_text="ссылка на контакт в телеграм", default="")
    youtube_link = models.URLField(blank=True, null=True, help_text="ссылка на ютуб канал", default="")
    whatsapp_link = models.URLField(blank=True, null=True, help_text="ссылка на контакт в ватсапп", default="")
    address = models.CharField(max_length=255, help_text="адрес компании", default="Адрес компании")
    about = models.TextField(help_text="О компании текст", default="О компании")
    
    # Изменение поля для изображения
    location_image = models.ImageField(upload_to='images/', blank=True, null=True, help_text="картинка города (где базируется компания)", default='images/jurmala.jpg')
    intro_img = models.ImageField(upload_to='images/', blank=True, null=True, help_text="картинка города (где базируется компания)", default='images/intro.jpg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компания"
