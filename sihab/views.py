from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from .models import *
from . forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.db import models
from django.contrib.auth.decorators import login_required,user_passes_test

def sihab(request):
    class eob():
        def __init__(self,svg, category, features,price):
            self.svg = svg
            self.category = category
            self.features = features
            self.price = price
    e = [ eob('scooter', 'Free', [1, 2, 3, 4],'0.00'),
        eob('shipped', 'Basic', [1, 2, 3, 4, 5],'9.99'),
        eob('startup', 'Premium', [1, 2, 3, 4, 5, 6],'99.9')]
    template = loader.get_template('index.html')
    context = {
        'e':e,
    }
    return HttpResponse(template.render(context, request))