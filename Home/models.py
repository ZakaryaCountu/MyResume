from django.contrib.auth.models import User
from django.db import models
from django.db.models.enums import Choices
from django.utils.text import slugify


#this function for rename any image in media with instance id
def Image_upload(instance,filename) :
    imagename,extension = filename.split(".")

    return "Profile/%s.%s"%(instance.id,extension)


    
# Create your models here.
#this for choice between avaliable and not avaliable
Freelunce_type = (
  ('Avaliable','Avaliable'),
  ('Not Avaliable','Not Avaliable'),
)

class Profile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    dateBirth = models.DateField(auto_now=False, auto_now_add=False)
    website = models.URLField( max_length=200)
    phone_number = models.CharField( max_length=10)
    City = models.ForeignKey("City", on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to=Image_upload)
    Age = models.IntegerField()
    freelance = models.CharField(max_length=20 , choices=Freelunce_type)
    degree = models.CharField(max_length=80)
    title = models.CharField( max_length=100 )
    about = models.TextField(max_length=2000)
    about_sous = models.TextField(max_length=1000)
    
    def __str__(self):
        return str(self.user)



class City(models.Model):
    name = models.CharField( max_length=50)
    

    def __str__(self):
        return self.name


#for skills page
values =(
  ('10','10%'),
  ('20','20%'),
  ('30','30%'),
  ('40','40%'),
  ('50','50%'),
  ('60','60%'),
  ('70','70%'),
  ('80','80%'),
  ('90','90%'),
  ('100','100%'),
)

class Skills(models.Model):
  title = models.CharField( max_length=100)
  Level = models.CharField(max_length = 4, choices=values)
 
  def __str__(self):
    return self.title
  


#for resume page

class Sumary(models.Model):
  description = models.TextField(max_length=1000)
  adresse = models.CharField( max_length=150)
  phone_number = models.CharField(max_length = 10)
  email = models.EmailField( max_length=254)

  def __str__(self):
    return self.email



class Education(models.Model):
  title = models.CharField( max_length=150)
  year = models.CharField(max_length=10)
  Establishment = models.CharField(max_length=200)
  description = models.TextField(max_length = 1000)
  
  def __str__(self):
    return self.title

  
class Experience(models.Model):
  title =  models.CharField( max_length=150)
  year = models.CharField(max_length=10)
  Location = models.CharField(max_length=150)


  def __str__(self):
    return self.title



class Experience_benefits(models.Model):
  Exp = models.ForeignKey(Experience,on_delete=models.CASCADE)
  text = models.TextField(max_length =500)

  def __str__(self):
    return self.text 
  
#for portfolio page
def Image_upload1(instance,filename) :
    imagename,extension = filename.split(".")

    return "Project/%s.%s"%(instance.id,extension)
    
class Project(models.Model):
  title =models.CharField(max_length=80)
  category = models.ForeignKey("Category",on_delete=models.CASCADE)
  image = models.ImageField(upload_to=Image_upload1)
  client =models.ForeignKey("Client",  on_delete=models.CASCADE)
  created_at = models.DateField(auto_now=False, auto_now_add=False)
  url = models.URLField(max_length=200)
  description = models.TextField(max_length=1000)

   
   
  slug = models.SlugField(blank=True, null=True)
    
  def save(self, *args, **kwargs) :
     
      self.slug = slugify(self.title)
      super(Project,self).save(*args, **kwargs)   
        


   
  def __str__(self):
     return self.title




class Category(models.Model):
  name = models.CharField(max_length=80)

  def __str__(self):
    return self.name


class Client(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name




#Service Page ::
ICON_TYPE =(
  ('fas fa-mobile-alt','Mobile App'),
  ('fas fa-desktop','Desktop App'),
  ('fas fa-globe','Web App'),
)

class Service(models.Model):
  title = models.CharField(max_length=100)
  icon_type = models.CharField( max_length=50, choices=ICON_TYPE)
  description = models.TextField(max_length = 200)

  def __str__(self):
    return self.title


#TESTIMONIALS Page ::
def Image_upload2(instance,filename) :
    imagename,extension = filename.split(".")

    return "TESTIMONIALS/%s.%s"%(instance.id,extension)

class TESTIMONIALS(models.Model):
 name = models.CharField(max_length=80)
 work = models.CharField( max_length=80)
 image = models.ImageField( upload_to=Image_upload2)
 description = models.TextField(max_length=1000)

 def __str__(self):
   return self.name



#Contact page ::
class Info(models.Model):
    location = models.CharField( max_length=60)
    phone_number = models.CharField(max_length = 10)
    email = models.EmailField(max_length=254)


    def __str__(self):
       return self.email
