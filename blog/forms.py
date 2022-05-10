from django import forms

from blog.models import Post


class AddPostAdmin(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']
