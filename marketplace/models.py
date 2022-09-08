from django.db import models
from company.models import Address

# Create your models here.
class Anuncio(models.Model):
    class Meta:
        abstract = True

    STATE_CHOICES = (
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    )

    nome_prod = models.CharField(max_length=100, verbose_name='Nome do Produto', null=False)
    descricao_prod = models.TextField(verbose_name='Descrição do Produto')
    quantidade_prod = models.IntegerField(verbose_name='Quantidade do Produto')
    endereco_prod = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Endereço do Produto')
    img_prod = models.ImageField(upload_to='marketplace', null=True, blank=True, verbose_name='Imagem do Produto')
    estado = models.CharField(max_length=1, choices=STATE_CHOICES, default='A', verbose_name='Estado do Anúncio')

    def __str__(self):
        return self.nome_prod


class AnuncioVenda(Anuncio):
    class Meta:
        verbose_name_plural = "Anúncios de Venda"

    preco_prod = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço do Produto')

    

class AnuncioDoacao(Anuncio):
    class Meta:
        verbose_name_plural = "Anúncios de Doação"
