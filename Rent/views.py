from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Ad
from .forms import AdForm
from django.shortcuts import redirect


def post_list(request):
    ads = Ad.objects.all()
    return render(request, 'Rent/post_list.html', {'ads': ads})


def post_new(request):
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.published_date = timezone.now()
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
    if request.method == "POST":
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.published_date = timezone.now()
            ad.save()
            return redirect('post_detail', pk=ad.pk)
    else:
        form = AdForm(instance=ad)
    return render(request, 'Rent/post_edit.html', {'form': form})
