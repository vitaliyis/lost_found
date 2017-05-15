from django.db import models
from persons.models import Person
from things.models import Thing


class City(models.Model):
    name = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Country(models.Model):
    name = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

class Mark(models.Model):
    name = models.CharField(max_length=256, blank=False)
    is_active = models.BooleanField()

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'

class Status(models.Model):
    name = models.CharField(max_length=256, blank=False)
    is_active = models.BooleanField()

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Statement(models.Model):
    person = models.ForeignKey(Person)
    thing = models.ForeignKey(Thing)
    when = models.DateField(verbose_name="Дата пропажи/находки: ")
    country = models.ForeignKey(Country)
    city = models.ForeignKey(City)
    address = models.CharField(max_length=256, blank=False, verbose_name="Адрес пропажи/находки: ")
    mark = models.ForeignKey(Mark)
    status = models.ForeignKey(Status)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    # def __str__(self):
    #     return "%s" % (self.name)

    class Meta:
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявления'


