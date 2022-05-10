from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(email=self.normalize_email(email))
        user.password = make_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_active = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email", unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False, verbose_name="Administrador")

    USERNAME_FIELD = "email"

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Post(models.Model):
    titulo = models.CharField(max_length=300, verbose_name='Título')
    conteudo = models.TextField(verbose_name='Conteúdo')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    criado_em = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    nome_usuario = models.CharField(max_length=255, verbose_name='Nome')
    conteudo = models.CharField(max_length=500, verbose_name='Conteúdo')
    criado_em = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"
