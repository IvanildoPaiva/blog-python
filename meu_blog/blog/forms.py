# from django import forms
# from .models import Comentario

# class ComentarioForm(forms.ModelForm):
#     class meta:
#         model = Comentario
#         fields = ('nome', 'email', 'conteudo')
        
        
        
from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nome', 'email', 'conteudo')