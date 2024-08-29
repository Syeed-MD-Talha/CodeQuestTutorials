from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.
class TopicSection(models.Model):
    rank=models.IntegerField()
    title=models.CharField(max_length=200)
    icon = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.title} | section: {self.rank}"

class Article(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=False,null=True,blank=True)
    topic=models.ForeignKey(TopicSection,on_delete=models.CASCADE)
    content=RichTextField(blank=True, null=True)
    rank=models.IntegerField(null=True,default=1)
    def __str__(self) -> str:
        return f"{self.topic.title}  ____ {self.title}"
