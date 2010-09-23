from django.db import models
#imports for signal dispatcher
from django.db.models.signals import post_init, post_save, post_delete

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
    birthdate =  models.DateField(verbose_name = 'Birth date',
                            blank = True)
    
class HttpRequestData(models.Model):
    path =  models.TextField()
    method = models.CharField(max_length = 5)
    request = models.TextField()
    cookies = models.TextField(blank = True) 
    meta = models.TextField()
    user = models.TextField(blank = True)
    date = models.DateTimeField(auto_now_add = True)
    
def my_callback(sender, **kwargs):
    print "Request finished!"
    
post_init.connect(my_callback)
post_save.connect(my_callback)
post_delete.connect(my_callback)    