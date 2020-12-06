from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, UpdateView, ListView

from accounts.models import UserProfile
from notes.models import Note


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class NotesListView(ListView):
    model = Note
    template_name = 'list_notes.html'

    def get_queryset(self):
        return Note.objects.filter(profile=self.request.user.userprofile)


def add_note(request):
    pass
