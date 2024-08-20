from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='python_tutorial'),
     path('topic/<slug:slug>/', views.topic_detail, name='topic_detail'),
    # path('hello_world/',views.hello_world,name='hello_world')
]
