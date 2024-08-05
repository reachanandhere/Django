from django.http import HttpResponse


def home(request):
    return HttpResponse("Home Page")

def rooms(request):
    return HttpResponse('Room')
