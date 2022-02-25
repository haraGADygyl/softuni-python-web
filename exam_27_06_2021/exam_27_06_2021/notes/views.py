from django.shortcuts import render, redirect

# Create your views here.
from exam_27_06_2021.notes.forms import CreateProfileForm, CreateNotesForm, EditNotesForm, DeleteNotesForm
from exam_27_06_2021.notes.models import Profile, Note


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    notes = Note.objects.all()

    context = {
        'profile': profile,
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)


def create_note(request):
    if request.method == 'POST':
        form = CreateNotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateNotesForm()

    context = {
        'form': form,
        'hide_note_link': True,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditNotesForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteNotesForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteNotesForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-details.html', context)


def show_profile(request):
    profile = get_profile()
    total_notes = len(Note.objects.all())

    context = {
        'profile': profile,
        'total_notes': total_notes
    }

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }

    return render(request, 'home-no-profile.html', context)


def delete_profile(request, pk):
    Note.objects.all().delete()
    Profile.objects.get(pk=pk).delete()
    return redirect('show index')
