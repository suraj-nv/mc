from django.shortcuts import render
from django.http import HttpResponse
def home(request):
     return render(request, "accounts/index.html")

# Create your views here.
