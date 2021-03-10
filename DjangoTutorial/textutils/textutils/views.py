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
    #params={'name':'Ankit','place':'bihar'}
    #return HttpResponse("Home")
    #return render(request,'index.html',params)
    return render(request,'index.html')



def removepunc(request):
    print(request.GET.get("text","default"))
    return HttpResponse("Remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")
def newlineremove(request):
    return HttpResponse("newlineremover")
def spaceremove(request):
    return HttpResponse("space remover")
def charcount(request):
    return HttpResponse("char count")