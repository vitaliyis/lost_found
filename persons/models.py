from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=256, blank=False)
    last_name = models.CharField(max_length=256, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=128, blank=False)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'