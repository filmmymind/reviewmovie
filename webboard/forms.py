from django.forms import ModelForm
from django import forms
from .models import boardpost,Boardcomment

class PostForm(ModelForm):
    Title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "หัวข้อเรื่อง",

                   })
    )
    Tag = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder":"คำถาม,ภาพยนตร์"
        })
    )

    class Meta:
        model = boardpost
        fields = ['Title','Tag','Content']



class CommentForm(ModelForm):
    class Meta:
        model = Boardcomment
        fields = ['comment']
