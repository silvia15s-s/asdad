from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def catalog(request):
    return render(request, 'main/catalog.html')

def contact(request):
    return render(request, 'main/contact.html')

def team(request):
    return render(request, 'main/team.html')

def login(request):
    return render(request, 'main/login.html')

def registration(request):
    return render(request, 'main/registration.html')