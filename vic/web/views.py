from django.shortcuts import render


# Главная страница
def index(request):
    return render(request, 'web/index.html')


