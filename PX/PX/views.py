from django.http import HttpResponse


def hello(request):
    return HttpResponse('<h1> I guess it works </h1>')

