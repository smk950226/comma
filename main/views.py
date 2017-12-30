from django.shortcuts import render, redirect
from .models import ActPhoto
from .forms import ActPhotoForm

def main(request):
    photos = ActPhoto.objects.all().order_by('?')[:8]
    return render(request, 'main/main.html', {
        'photos': photos,
    })

def act_photo(request):
    photos = ActPhoto.objects.all()
    return render(request, 'main/act_photo.html', {
        'photos': photos,
    })

def act_photo_add(request):
    if request.method == 'POST':
        form = ActPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            mentor = form.save()
            return redirect('main:act_photo')
    else:
        form = ActPhotoForm()
    return render(request, 'main/act_photo_add.html', {
        'form': form,
    })