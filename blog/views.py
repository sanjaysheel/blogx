from django.shortcuts import render
from .models import Post

from django.http import HttpResponse
# Create your views here.

post=[
    {
        "author":'jorge',
        'title':'blog post',
        'conetnt':'first blog post',
        'date post':'august 27,2020'
    },
    {
        "author": 'jorge',
        'title': 'blog post',
        'conetnt': 'second blog post',
        'datepost': 'august 28,2020'
    }
]



def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/template.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About page'})