from django.shortcuts import render

def index(request):
    return render(request,'intro_page.html')

def first(request):
    return render(request,'first_page.html')
# Create your views here.
