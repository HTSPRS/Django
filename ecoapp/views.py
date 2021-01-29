from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
import random

def index(request):
    return render(request, 'index.html')
# Create your views here.
