from django.contrib import admin
from .models import Note

# Admin page par Note model ko register kiya hai
# Taake instructor asani se notes dekh sake
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at', 'color')
    list_filter = ('owner', 'created_at')
    search_fields = ('title', 'content')
