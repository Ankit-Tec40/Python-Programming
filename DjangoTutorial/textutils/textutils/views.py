#this created by Ankit
from django.http import HttpResponse
from django.shortcuts import render
"""
def index(request):
    f=open('text.txt','r')
    text=f.read()
    return HttpResponse(text)
    f.close()

def about(request):
    return HttpResponse("about Ankit")
"""
def index(request):
    #return HttpResponse("Home")
    return render(request,'index.html')


def removepunc(request):
    return HttpResponse("Remove punc")
def capfirst(request):
    return HttpResponse("capitalize first")
def newlineremove(request):
    return HttpResponse("newlineremover")
def spaceremove(request):
    return HttpResponse("space remover")
def charcount(request):
    return HttpResponse("char count")