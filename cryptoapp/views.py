import requests, json
from django.shortcuts import render, get_object_or_404,redirect
from cryptoapp.models import Blockchain,Token,Tutorial,Dict,Basic
from .forms import BlockchainForm,TokenForm
from django.http import HttpResponse





def index(request):
    
    return render(request, 'cryptoapp/index.html')



def main(request):
    coingeckoapi = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'cryptoapp/main.html',{ 'api':api,'coingeckoapi':coingeckoapi})

        # dodac do return request coingeckoapi:coingeckoapi
    


def form(request):
    return render(request, 'cryptoapp/form.html')

def show(request):
    error = False
    if request.POST:
        if 'first_name' in request.POST:
            first_name = request.POST.get('first_name')
        else:
            error = True
    else:
        error = True
    if not error:
        return render(request, 'cryptoapp/show.html', {"first_name": first_name})
    else:
        # albo np. komunikat o błędzie
        return render(request, 'cryptoapp/form.html')

def blockchains(request):
    all_blockchains = Blockchain.objects.all()
    return render(request, 'cryptoapp/blockchain/index.html',
                {'action': 'Lista Blockchainów', 'all_blockchains': all_blockchains})

def tutorials(request):
    all_tutorials = Tutorial.objects.all()
    return render(request, 'cryptoapp/tutorial/index.html',
                {'action': 'Lista tutoriali', 'all_tutorials': all_tutorials})

def dicts(request):
    all_dicts = Dict.objects.all()
    return render(request, 'cryptoapp/dict/index.html',
                {'action': 'Słownik', 'all_dicts': all_dicts})

def dicts_szczegoly(request, dict_id):
    action = 'Dict o ID = ' + str(dict_id)
    dict = get_object_or_404(Dict, pk=dict_id)
    return render(request, 'cryptoapp/dict/details.html', locals())

def tutorials_szczegoly(request, tutorial_id):
    action = 'Tutorial o ID = ' + str(tutorial_id)
    tutorial = get_object_or_404(Tutorial, pk=tutorial_id)
    return render(request, 'cryptoapp/tutorial/details.html', locals())

def blockchain_nowy(request):
    action = 'Nowy blockchain'
    if(request.method == 'POST'):
        form = BlockchainForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('blockchain')
    else:
        form = BlockchainForm()
    return render(request, 'cryptoapp/blockchain/new.html', locals())

def blockchains_szczegoly(request, blockchain_id):
    action = 'Blockchain o ID = ' + str(blockchain_id)
    blockchain = get_object_or_404(Blockchain, pk=blockchain_id)
    return render(request, 'cryptoapp/blockchain/details.html', locals())

def tokens(request):
    all_tokens = Token.objects.all()
    return render(request, 'cryptoapp/token/index.html',
                {'action': 'Lista Kryptowalut', 'all_tokens': all_tokens})

def cryptocurrencies(request):
    coingeckoapi = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    return render(request, 'cryptoapp/cryptocurrencies.html',{'coingeckoapi':coingeckoapi})

def token_nowy(request):
    action = 'Nowy token'
    if(request.method == 'POST'):
        form = TokenForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('token')
    else:
        form = TokenForm()
    return render(request, 'cryptoapp/token/new.html', locals())                

def tokens_szczegoly(request, token_id):
    action = 'Token o ID = ' + str(token_id)
    token = get_object_or_404(Token, pk=token_id)
    return render(request, 'cryptoapp/token/details.html', locals())               

def basics(request):
    all_basics = Basic.objects.all()
    return render(request, 'cryptoapp/basic/index.html',
                {'action': 'Podstawowa wiedza', 'all_basics': all_basics})

def basics_szczegoly(request, basic_id):
    action = 'Basic o ID = ' + str(basic_id)
    basic = get_object_or_404(Basic, pk=basic_id)
    return render(request, 'cryptoapp/basic/details.html', locals())

def news(request):
    import requests,json
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'cryptoapp/news.html', {"api": api})