from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'home/home_page.html')

def about_page(request):
    return render(request,'home/about_page.html')

def tutorials_page(request):
    return render(request,'home/tutorials.html')

def contact_page(request):
    return render(request,'home/contact.html')