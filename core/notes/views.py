from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse

from .models import Note


def notes(request, **kwargs):
    notes_list = Note.objects.order_by('-note_last_updated_time')
    return render(request, 'notes/notes.html', {"notes_list": notes_list})

        # output = '.\n '.join([n.text for n in latest_notes_list])


def note_details(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/note_details.html', {'note': note})


def note_create(request):
    note = Note(note_title=request.POST['note_title'],
                note_content=request.POST['note_content'],
                note_last_updated_time=timezone.now())
    note.save()
    return HttpResponseRedirect(reverse('notes:notes'))


def note_modify(request):
    note = Note.objects.get(pk=request.POST["note_id"])
    note.note_title = request.POST["note_title"]
    note.note_content = request.POST["note_content"]
    note.save()
    return HttpResponseRedirect(reverse('notes:notes'))


def note_delete(request):
    Note.objects.get(pk=request.POST["note_id"]).delete()
    return HttpResponseRedirect(reverse('notes:notes'))
