from views import news
import requests
from django.shortcuts import render, get_object_or_404,redirect
from cryptoapp.models import Blockchain,Token,Tutorial,Dict,Basic
from .forms import BlockchainForm,TokenForm
from django.http import HttpResponse

def news(request):
    import requests,json
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'cryptoapp/news.html', {"api": api})



def groupnews(title)