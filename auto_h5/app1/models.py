from django.db import models

# Create your models here.


   
class Animal( models.Model ):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
      
    class Meta:
        db_table = 'app1_animal'