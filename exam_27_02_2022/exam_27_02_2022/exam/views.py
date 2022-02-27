from django.shortcuts import render, redirect

# Create your views here.
from exam_27_02_2022.exam.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, \
    DeleteAlbumForm
from exam_27_02_2022.exam.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    albums = Album.objects.all()

    context = {
        'profile': profile,
        'albums': albums,
    }
    return render(request, 'home-with-profile.html', context)


def create_album(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateAlbumForm()

    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'delete-album.html', context)


def create_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show index")
    else:
        form = CreateProfileForm()

    context = {
        "form": form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def details_profile(request):
    profile = get_profile()

    albums_count = len(Album.objects.all())

    context = {
        'profile': profile,
        'albums_count': albums_count

    }
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    Profile.objects.first().delete()
    Album.objects.all().delete()

    return redirect('show index')
