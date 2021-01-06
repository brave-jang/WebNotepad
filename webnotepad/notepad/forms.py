from django import forms
from .models import Notepad


class NotepadForm(forms.ModelForm):
    class Meta:
        model = Notepad
        fields = ['title', 'content']
        labels = {
            '제목' : 'title',
            '내용' : 'content'
        }