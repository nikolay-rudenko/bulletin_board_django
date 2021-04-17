from django.http import HttpResponse

def index(request):
    print(request)
    return HttpResponse("Here will be list of bulletin")



