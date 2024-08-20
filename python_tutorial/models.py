from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class PythonTutorial(models.Model):
    title=models.CharField(max_length=500)
    slug=models.SlugField(unique=False,null=True,blank=True)
    content=RichTextField(blank=True, null=True,default='No content yet')
    
    def __str__(self) -> str:
        return self.title

class Topic(models.Model):
    rank=models.IntegerField(blank=True,null=True)
    title=RichTextField(blank=True, null=True,default='No content yet')
    slug=models.SlugField(unique=False,null=True,blank=True)
    details=models.OneToOneField(PythonTutorial,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.details.title} ---- {self.rank}"
    
    def get_absolute_url(self):
        if self.slug != 'heading':
         return reverse('topic_detail', kwargs={'slug': self.slug})
        return '#'