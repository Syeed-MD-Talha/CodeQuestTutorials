from django.urls import path
from . import views

urlpatterns = [
   path('',views.HomePage.as_view(),name='django_tutorial'),
   path('<slug:slug>',views.TopicDetails.as_view())
]
