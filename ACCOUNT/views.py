from django.shortcuts import render
from . models import *
from CRUD_APP.models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

# home page
def index(request):
    return render(request, 'index.html')