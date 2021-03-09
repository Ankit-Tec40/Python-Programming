#this created by Ankit
from django.http import HttpResponse
def index(request):
    f=open('text.txt','r')
    text=f.read()
    return HttpResponse(text)
    f.close()

def about(request):
    return HttpResponse("about Ankit")
