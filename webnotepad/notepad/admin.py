from django.contrib import admin
from .models import Notepad

# Register your models here.
class NotepadAdmin(admin.ModelAdmin):
    list_display = ('title', 'registered_dttm')

admin.site.register(Notepad, NotepadAdmin)