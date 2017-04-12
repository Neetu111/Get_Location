import json as js
from django.shortcuts import render, redirect
from .forms import *
import requests

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        post = form.save(commit=False)
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
            state = request.POST.get('state')
            city = request.POST.get('city')
            address = request.POST.get('address')
            Pincodes = pincode(state, city, address)
            return render(request,'login/pin.html',{'Pincodes':Pincodes})
        else:
            form = detailForm()
            return render(request, 'login/further_info.html', {'form': form})

def pincode(state, city, address):
    jsonList = []
    Pincodes = {}
    req = requests.get(('https://www.whizapi.com/api/v2/util/ui/in/indian-postal-codes?project-app-key=k6oyhd6vvi3sdh5m8w2rc7k5&search=') + state)
    jsonList.append(js.loads(req.content))
    for data in jsonList[0]['Data']:
        if (data['State']==state.upper() and data['City']==city and data['Address']==(address+" ")):
            Pincodes['Address'] =data['Address']
            Pincodes['Pincode'] = data['Pincode']
            Pincodes['City'] = data['City']
            Pincodes['State'] = data['State']
            return (Pincodes)