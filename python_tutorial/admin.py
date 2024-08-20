from django.contrib import admin
from .models import PythonTutorial,Topic
# Register your models here.
class PythonTutorialAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}

class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}
    # list_display = ('title', 'rank')
    # list_editable = ('rank',)
    ordering = ('rank', 'title')


admin.site.register(PythonTutorial,PythonTutorialAdmin)
admin.site.register(Topic,TopicAdmin)