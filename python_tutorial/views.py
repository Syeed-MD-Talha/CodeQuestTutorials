from django.shortcuts import render,get_object_or_404
from .models import Topic,PythonTutorial
# Create your views here.
def homepage(request):
    topic=Topic.objects.all().order_by('rank','title')
    details=get_object_or_404(PythonTutorial,slug='introduction-to-python')
    return render(request,'python_tutorial/base.html',{
        'topics':topic,
        'infos':details
    })


def topic_detail(request, slug):
    topics = Topic.objects.all().order_by('rank', 'title')
    current_topic = get_object_or_404(Topic, slug=slug)
    return render(request, 'python_tutorial/base.html', {
        'topics': topics,
        'infos': current_topic.details
    })

