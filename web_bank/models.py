import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Client(models.Model):
    firstname = models.CharField(
        max_length=50,
        verbose_name='firstname',
        blank=False,
        null=False
    )
    lastname = models.CharField(
        max_length=50,
        verbose_name='lastname',
        blank=False,
        null=False
    )
    birthdate = models.DateField(
        verbose_name='birthdate',
        validators=[MaxValueValidator(datetime.date.today() - datetime.timedelta(days=14 * 365))]
    )
    age = models.SmallIntegerField(
        verbose_name='age',
        validators=[MinValueValidator(14)]
    )
    address = models.CharField(
        max_length=100,
        verbose_name='address'
    )
    sex_list = [
        ('m', 'male'),
        ('f', 'female')
    ]
    sex = models.CharField(
        max_length=20,
        verbose_name='sex',
        blank=False,
        null=False,
        choices=sex_list
    )
    products = models.ManyToManyField(
        'Product',
        verbose_name='product',
        blank=True
    )

    class Meta:
        unique_together = ('firstname', 'lastname')
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['firstname', 'lastname']


class Product(models.Model):
    product_name = models.CharField(
        max_length=50,
        verbose_name='product_name',
        blank=False,
        null=False
    )
    cred_type = models.CharField(
        max_length=50,
        verbose_name='type',
        blank=False,
        null=False
    )
    clients = models.ManyToManyField(
        'Client',
        verbose_name='clients',
        blank=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    start_date = models.DateField(
        verbose_name='start_date',
        validators=[MaxValueValidator(datetime.date.today())]
    )
    end_date = models.DateField(
        verbose_name='end_date',
        validators=[MinValueValidator(datetime.date.today())],
        blank=True,
        null=True
    )

    class Meta:
        indexes = [models.Index(fields=['product_name'])]
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['product_name']
