from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from notes.models import Note


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


@method_decorator(login_required, name='dispatch')
class NotesListView(ListView):
    model = Note
    template_name = 'notes/list_notes.html'

    def get_queryset(self):
        return Note.objects.filter(profile=self.request.user.userprofile)


@method_decorator(login_required, name='dispatch')
class NoteCreateView(CreateView):
    template_name = 'notes/add_note.html'
    model = Note
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('list_notes')

    def form_valid(self, form):
        form.instance.profile = self.request.user.userprofile
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class NoteUpdateView(UpdateView):
    template_name = 'notes/update_note.html'
    model = Note
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('list_notes')


@method_decorator(login_required, name='dispatch')
class NoteDeleteView(DeleteView):
    template_name = 'notes/delete_note.html'
    model = Note
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('list_notes')
