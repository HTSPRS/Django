from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def exercise1(request):
    template = loader.get_template('exercise1.html')

    context = {'result': 'HCH'}
    return HttpResponse(template.render(context,request))

def exercise2(request):
    if request.method == 'POST':
        name = request.POST['nm']
        text = request.POST['cnt']
        context = {'name': name, 'text': text}
    else:
        context = None
    return render(request, 'exercise2.html', context)
# Create your views here.
