from django.shortcuts import render, redirect
from .forms import SignupForm
from item.models import Category, Item
from django.contrib.auth import logout as auth_logout
from django.urls import reverse
# Create your views here.


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html',{
        'form': form,
    })

def logout(request):
    auth_logout(request)
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })  # Replace 'home' with the URL name of your home page or any other page you want to redirect to after logout.