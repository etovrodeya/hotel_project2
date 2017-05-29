from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from myprofile.models import User,UserAvatar
from django.forms.extras.widgets import SelectDateWidget

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'type':'password',
            'placeholder':'Enter password',
            }),
    )
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'type':'password',
            'placeholder':'Enter password',
            }),
    )
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароль и подтверждение не совпадают')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['email',]
        widgets = {
            'email': forms.TextInput(attrs={'class':'form-control', 'type':'email', 'placeholder':'Enter email'}),
            }
        
class UserChangeForm(forms.ModelForm):

    '''
    Форма для обновления данных пользователей. Нужна только для того, чтобы не
    видеть постоянных ошибок "Не заполнено поле password" при обновлении данных
    пользователя.
    '''
    password = ReadOnlyPasswordHashField(
        widget=forms.PasswordInput,
        required=False
    )

    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['email', ]

class ProfileForm(forms.ModelForm):
  class Meta:
    model = get_user_model()
    fields = ['email','firstname','surname','patronymic','category',
              'balance','country','city','phone',
              'index','street','home','region','office',
              'birthday']
    widgets = {
        'email': forms.TextInput(attrs={'class':'form-control', 'type':'email', 'placeholder':'Enter email'}),
        'firstname': forms.TextInput(attrs={'class':'form-control'}),
        'surname': forms.TextInput(attrs={'class':'form-control'}),
        'patronymic': forms.TextInput(attrs={'class':'form-control'}),
        'category': forms.Select(attrs={'class':'form-control'}),
        'balance': forms.TextInput(attrs={'class':'form-control'}),
        'country': forms.TextInput(attrs={'class':'form-control'}),
        'city': forms.TextInput(attrs={'class':'form-control'}),
        'phone': forms.TextInput(attrs={'class':'form-control'}),
        'index': forms.TextInput(attrs={'class':'form-control'}),
        'street': forms.TextInput(attrs={'class':'form-control'}),
        'home': forms.TextInput(attrs={'class':'form-control'}),
        'region': forms.TextInput(attrs={'class':'form-control'}),
        'office': forms.TextInput(attrs={'class':'form-control'}),
        'birthday': SelectDateWidget(years=range(1901, 2017),attrs={'class':'form-control'}),

        }

class UserAvatarForm(forms.ModelForm):
    class Meta:
        model= UserAvatar
        fields=['avatar']
        widgets = {
            'user': forms.HiddenInput(),
            }
