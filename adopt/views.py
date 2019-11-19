from django.http import HttpResponse

def index(request):
    return HttpResponse('Hi!How are you!!')
