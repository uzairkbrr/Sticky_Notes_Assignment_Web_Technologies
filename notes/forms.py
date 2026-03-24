from django import forms
from .models import Note

# ye form naya note banane aur edit karne ke liye hai
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        # Sirf title, content, color aur is_pinned user se lene hain
        fields = ['title', 'content', 'color', 'is_pinned']
        
        # HTML form elements ko style karne ke liye widgets add kiye hain
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note ka title...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Yahan note likhein...', 'rows': 5}),
            'color': forms.TextInput(attrs={'type': 'color', 'class': 'color-picker'}),
            'is_pinned': forms.CheckboxInput(attrs={'class': 'pin-checkbox'}),
        }
