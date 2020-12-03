from django.urls import path
from notes.views import list_notes, add_note

urlpatterns = [
    path('list/', list_notes, name='list_notes'),
    path('add/', add_note, name='add_notes'),
]