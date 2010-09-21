from django.db import models

#That class represents a person
class Person(models.Model):
    name =      models.CharField(max_length = 255,
                            blank = False,
                            verbose_name = 'Name')  
    surname =   models.CharField(max_length = 255,
                            blank = False,
                            verbose_name = 'Surname')    
    bio =       models.TextField(max_length = 255,
                            blank = True,
                            verbose_name = 'Biography')  
    contacts =  models.CharField(max_length = 255,
                            blank = False,
                            verbose_name = 'Contacts') 