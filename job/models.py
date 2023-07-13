
from django.contrib.auth.models import User
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
       owner = models.ForeignKey(User , related_name='job_owner', on_delete= models.CASCADE)
       title = models.CharField(max_length=100) #column
       
       job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
       description = models.TextField(max_length=1000)
       published_at = models.DateTimeField(auto_now=True)
       vacancy = models.IntegerField(default=1)
       salary = models.IntegerField(default=0)
       experience = models.IntegerField(default=3)
       Category = models.ForeignKey('Category', on_delete= models.CASCADE)
       image = models.ImageField(upload_to= image_upload)
       slug = models.SlugField(blank=True , null= True)
       
      
       def save(self,*args, **kewords) :
          self.slug = self.title
          super(Job,self).save(*args , **kewords)
      
      
      #        Job-----------------

       def __str__(self) :
              return self.title 
       

class Category(models.Model):
       name = models.CharField(max_length=30)  

#     Category-----------------
       def __str__(self) :
              return self.name

class Apply(models.Model) :
      job = models.ForeignKey(Job, related_name='job_apply' , on_delete= models.CASCADE)
      name = models.CharField(max_length= 50)
      email = models.EmailField()
      website = models.URLField()
      cv = models.FileField(upload_to='apply/')
      coverletter = models.TextField(max_length= 500)
#       mobile = models.IntegerField(max_length= 12)
      applied_at = models.DateTimeField(auto_now=True)
      
#   Apply-----------------
      def __str__(self):
          return self.name 


