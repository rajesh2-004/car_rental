from django.shortcuts import render 
from django.http import HttpResponse



def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def about(request):
    return render(request,"about.html")
def main(request):
    return render(request,"main.html")
def book(request):
    return render(request,"book.html")
def sample(request):
    return render(request,"sample.html")
def register(request):
    return render(request,"register.html")
def cars(request):
    return render(request,"cars.html")
def contact(request):
    return render(request,"contact.html")