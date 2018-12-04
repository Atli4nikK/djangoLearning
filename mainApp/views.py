from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html',
                  {'values': ['Контактный телефон', '(918) 123-45-67', 'example@gmail.com']})
