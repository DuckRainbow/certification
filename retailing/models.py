from django.db import models


class Supplier(models.Model):
    title = models.CharField(

    )
    contact = models.ForeignKey(

    )
    products = models.ManyToManyField(

    )
    supplier = models.ForeignKey(

    )
    debt = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )
    created_time = models.DateTimeField(
        auto_created=True
    )
    LEVEL_CHOICES = {
        0: 'завод',
        1: 'розничная сеть',
        2: 'индивидуальный предприниматель'
    }
    level = models.CharField(
        choices=LEVEL_CHOICES,
    )

    class Meta:
        pass


class Contact(models.Model):
    email = models.CharField(

    )
    country = models.CharField(

    )
    city = models.CharField(

    )
    street = models.CharField(

    )
    building = models.CharField(

    )

    class Meta:
        pass


class Product(models.Model):
    title = models.CharField(

    )
    type = models.CharField(

    )
    date_of_release = models.DateTimeField(

    )
