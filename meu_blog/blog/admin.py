# from django.contrib import admin
# from .models import Comentario, Post

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('titulo', 'data_publicacao', 'imagem')
#     search_fields = ('titulo',)
    
# @admin.register(Comentario)
# class ComentarioAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'post', 'data_criacao', 'aprovado')
#     list_filter = ('aprovado', 'datra_criacao')
#     actions = ['aprovar_comentarios']

#     def aprovar_comentarios(self,request,queryset):
#         queryset.update(aprovado=True) # mudando o status lá do model que era false para True, exibir o comentário aprovando 
#         aprovar_comentarios.short_description = "Aprovar comentários selecionados" # type: ignore



from django.contrib import admin
from .models import Post, Comentario

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'post', 'data_criacao', 'aprovado')
    list_filter = ('aprovado', 'data_criacao')
    actions = ['aprovar_comentarios']

    def aprovar_comentarios(self, request, queryset):
        queryset.update(aprovado=True)
    aprovar_comentarios.short_description = "Aprovar comentários selecionados"