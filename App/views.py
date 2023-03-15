from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import requests
import json


# Create your views here.

class DomainChecker(View):

    def get(self, request):
        return render(request, 'App/index.html')

    def post(self, request):
        if request.method == "POST":
            con = True
            url = "https://domain-checker7.p.rapidapi.com/whois"
            domain = request.POST['domain']
            querystring = {"domain": domain}

            headers = {
                "X-RapidAPI-Key": "fe7ac125c5msh94f9c196609b1eep12fb18jsndc6f9e5920c3",
                "X-RapidAPI-Host": "domain-checker7.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            x = json.dumps(response.json())
            data = json.loads(x)
            if response.status_code == 429:
                return HttpResponse('This Service Under Construction')
            if not data['available']:
                con = False

            return render(request, 'App/result.html', {
                'con': con,
                'available': data['available'],
                'created_at': data['created_at'],
                'expires_at': data['expires_at'],
                'tld': data['tld'],
                'registrar': data['registrar'],
                'updated_at': data['updated_at'],
                'valid': data['valid'],
                'domain': domain
            })
