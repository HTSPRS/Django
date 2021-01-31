from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
import random

def index1(request):
    return render(request, 'index1.html')


# Create your views here.
