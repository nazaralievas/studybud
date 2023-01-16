from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['topic', 'name', 'description']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']