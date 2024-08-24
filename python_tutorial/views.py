from django.shortcuts import render,get_object_or_404
# from .models import Topic,PythonTutorial
from .models import TopicSection,Article
# Create your views here.
# def homepage(request):
#     topic=Topic.objects.all().order_by('rank','title')
#     details=get_object_or_404(PythonTutorial,slug='introduction-to-python')
#     return render(request,'python_tutorial/base.html',{
#         'topics':topic,
#         'infos':details
#     })

# def topic_detail(request, slug):
#     topics = Topic.objects.all().order_by('rank', 'title')
#     current_topic = get_object_or_404(Topic, slug=slug)
#     return render(request, 'python_tutorial/base.html', {
#         'topics': topics,
#         'infos': current_topic.details
#     })


topic=TopicSection.objects.all().order_by('rank','title')
articles=Article.objects.all()
titles=TopicSection.objects.all().order_by('rank','title')
ls=[]
for title in titles:
        ls.append(title)
        for article in articles:
            if title ==article.topic:
                ls.append(article)

def homepage(request):


    # for article in articles:
    #     print(article,article.topic)
    details=get_object_or_404(Article,slug='introduction-to-python')
    return render(request,'python_tutorial/base.html',{
        'topics':ls,
        'infos':details
    })

def topic_detail(request, slug):
    current_topic = get_object_or_404(Article, slug=slug)
    return render(request, 'python_tutorial/base.html', {
        'topics': ls,
        'infos': current_topic
    })
