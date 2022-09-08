# Generated by Django 4.1.1 on 2022-09-08 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0013_address_cep"),
        ("marketplace", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="anunciodoacao",
            options={"verbose_name_plural": "Anúncios de Doação"},
        ),
        migrations.AlterModelOptions(
            name="anunciovenda",
            options={"verbose_name_plural": "Anúncios de Venda"},
        ),
        migrations.AlterField(
            model_name="anunciodoacao",
            name="address_prod",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="company.address",
                verbose_name="Endereço do Produto",
            ),
        ),
        migrations.AlterField(
            model_name="anunciodoacao",
            name="descricao_prod",
            field=models.TextField(verbose_name="Descrição do Produto"),
        ),
        migrations.AlterField(
            model_name="anunciodoacao",
            name="img_prod",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="marketplace",
                verbose_name="Imagem do Produto",
            ),
        ),
        migrations.AlterField(
            model_name="anunciodoacao",
            name="nome_prod",
            field=models.CharField(max_length=100, verbose_name="Nome do Produto"),
        ),
        migrations.AlterField(
            model_name="anunciodoacao",
            name="quantidade_prod",
            field=models.IntegerField(verbose_name="Quantidade do Produto"),
        ),
        migrations.AlterField(
            model_name="anunciodoacao",
            name="state",
            field=models.CharField(
                choices=[("A", "Ativo"), ("I", "Inativo")],
                default="A",
                max_length=1,
                verbose_name="Estado do Anúncio",
            ),
        ),
        migrations.AlterField(
            model_name="anunciovenda",
            name="address_prod",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="company.address",
                verbose_name="Endereço do Produto",
            ),
        ),
        migrations.AlterField(
            model_name="anunciovenda",
            name="descricao_prod",
            field=models.TextField(verbose_name="Descrição do Produto"),
        ),
        migrations.AlterField(
            model_name="anunciovenda",
            name="img_prod",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="marketplace",
                verbose_name="Imagem do Produto",
            ),
        ),
        migrations.AlterField(
            model_name="anunciovenda",
            name="nome_prod",
            field=models.CharField(max_length=100, verbose_name="Nome do Produto"),
        ),
        migrations.AlterField(
            model_name="anunciovenda",
            name="preco_prod",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Preço do Produto"
            ),
        ),
        migrations.AlterField(
            model_name="anunciovenda",
            name="quantidade_prod",
            field=models.IntegerField(verbose_name="Quantidade do Produto"),
        ),
        migrations.AlterField(
            model_name="anunciovenda",
            name="state",
            field=models.CharField(
                choices=[("A", "Ativo"), ("I", "Inativo")],
                default="A",
                max_length=1,
                verbose_name="Estado do Anúncio",
            ),
        ),
    ]