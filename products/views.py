from django.http import HttpResponse
from django.shortcuts import render
from .models import Account,Product

def index(request):
    products=Product.objects.all()
    return render(request,"index.html",{'items':products})

def new(request):
    return HttpResponse(Account("frank",300))


# Create your views here.
