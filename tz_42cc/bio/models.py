# -*- coding: utf-8 -*-

from django.db import models
#imports for signal dispatcher
from django.db.models.signals import post_init, post_save, post_delete
from django.contrib.contenttypes.models import ContentType
from datetime import datetime


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


class HttpRequestData(models.Model):
    path = models.TextField()
    method = models.CharField(max_length=5)
    request = models.TextField()
    cookies = models.TextField(blank=True)
    meta = models.TextField()
    user = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return u'%s %s' % (self.path, self.request)


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
