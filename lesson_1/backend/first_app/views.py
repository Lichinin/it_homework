from django.http import HttpResponse


def first_one_view(request):
    return HttpResponse('Первое приложение. 1 view')


def first_two_view(request):
    return HttpResponse('Первое приложение. 2 view')


def first_three_view(request):
    return HttpResponse('Первое приложение. 3 view')
