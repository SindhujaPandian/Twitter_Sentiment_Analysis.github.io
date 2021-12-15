from app.models import userModel
from django import forms

class userForm(forms.ModelForm):
    class Meta:
        model = userModel
        fields = [
            'username', 'keyword'
        ]
        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'keyword':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
        "username": "Enter your name",
        "keyword" : "Enter the Keyword you want to predict"
        }
