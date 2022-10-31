from django.forms import ModelForm
from .models import Note


class NoteModelForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
