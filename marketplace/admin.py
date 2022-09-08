from django.contrib import admin
from .models import AnuncioVenda, AnuncioDoacao

# Register your models here.
admin.site.register(AnuncioVenda)
admin.site.register(AnuncioDoacao)