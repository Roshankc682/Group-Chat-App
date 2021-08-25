from django import forms
from .models import UserData
  
class UserDataForm(forms.ModelForm):
    username = forms.CharField(label='')
    password = forms.CharField(widget=forms.PasswordInput,label='')
    def __init__(self, *args, **kwargs):
        super(UserDataForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Type username'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Type password'

        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'form-control'
        #     visible.field.widget.attrs['placeholder'] = 'Type username'

    class Meta:
        model = UserData
        fields = "__all__"

  
class UserDataCheck(forms.ModelForm):
    username = forms.CharField(label='')
    password = forms.CharField(widget=forms.PasswordInput,label='')
    def __init__(self, *args, **kwargs):
        super(UserDataCheck, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Type username'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Type password'

    class Meta:
        model = UserData
        fields = "__all__"

