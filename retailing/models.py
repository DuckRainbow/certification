from django.db import models


class Contact(models.Model):
    email = models.EmailField(
        verbose_name='email',
        help_text='Укажите email контакта',
    )
    country = models.CharField(
        max_length=100,
        verbose_name='страна',
        help_text='Укажите страну контакта',
    )
    city = models.CharField(
        max_length=50,
        verbose_name='город',
        help_text='Укажите город контакта',
    )
    street = models.CharField(
        max_length=50,
        verbose_name='улица',
        help_text='Укажите улицу контакта',
    )
    building = models.CharField(
        max_length=20,
        verbose_name='номер дома',
        help_text='Укажите номер дома/строения контакта',
    )

    def __str__(self):
        return f'Контакт {self.email}, по адресу {self.country}, г.{self.city} ул.{self.street} д.{self.building}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='название',
        help_text='Укажите название продукта',
    )
    type = models.CharField(
        max_length=25,
        verbose_name='модель',
        help_text='Укажите модель продукта',
    )
    date_of_release = models.DateTimeField(
        auto_now=True,
        verbose_name='дата выхода продукта на рынок',
        help_text='Укажите дату выхода продукта на рынок',
    )

    def __str__(self):
        return f'Продукт {self.title}, модель {self.type}, дата выхода на рынок {self.date_of_release}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Supplier(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        help_text='Укажите название поставщика',
    )

    contacts = models.ManyToManyField(
        Contact,
        verbose_name='Контакты',
        help_text='Укажите контакты поставщика',
    )

    products = models.ManyToManyField(
        Product,
        verbose_name='Продукты',
        help_text='Укажите продукты поставщика',
    )

    supplier = models.ForeignKey(
        'self',
        verbose_name='Поставщик',
        help_text='Укажите поставщика продуктов',
    )

    debt = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name='Задолженность перед поставщиком',
        help_text='Укажите задолженность перед поставщиком',
    )

    created_time = models.DateTimeField(
        auto_created=True,
        verbose_name='Время создания',
    )

    LEVEL_CHOICES = {
        0: 'завод',
        1: 'розничная сеть',
        2: 'индивидуальный предприниматель'
    }

    level = models.CharField(
        choices=LEVEL_CHOICES,
    )

    def __str__(self):
        return (
            f'Поставщик {self.title}, контакты {self.contacts}, продукты {self.products}, поставщик {self.supplier},'
            f'задолженность перед поставщиком {self.debt}, время создания {self.created_time}'\
            )

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
