from django.shortcuts import render
from django.http import HttpResponse

# Add the following import

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')