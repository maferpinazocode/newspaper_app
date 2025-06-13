from django.shortcuts import render

from django.http import HttpResponse

def newsView(request):
    return HttpResponse('Hello Web from view function. Ate, RickAqp 2025/06/12')
