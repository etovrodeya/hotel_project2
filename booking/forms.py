from django import forms
from booking.models import Booking
from django.forms.extras.widgets import SelectDateWidget

class BookingCreateForm(forms.ModelForm):
       
    class Meta:
        model = Booking
        fields  = ['style','comment','child','number_peoples','s_date','e_date']
        widgets = {
            'user': forms.HiddenInput(),
            's_date': SelectDateWidget(attrs={'class':'form-control'}),
            'e_date': SelectDateWidget(attrs={'class':'form-control'}),
            'style': forms.Select(attrs={'class':'form-control'}),
            'comment': forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'child': forms.TextInput(attrs={'class':'form-control'}),
            'number_peoples': forms.TextInput(attrs={'class':'form-control'}),
            }

class BookingEditForm(forms.ModelForm):
       
    class Meta:
        model = Booking
        fields  = ['style','comment','child','number_peoples','s_date','e_date',
                   'room','status','price']
        widgets = {
            'user': forms.HiddenInput(),
            's_date': SelectDateWidget(attrs={'class':'form-control'}),
            'e_date': SelectDateWidget(attrs={'class':'form-control'}),
            'style': forms.Select(attrs={'class':'form-control'}),
            'comment': forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'child': forms.TextInput(attrs={'class':'form-control'}),
            'number_peoples': forms.TextInput(attrs={'class':'form-control'}),
            'room': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            
            }
