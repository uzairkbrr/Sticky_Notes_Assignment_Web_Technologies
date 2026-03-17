from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Yahan sab notes list hongi
    path('notes/', views.note_list, name='note_list'),
    # Naya note banane ka url
    path('notes/new/', views.note_create, name='note_create'),
    # Note edit karne ka rasta
    path('notes/<int:id>/edit/', views.note_edit, name='note_edit'),
    # Note delete karne ka url
    path('notes/<int:id>/delete/', views.note_delete, name='note_delete'),
    
    # Registration ka url
    path('register/', views.register_view, name='register'),
    
    # Built-in Login aur Logout views
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
