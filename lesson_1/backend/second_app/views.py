# from django.shortcuts import render
from django.http import HttpResponse


def second_one_view(request):
    return HttpResponse('Второе приложение. 1 view')

def second_two_view(request):
    return HttpResponse('Второе приложение. 2 view')

def second_thee_view(request):
    return HttpResponse('Второе приложение. 3 view')
