# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from rest_framework.decorators import api_view 
from django.shortcuts import render 

import requests


from . import firebaseconfig

database = firebaseconfig.database()


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
@login_required(login_url="/login/")
def tables(request):
   
    channel_data = database.child('machines') 
    lm = channel_data.get().val()
    channel_data2 = database.child('Bottles') 
    lmm = channel_data2.get().val() 
    url = "http://127.0.0.1:8888/restapi/model1/"
    steps = {"steps" : 365}
    x = requests.post(url, json = steps)
    print(x)
    url2 = "http://127.0.0.1:8888/restapi/model2/"
   
    y = requests.post(url2, json = steps)


    return render(request, "home/tables.html" , {"listmachine":lm.items() , "listbottle" : lmm.items() , "step":x.json()["result"] , "sarimax":y.text})
    
    
