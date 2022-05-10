from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from blog.forms import FiltroPostForm, AddComentarioForm
from blog.models import Post
from blog.utils import paginar_registros


def listar_posts(request):
    form = FiltroPostForm(request.GET or None)
    queryset = Post.objects.all()
    if request.GET:
        if form.is_valid():
            queryset = form.filtrar().order_by('-criado_em')
    posts = paginar_registros(request, queryset, 6)
    return render(request, 'listar_posts.html', locals())


def visualizar_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        messages.error(request, 'Post não existe.')
        return redirect('blog:listar_posts')
    comentarios = post.comentarios.all().order_by('-criado_em')

    form = AddComentarioForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
    return render(request, 'visualizar_post.html', locals())

