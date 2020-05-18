from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse

from .models import Note


def notes(request):
    try:
        notes_list = Note.objects.order_by('-note_last_updated_time')
        return render(request, 'notes/notes.html', {'notes_list': notes_list})
    except Note.DoesNotExist:
        raise Http404('Es gibt keine Notiz mit dieser Nummer')

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
