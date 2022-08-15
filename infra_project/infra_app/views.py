from django.http import HttpResponse


def index(request):
    return HttpResponse('Ура, У меня все-таки получилось!')


def second_page(request):
    return HttpResponse('Ура! А это вторая страница!')
