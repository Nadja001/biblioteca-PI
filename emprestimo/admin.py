from django.contrib import admin

# Register your models here.
from emprestimo.models import categoria, livro, avaliacao, usuario, emprestimo

admin.site.register(categoria)
admin.site.register(livro)
admin.site.register(avaliacao)
admin.site.register(usuario)
admin.site.register(emprestimo)