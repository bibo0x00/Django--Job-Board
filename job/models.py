from django.db import models

# Create your models here.
# django model field 
# html widget 
#  validation
# database size

JOB_TYPE = (
       ('Full Time','Full Time') ,
       ('Part Time','Part Time') ,
)

def image_upload(instance , filename):
     
     image_name , extention = filename.split(".")
     return "jobs/%s.%s"%( instance.id , extention )
      
   
class Job(models.Model) : #table
       
       title = models.CharField(max_length=100) #column
       
       job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
       description = models.TextField(max_length=1000)
       published_at = models.DateTimeField(auto_now=True)
       vacancy = models.IntegerField(default=1)
       salary = models.IntegerField(default=0)
       experience = models.IntegerField(default=3)
       Category = models.ForeignKey('Category', on_delete= models.CASCADE)
       image = models.ImageField(upload_to= image_upload)

       def __str__(self) :
              return self.title 
       

class Category(models.Model):
       name = models.CharField(max_length=30)  

       def __str__(self) :
              return self.name
