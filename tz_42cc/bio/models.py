# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
#imports for signal dispatcher
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_init, post_save, post_delete


#That class represents a person
class Person(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name=u'Имя:')
    surname = models.CharField(max_length=255,
                            verbose_name=u'Фамилия:')
    bio = models.TextField(max_length=255,
                            blank=True,
                            verbose_name=u'Биография:')
    contacts = models.CharField(max_length=255,
                            verbose_name=u'Контакты:')
    birthdate = models.DateField(verbose_name=u'Дата рождения:',
                            blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.surname)


def get_choices():
    result = tuple()
    for i in range(0, 10):
        result += (i, 'Priority %d' % (i + 1)),

    return result


class HttpRequestData(models.Model):

    PRIORITY_CHOICES = get_choices()

    path = models.TextField()
    method = models.CharField(max_length=5)
    request = models.TextField()
    cookies = models.TextField(blank=True)
    meta = models.TextField()
    user = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now)
    priority = models.IntegerField(choices=PRIORITY_CHOICES,
                            default=0,
    )

    def __unicode__(self):
        return u'%s %s' % (self.path, self.request, self.priority)


class SignalLog(models.Model):
    souce = models.CharField(max_length=254)
    type = models.CharField(max_length=15)

    def __unicode__(self):
        return u'%s %s' % (self.type, self.souce)


def my_callback(sender, **kwargs):
    if sender == SignalLog:             # don`t log self
        return
    elif sender == ContentType:           # dont fail django test
        return

    try:
        # get signal from kwargs arguments
        signal = kwargs.get('signal')
        # get dispatch_uid if present
        action = signal.__dict__['receivers'][0][0][0]
    except:
        action = 'can`t detect'
    signal_log = SignalLog(souce=str(sender), type=action)
    signal_log.save()

post_init.connect(my_callback, dispatch_uid='init')
post_save.connect(my_callback, dispatch_uid='save')
post_delete.connect(my_callback, dispatch_uid='delete')
