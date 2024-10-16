from django import forms
from .models import ForumPost,Comment

class ForumForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['titulo','text']

    def __init__(self, *args, **kwargs):
        super(ForumForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].required = False  # Set title as not required
        self.fields['text'].required = False
   
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['conteudo']