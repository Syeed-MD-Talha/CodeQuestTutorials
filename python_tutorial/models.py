from typing import Iterable
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class TopicSection(models.Model):
    rank=models.IntegerField()
    title=models.CharField(max_length=200)
    
    def save(self, *args, **kwargs):
       self.title=self.title.upper()
       super().save(*args, **kwargs) # Call the real save() method
    
    def __str__(self) -> str:
        return f"{self.title} | section: {self.rank}"

class Article(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=False,null=True,blank=True)
    topic=models.ForeignKey(TopicSection,on_delete=models.CASCADE)
    content=RichTextField(blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.topic.title}  ____ {self.title}"
        # return f"{self.title} ..... ___({self.topic.title} )"
