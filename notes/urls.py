from django.urls import path
from notes.views import NotesListView, add_note

urlpatterns = [
    path('list/', NotesListView.as_view(), name='list_notes'),
    path('add/', add_note, name='add_notes'),
]