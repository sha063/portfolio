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
    template = loader.get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))