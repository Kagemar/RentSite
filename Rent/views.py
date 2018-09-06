from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Ad
from .forms import AdForm
from django.shortcuts import redirect

import json
import requests



def post_list(request):
    ads = Ad.objects.all()
    return render(request, 'Rent/post_list.html', {'ads': ads})


def post_new(request):
    api_key = "AIzaSyBywMAwBbcFPq-nDOYm_WRGqkCwS53fTVo"
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.published_date = timezone.now()
            address = ad.localization
            api_response = requests.get(
                'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
            api_response_dict = api_response.json()
            ad.latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            ad.longitude = api_response_dict['results'][0]['geometry']['location']['lng']
            ad.save()
            return redirect('post_detail', pk=ad.pk)
    else:
        form = AdForm()
    return render(request, 'Rent/post_edit.html', {'form': form})


def post_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    return render(request, 'Rent/post_detail.html', {'ad': ad})


def post_edit(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    api_key = "AIzaSyBywMAwBbcFPq-nDOYm_WRGqkCwS53fTVo"

    if request.method == "POST":
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.published_date = timezone.now()
            address = ad.localization
            api_response = requests.get(
                'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
            api_response_dict = api_response.json()
            ad.latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            ad.longitude = api_response_dict['results'][0]['geometry']['location']['lng']
            ad.save()
            return redirect('post_detail', pk=ad.pk)
    else:
        form = AdForm(instance=ad)
    return render(request, 'Rent/post_edit.html', {'form': form})

def localization_change(address, pk):
    ad = get_object_or_404(Ad, pk=pk)
    api_key = "AIzaSyBywMAwBbcFPq-nDOYm_WRGqkCwS53fTVo"
    address = ad.localization
    api_response = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
    api_response_dict = api_response.json()
    ad.latitude = api_response_dict['results'][0]['geometry']['location']['lat']
    ad.longitude = api_response_dict['results'][0]['geometry']['location']['lng']

