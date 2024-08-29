# from django.shortcuts import render,get_object_or_404
# from django.views import View
# from .models import *
# from collections import defaultdict


# # Create your views here.
# ar={}
# topics=TopicSection.objects.all() 
# details=Article.objects.all()

# for detail in details:
#     Topic=detail.topic.title
#     Icon=detail.topic.icon
#     if (Topic,Icon) not in ar:ar[(Topic,Icon)]=[]
#     ar[(Topic,Icon)].append(detail)



# class HomePage(View):        
#     def get(self,request):
#         return render(request,'django_tutorial/homePage.html',{
#             'topics':ar,
#         })


# class TopicDetails(View):
#     def get(self,request,slug):
#         current_topic=get_object_or_404(Article,slug=slug)
#         return render(request,'django_tutorial/homePage.html',{
#             'topics':ar,
#             'infos':current_topic,
#         })

from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import TopicSection, Article
from collections import defaultdict

def get_organized_articles():
    ar = {}
    topics = TopicSection.objects.all()
    details = Article.objects.all().order_by('rank')

    for detail in details:
        Topic = detail.topic.title
        Icon = detail.topic.icon
        if (Topic, Icon) not in ar:
            ar[(Topic, Icon)] = []
        ar[(Topic, Icon)].append(detail)
    
    return ar

class HomePage(View):        
    def get(self, request):
        ar = get_organized_articles()
        current_topic = get_object_or_404(Article, slug='what-is-django')
        return render(request, 'django_tutorial/index.html', {
            'topics': ar,
            'infos': current_topic,
        })

class TopicDetails(View):
    def get(self, request, slug):
        ar = get_organized_articles()
        current_topic = get_object_or_404(Article, slug=slug)
        return render(request, 'django_tutorial/index.html', {
            'topics': ar,
            'infos': current_topic,
        })