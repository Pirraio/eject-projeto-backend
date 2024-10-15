from django import forms
from .models import ForumPost,Comment

class ForumForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['titulo','text']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['conteudo']
        
    