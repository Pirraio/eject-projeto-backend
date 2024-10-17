from django import forms
from .models import ForumPost,Comment

class ForumForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['titulo','text']
        widgets ={
            'titulo': forms.TextInput(attrs={'placeholder': 'Título do tópico'}),             
            'text' : forms.Textarea(attrs={'placeholder': 'Adicionar um novo tópico'}),
        }

    def __init__(self, *args, **kwargs):
        super(ForumForm, self).__init__(*args, **kwargs)
        #Colocando o titulo e o text como não necessários para a atualização da página
        self.fields['titulo'].required = False  
        self.fields['text'].required = False
   
        self.fields['titulo'].label = ''  # Remove o label de 'titulo'
        self.fields['text'].label = ''    # Remove o label de 'text'
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['conteudo']
        widgets ={
            'conteudo': forms.Textarea(attrs={'placeholder': 'Escreva seu comentario'}), 
        }
        labels = {
            'conteudo': '',
        }