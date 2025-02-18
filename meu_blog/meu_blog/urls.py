from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('blog.urls')),
]

# Adiciona a rota para servir arquivos de mídia durante o desenvolvimento
# 🔹 Adiciona suporte para arquivos estáticos e de mídia durante o desenvolvimento
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # ADICIONE ESTA LINHA
    