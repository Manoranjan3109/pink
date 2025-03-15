from django.shortcuts import render

def home(request):
    return render(request, "clgapp/home.html")

def about(request):
    return render(request, "clgapp/about.html")

def cse(request):
    return render(request, "clgapp/cse.html")  # Ensure this template exists

def ece(request):
    return render(request, "clgapp/ece.html")

def mech(request):
    return render(request, "clgapp/mech.html")

def civil(request):
    return render(request, "clgapp/civil.html")

def contact(request):
    return render(request, "clgapp/contact.html")
