from django import forms
from .models import userModel

class userform(forms.Form):
  name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  contact = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

choices = (
            ('male','Male'),
            ('female','Female'),
          )

class djangoform(forms.Form):
  name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  # contact = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  # email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
  # address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
  # password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
  # gender = forms.ChoiceField(choices=choices,widget=forms.RadioSelect())
  file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))

class userModelForm(forms.ModelForm):
  class Meta:
    model = userModel
    fields = ["name", "contact", "email"] ## "__all__" --> for all the input fields in the model
    widgets = {
      "name" : forms.TextInput(attrs={'class':'form-control'}),
      "email" : forms.TextInput(attrs={'class':'form-control'}),
      "contact" : forms.TextInput(attrs={'class':'form-control'}),
    }