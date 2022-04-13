import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Tutorial, Testimonial, Recommended, BuyCoins, Coin
from .forms import BuyCoinsForm


# Fetching API response and rendering API data to index.html file
def index(request):
    apidata = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=cad&order=market_cap_desc&market_chart?vs_currency=cad&days=7&per_page=100&page=1'
        '&sparkline=false').json()
    return render(request, 'index.html', {'apidata': apidata})

# This is used for registration of new users
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form.as_p()}
    return render(request, 'registration/register.html', context)

#This is used for the fetching data from the DB for tutotials page
def tutorial(request):
    data = Tutorial.objects.all()
    return render(request, 'tutorial.html', {'data': data})

#to order coins
def order(request):
    if request.method == 'POST':
        filled_form = BuyCoinsForm(request.POST)
        if filled_form.is_valid():
            note = 'Thank you for your purchase, You bought %s %s and they will be added to your wallet %s within 24 ' \
                   'hours after further validation' % (
                       filled_form.cleaned_data['qty'],
                       filled_form.cleaned_data['name'],
                       filled_form.cleaned_data['address'])

            filled_form.save()
            newform = BuyCoinsForm()
            return render(request, 'order.html', {'buycoinsform': newform, 'note': note})

    else:
        form = BuyCoinsForm()
        return render(request, 'order.html', {'buycoinsform': form})

#for the recommendation page
def recommendation(request):
    return render(request, 'recommendations.html')

#for the testimonial page
def testimonial(request):
    data = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'data': data})

def aboutus(request):
    return render(request, 'aboutus.html')
