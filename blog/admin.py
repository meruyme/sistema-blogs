from django.contrib import admin

from blog.forms import AddPostAdmin
from blog.models import Post, Comentario

from django.contrib.auth import get_user_model

User = get_user_model()


class PostAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            kwargs['form'] = AddPostAdmin
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.autor = request.user
        super(PostAdmin, self).save_model(request, obj, form, change)


admin.site.site_header = 'Administração do blog'
admin.site.site_title = 'Administração do blog'

admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(Comentario)
