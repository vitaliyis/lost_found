from django.db import models
from statements.models import Statement
from persons.models import Person

class Message(models.Model):
    person_from = models.ForeignKey(Person,related_name='person_from', verbose_name="От кого: ")
    person_to = models.ForeignKey(Person, verbose_name="Кому: ")
    subject = models.CharField(max_length=256, blank=False, verbose_name="Тема: ")
    letter = models.TextField(default=None, blank=False, verbose_name="Текст: ")

    def __str__(self):
        return "%s" % (self.subject)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

