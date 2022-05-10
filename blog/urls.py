from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/', views.listar_posts, name='listar_posts'),
    path('posts/<int:post_id>/', views.visualizar_post, name='visualizar_post')
]
