from django.http import HttpResponse


def third_one_view(request):
    return HttpResponse('Третье приложение. 1 view')


def third_two_view(request):
    return HttpResponse('Третье приложение. 2 view')


def third_three_view(request):
    return HttpResponse('Третье приложение. 3 view')
