from django.shortcuts import render
from django.http import HttpResponse


gems = [
    {
        'book': 'Matthew',
        'chapter': 24,
        'summary': 'the end is coming',
        'date_entered': 'April 20, 2019'         
    },
    {
        'book': '1 Corinthians',
        'chapter': 7,
        'summary': 'singleness and marriage',
        'date_entered': 'March 1, 2020'         
    },]

#Added a comment
# Create your views here.

def home(request):
    context = {
        'gems': gems
    }
    return render(request, 'study/home.html', context)


def about(request):
    return render(request, 'study/about.html')