# -*- coding: utf-8 -*-

from django.db import models

#That class represents a person
class Person(models.Model):
    name =      models.CharField(max_length = 255,
                            blank = False,
                            verbose_name = u'Имя:')  
    surname =   models.CharField(max_length = 255,
                            blank = False,
                            verbose_name = u'Фамилия:')    
    bio =       models.TextField(max_length = 255,
                            blank = True,
                            verbose_name = u'Биография:')  
    contacts =  models.CharField(max_length = 255,
                            blank = False,
                            verbose_name = u'Контакты:')
    birthdate =  models.DateField(verbose_name = u'Дата рождения:',
                            blank = False)
 
    def __unicode__(self):
        return u'%s %s' % (self.name, self.surname)
           
class HttpRequestData(models.Model):
    path =  models.TextField()
    method = models.CharField(max_length = 5)
    request = models.TextField()
    cookies = models.TextField(blank = True) 
    meta = models.TextField()
    user = models.TextField(blank = True)
    date = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return u'%s %s' % (self.path, self.method)
    