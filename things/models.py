from django.db import models


class ThingCategory(models.Model):
    name = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Категория вещей'
        verbose_name_plural = 'Категории вещей'


class Thing(models.Model):
    name = models.CharField(max_length=256, blank=False)
    thing_category = models.ForeignKey(ThingCategory)
    notes = models.TextField(blank=True, default=None)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'