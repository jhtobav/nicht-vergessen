from django.http import HttpResponse


def notes(request):
    return HttpResponse("Hello, world. You're at the polls index.")