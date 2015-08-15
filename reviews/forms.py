from django import forms
from reviews.models import Vote

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['voter', 'business']