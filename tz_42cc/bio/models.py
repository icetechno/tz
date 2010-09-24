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
                            blank = True)
 
    def __unicode__(self):
        return u'%s %s' % (self.name, self.surname)
         