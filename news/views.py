from django.shortcuts import render

from django.http import HttpResponse

def newsView(request):
    return HttpResponse('Hello Web from view function. Ate, Maria Fernanda Pinazo 2025/06/13')
