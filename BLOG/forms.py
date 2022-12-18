from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="imagen")

class comentarioF(forms.Form):
    campo=forms.TextInput()
    date_created = models.DateTimeField(default=timezone.now)
    imagen=forms.ImageField(label="imagen")