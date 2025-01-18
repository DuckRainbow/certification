from django.db import models


class Contact(models.Model):
    email = models.EmailField(
        verbose_name='email',
        help_text='',
    )
    country = models.CharField(
        max_length=100,
        verbose_name='страна',
        help_text='',
    )
    city = models.CharField(
        max_length=50,
        verbose_name='город',
        help_text='',
    )
    street = models.CharField(
        max_length=50,
        verbose_name='улица',
        help_text='',
    )
    building = models.CharField(
        max_length=20,
        verbose_name='номер дома',
        help_text='',
    )

    def __str__(self):
        return f' '

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='название',
        help_text='',
    )
    type = models.CharField(
        max_length=25,
        verbose_name='модель',
        help_text='',
    )
    date_of_release = models.DateTimeField(
        auto_now=True,
        verbose_name='',
        help_text='дата выхода продукта на рынок',
    )

    def __str__(self):
        return f' '

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Supplier(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        help_text='',
    )

    contact = models.ManyToManyField(
        Contact,
        verbose_name='Контакты',
        help_text='',
    )

    products = models.ManyToManyField(
        Product,
        verbose_name='Продукты',
        help_text='',
    )

    supplier = models.ForeignKey(
        'self',
        verbose_name='Поставщик',
        help_text='',
    )

    debt = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name='Задолженность перед поставщиком',
        help_text='',
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
        return f' '

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
