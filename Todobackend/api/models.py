from django.db import models

# Create your models here.

class Contact(models.Model): 
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    
    def __str__(self):
        return self.name

       

    


        
    
