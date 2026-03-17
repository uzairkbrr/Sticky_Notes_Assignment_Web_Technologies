from django.apps import AppConfig

class NotesConfig(AppConfig):
    # Default database field ID ke liye set kiya
    default_auto_field = 'django.db.models.BigAutoField'
    # App ka naam notes hai
    name = 'notes'
