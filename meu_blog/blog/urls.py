from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),  # Referência à função lista_posts
    path('post/<int:pk>/', views.detalhes_post, name='detalhes_post'),
]