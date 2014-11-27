from django.shortcuts import render
import re
from urlparse import urlparse
import json
from StringIO import StringIO
import gzip
from models import tokens
import urllib
from django.shortcuts import redirect
import httplib
from django.shortcuts import HttpResponse
# Create your views here.

headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/json"}

def home(request):
    if get_token(1) != "FAIL":
        return redirect("/get_content")
    return redirect('https://stackexchange.com/oauth?client_id=3746&redirect_uri=http://lab1.rsoi:8000/login&scope=private_info')

def login(request):
    try:
        code = request.GET["code"]
    except:
        return HttpResponse("ERROR!")
    params = urllib.urlencode({'client_id': 3746, 'client_secret': 'PQT6Ln6C8Nm5K2VajkN8rg((',
                               'redirect_uri': 'http://lab1.rsoi:8000/login' ,'code':code})
    conn = httplib.HTTPSConnection("stackexchange.com",443)
    conn.request("POST","/oauth/access_token", params , headers)
    response = conn.getresponse()
    data = response.read()
    i = data.find('=')
    j = data.find('&')
    token = data[i+1:j]
    print "Token = " + token
    objs = tokens.objects.all().filter(user_id=1)
    if len(objs) == 0:
        token_obj = tokens(token=token, user_id=1)
        token_obj.save()
    else:
        objs[0].token=token
        objs[0].save()
    return redirect("/get_content")


def get_token(user_id):
    token_obj = tokens.objects.all().filter(user_id=user_id)
    if len(token_obj) == 0:
        return "FAIL"
    else:
        return token_obj[0].token


def get_content(request):

    token = get_token(1)

    if token == "FAIL":
        return redirect("/")

    conn = httplib.HTTPSConnection("api.stackexchange.com",443)
    params = urllib.urlencode({'order': 'desc', 'sort': 'reputation', 'site': 'stackoverflow',
                               'access_token': token, 'key': 'hrGx5YBDKbWAjv*IglhhgA(('})
    conn.request("GET", "/2.2/me", params, headers)
    response = conn.getresponse()

    buf = StringIO(response.read())
    f = gzip.GzipFile(fileobj=buf)
    data = f.read()
    dict = json.loads(data)
    if dict.get("error_id") != None:
        return redirect('https://stackexchange.com/oauth?client_id=3746&redirect_uri=http://lab1.rsoi:8000/login&scope=private_info')

    return HttpResponse(data)