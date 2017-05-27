from django import forms
from comments.models import Comment

class CommentReviewForm(forms.ModelForm):
       
    class Meta:
        model = Comment
        fields = ['title','comment']
        widgets = {
            'user': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'comment': forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            }
