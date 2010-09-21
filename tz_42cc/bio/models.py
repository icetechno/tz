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
    
    
class HttpRequestData(models.Model):
    path =  models.TextField()
    method = models.CharField(max_length = 5)
    request = models.TextField()
    cookies = models.TextField(blank = True) 
    meta = models.TextField()
    user = models.TextField(blank = True)
    date = models.DateTimeField(auto_now_add = True)