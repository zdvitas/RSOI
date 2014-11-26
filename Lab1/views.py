from django.shortcuts import render
import re
from urlparse import urlparse
import urllib
from django.shortcuts import redirect
import httplib
from django.shortcuts import HttpResponse
# Create your views here.

def home(request):
    return redirect('https://stackexchange.com/oauth?client_id=3746&redirect_uri=http://lab1.rsoi:8000/login&scope=private_info')

def login(request):
    try:
        code = request.GET["code"]
    except:
        return HttpResponse("ERROR!")
    params = urllib.urlencode({'client_id': 3746, 'client_secret': 'PQT6Ln6C8Nm5K2VajkN8rg((', 'redirect_uri': 'http://lab1.rsoi:8000/login' ,'code':code})
    conn = httplib.HTTPSConnection("stackexchange.com",443)
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/json"}
    conn.request("POST","/oauth/access_token", params , headers)
    response = conn.getresponse()
    data = response.read()
    i = data.find('=')
    j = data.find('&')
    token = data[i+1:j]

    conn = httplib.HTTPSConnection("api.stackexchange.com",443)
    params = urllib.urlencode({'order': 'asc', 'sort': 'name((', 'site': 'stackoverflow' ,'access_token': token})
    conn.request("POST","/2.2/me", params , headers)
    response = conn.getresponse()
    data = response.read()
    return HttpResponse(data)