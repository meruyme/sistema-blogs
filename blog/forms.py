from django import forms

from blog.models import Post, Comentario


class AddPostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']


class FiltroPostForm(forms.Form):
    titulo = forms.CharField(label='Título', max_length=300, required=False)

    def filtrar(self):
        posts = Post.objects.all()
        titulo = self.cleaned_data.get('titulo')

        if titulo:
            posts = posts.filter(titulo__icontains=titulo)

        return posts


class AddComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome_usuario', 'conteudo']

        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 3})
        }
        help_texts = {
            'conteudo': '0/500 caracteres'
        }

    def __init__(self, post, *args, **kwargs):
        super(AddComentarioForm, self).__init__(*args, **kwargs)
        self.post = post

    def save(self, commit=True):
        comentario = super(AddComentarioForm, self).save(commit=False)
        comentario.post = self.post
        if commit:
            comentario.save()
        return comentario
