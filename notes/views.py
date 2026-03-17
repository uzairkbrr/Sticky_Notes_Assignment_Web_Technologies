from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Note
from .forms import NoteForm

# yeh view naye user ko register karne ke liye hai
def register_view(request):
    # agar user pehle se login hai to page access nahi karne do, notes par bhej do
    if request.user.is_authenticated:
        return redirect('note_list')
        
    if request.method == 'POST':
        # form ka data get karo
        form = UserCreationForm(request.POST)
        # agar form valid ho to usko database main load karo
        if form.is_valid():
            form.save() # naya user database mein save karo
            messages.success(request, 'Account ban gaya hai. Ab login karein.')
            return redirect('login') # fir login page par redirect kar do
    else:
        # pehli baar bas empty form dena hai
        form = UserCreationForm()
        
    # register.html template render karo
    return render(request, 'register.html', {'form': form})

# yahan par user ki notes fetch ho rahi hain
@login_required # login hona zaroori hai
def note_list(request):
    # Database se current user ki notes fetch karein (Security Rule)
    notes = Note.objects.filter(owner=request.user).order_by('-created_at')
    
    # note_list template pe bhejo
    return render(request, 'note_list.html', {'notes': notes})

# yeh view naya note banata hai
@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        # agar form valid ho to note save karo
        if form.is_valid():
            note = form.save(commit=False)
            # Yahan owner user ko assign kiya hai
            note.owner = request.user
            note.save() # ab db me asalki save maro
            messages.success(request, 'Note ban gaya!')
            return redirect('note_list')
    else:
        # User ko khali form dikhao
        form = NoteForm()
        
    return render(request, 'note_form.html', {'form': form, 'edit_mode': False})

# yeh view note edit karta hai
@login_required
def note_edit(request, id):
    # Agar ye user ka nahi hai, to 404 page error ayega (Security Rule)
    note = get_object_or_404(Note, id=id, owner=request.user)
    
    if request.method == 'POST':
        # naya data note object per daalo
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note update ho gaya!')
            return redirect('note_list')
    else:
        # taake pehle wala data forms main dikhe
        form = NoteForm(instance=note)
        
    return render(request, 'note_form.html', {'form': form, 'edit_mode': True})

# yeh view note delete karta hai
@login_required
def note_delete(request, id):
    # Confirmation ka wait karo, aur find karo same owner ko 
    note = get_object_or_404(Note, id=id, owner=request.user)
    
    if request.method == 'POST':
        # db se delete karo
        note.delete()
        messages.success(request, 'Note delete ho gaya!')
        return redirect('note_list')
        
    # Sirf delete confirmation page open karein
    return render(request, 'note_confirm_delete.html', {'note': note})
