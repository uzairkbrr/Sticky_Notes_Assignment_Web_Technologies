from django.db import models
from django.contrib.auth.models import User

# ye model sticky note ko represent karta hai
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Note ka rang save karne ke liye, default halke peele rang (yellow) ka hai
    color = models.CharField(max_length=7, default='#FFFF99')
    
    # pinned notes ke liye field
    is_pinned = models.BooleanField(default=False)
    
    # note kab bana aur kab edit hua iska record
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Har note ka ek owner (user) hoga jo ise banayega
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Admin panel mein title dikhane ke liye
        return self.title

    @property
    def text_color(self):
        # Hex se RGB extract karke luminance check karein 
        # (Dark background pe light text aur light background pe dark text)
        hex_color = self.color.lstrip('#')
        if len(hex_color) == 6:
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
            # Agar color light hai to dark color dijiye '#1f2937', warna white '#ffffff'
            return '#1f2937' if luminance > 0.5 else '#ffffff'
        return '#1f2937'
