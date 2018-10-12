from django import forms
from .models import *

class RegisterTeamForm(forms.ModelForm):
    class Meta:
        model = RegisterTeam
        fields = ('Team_Name', 'Player1_Name', 'Player2_Name',)

class RegisterGameForm(forms.ModelForm):
    class Meta:
        model = RegisterGame
        fields = ('team1', 'team1_score', 'team2', 'team2_score',)
