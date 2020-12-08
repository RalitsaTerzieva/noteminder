from django.urls import path
from notes.views import NotesListView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('list/', NotesListView.as_view(), name='list_notes'),
    path('add/', NoteCreateView.as_view(), name='note_add'),
    path('<pk>/update/', NoteUpdateView.as_view(), name='note_update'),
    path('<pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),

]