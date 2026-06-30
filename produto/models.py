from django.conf import settings
import os
from PIL import Image
from django.db import models
from django.utils.text import slugify
from utils import utils


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(verbose_name='Descrição', default='')
    
    # Organiza o upload de imagens em pastas dinâmicas baseadas no ano e mês atual
    imagem = models.ImageField(
        upload_to='produto_imagens/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    preco_marketing_promocional = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, verbose_name='Preço Promo.')
    
    # Define se o produto possui variações
    
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
        )
    )

    def get_preco_formatado(self):
        return utils.formata_preco(self.preco_marketing)
    get_preco_formatado.short_description = 'Preço'

    def get_preco_promocional_formatado(self):
        return utils.formata_preco(self.preco_marketing_promocional)
    get_preco_promocional_formatado.short_description = 'Preço Promo.'

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        with Image.open(img_full_path) as img_pil:
            original_width, original_height = img_pil.size

            if original_width <= new_width:
                return

            new_height = round((new_width * original_height) / original_width)

            new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
            new_img.save(
                img_full_path,
                optimize=True,
                quality=50
            )
    
    # Sobrescreve o salvamento para automatizar a criação do slug e o tratamento de imagem
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.nome)
            slug = base_slug
            counter = 1
            # Verifica se o slug já existe e adiciona um sufixo se necessário
            while Produto.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    preco_promocional = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
