from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post, Comentario
from .forms import ComentarioForm

def lista_posts(request):
    # Busca todos os posts ordenados pela data de publicação (mais recente primeiro)
    posts = Post.objects.all().order_by('-data_publicacao')
    # Configura a paginação (3 posts por página)
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Renderiza o template com os posts paginados
    return render(request, 'blog/lista_posts.html', {'page_obj': page_obj})

def detalhes_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('detalhes_post', pk=post.pk)
    else:
        form = ComentarioForm()
    return render(request, 'blog/detalhes_post.html', {
        'post': post,
        'form': form,
        'comentarios': post.comentarios.filter(aprovado=True).order_by('-data_criacao')
    })