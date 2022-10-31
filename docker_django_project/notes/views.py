from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import *

# Create your views here.


class Index(View):
    def get(self, request):
        notes = Note.objects.all()
        form = NoteModelForm()
        return render(request, 'notes/index.html', {'notes': notes, 'form': form})

    def post(self, request):
        form = NoteModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('notes:notes')


class Delete(View):
    def get(self, request, pk):
        note = Note.objects.get(pk=pk)
        note.delete()
        return redirect('notes:notes')


class Update(View):
    def get(self, request, pk):
        note = Note.objects.get(pk=pk)
        notes = Note.objects.all()
        form = NoteModelForm(instance=note)
        update_flag = True
        return render(request, 'notes/index.html', {'form': form, 'notes': notes, 'update_flag': update_flag, 'note': note})

    def post(self, request, pk):
        note = Note.objects.get(pk=pk)
        print(pk)
        form = NoteModelForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
        return redirect('notes:notes')
