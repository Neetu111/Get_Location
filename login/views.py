from datetime import timezone

from django.core.serializers import json
import json as js
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
import requests

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        post = form.save(commit=False)
        #post.password = form.password
        #post.published_date = timezone.now()
        post.save()
        redirect('other_details', pk=post.pk)
    else:
        form = LoginForm()
        return render(request, 'login/login.html',{'form': form})

def other_details(request):
    form = detailForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            location = request.POST.get('address')

            Pincodes = pincode(location)
            print(Pincodes)
            return render(request,'login/pin.html',{'location':location})
        else:
            form = detailForm()
            return render(request, 'login/further_info.html', {'form': form})

def pincode(location):
    jsonList = []
    Pincodes = {}
    req = requests.get(('https://www.whizapi.com/api/v2/util/ui/in/indian-postal-codes?project-app-key=k6oyhd6vvi3sdh5m8w2rc7k5&search=') + location)
    try:
        jsonList.append(js.loads(req.content))
    except:
        print(req.content)
    for data in jsonList['Data']:
        Pincodes[data['Address']] = data['Pincode']
        # Pincodes[[data['Address']].append(data['Pincode'])
        return Pincodes