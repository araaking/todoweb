from django.db import models

# Create your models here.

class db_todo(models.Model):
    status = (
        ('0','ongoing'),
        ('1','done')
    )
    namaPekerjaan = models.CharField(max_length=200)
    startdate = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=200, choices=status, default=0)
    
    
    
        
    
    def __str__(self):
        return self.namaPekerjaan