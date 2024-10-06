from django.shortcuts import render

# Create your views here.


def homePage(request):
    return render(request, 'home.html')


def navebar(request):
    return render(request, 'nav.html')


def contactPage(request):
    return render(request, 'contact.html')


def travelPage(request):
    return render(request, 'travel.html')


def recommend(request):
    return render(request, 'recommend.html')


def option(request):
    return render(request, 'option.html')
