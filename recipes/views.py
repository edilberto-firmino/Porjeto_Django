from django.shortcuts import HttpResponse, render


def home(resquest):
    return render(resquest, 'recipes/pages/home.html')
