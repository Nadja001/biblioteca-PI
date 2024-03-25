from django.db import models

# Create your models here.
class categoria(models.Model):
    nome = models.CharField (max_length=50)

class livro(models.Model):
    titulo = models.CharField (max_length=50)
    autor = models.CharField (max_length=50)
    ano = models.IntegerField ()
    genero = models.CharField (max_length=50)
    categorias = models.ManyToManyField(categoria)

class usuario(models.Model):
    nome  = models.CharField (max_length=100)
    email = models.EmailField ()
    senha = models.CharField (max_length=50)

class avaliacao(models.Model):
    pontuacao = models.IntegerField()
    comentario = models.CharField(max_length=200)
    livro = models.ForeignKey (livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey (usuario, on_delete=models.CASCADE)

class emprestimo(models.Model):
    data_inicio = models.DateField
    data_fim = models.DateField
    livros = models.ForeignKey(livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)