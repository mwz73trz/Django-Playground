from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, dear Reader.  This is the index of our app.")
