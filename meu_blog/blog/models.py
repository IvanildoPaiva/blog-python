# from django.utils import timezone
# from django.db import models

# class Post(models.Model):
#     titulo = models.CharField(max_length=200)
#     conteudo = models.TextField()
#     imagem = models.ImageField(upload_to='img_blog/', blank=True, null=True)
#     data_publicacao = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.titulo
    
# class Comentario(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios') # Faz um relacionamento com o Post
#     nome = models.CharField(max_length=100)# nome de quem comentou
#     email = models.EmailField() #Email de quem fez o comentário
#     conteudo = models.TextField() # Conteúdo do comentário, o comentário em si
#     data_criacao = models.DateTimeField(default=timezone.now)# Data da criação do comentário
#     aprovado = models.BooleanField(default=False) # agurada a aprovação do comentário ou não
    
#     def __str__(self):
#         return f'Comentado por {self.nome} em {self.post.titulo}'
        


from django.db import models
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='posts/', blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')  # Relacionamento com Post
    nome = models.CharField(max_length=100)  # Nome do autor do comentário
    email = models.EmailField()  # Email do autor (opcional)
    conteudo = models.TextField()  # Conteúdo do comentário
    data_criacao = models.DateTimeField(default=timezone.now)  # Data de criação do comentário
    aprovado = models.BooleanField(default=False)  # Para moderar comentários

    def __str__(self):
        return f'Comentário por {self.nome} em {self.post.titulo}'