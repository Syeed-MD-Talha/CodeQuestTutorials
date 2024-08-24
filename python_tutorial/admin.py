from django.contrib import admin
from .models import TopicSection,Article



class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}
    ordering = ('topic__title',)
    
class TopicSectionAdmin(admin.ModelAdmin):
    ordering = ('rank', 'title')
       
admin.site.register(TopicSection,TopicSectionAdmin)
admin.site.register(Article, ArticleAdmin)