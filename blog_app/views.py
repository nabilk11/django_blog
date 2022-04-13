from django.shortcuts import render

# Create your views here.

# Basic Home View
def home(request):
    return render(request, 'home.html', {})