#creatyed by ankit
from django.http import HttpResponse
def index(request):
    return HttpResponse('''<a href="https://www.facebook.com/">facebook</a>''')