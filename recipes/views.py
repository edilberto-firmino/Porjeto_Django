from django.shortcuts import HttpResponse, render


def home(resquest):
    return render(resquest, 'recipes/home.html')


def contato(request):
    return render(request, 'recipes/contato.html')


def sobre(request):
    return HttpResponse('sobre')
