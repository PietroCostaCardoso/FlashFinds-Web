from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from .forms import ProdutoForm, VariacaoFormSet
from perfil.models import Perfil

# Lista os produtos na página principal
class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10
    ordering = ['-id']

# Realiza a busca filtrando
class Busca(ListaProdutos):
    def get_queryset(self, *args, **kwargs):
        termo = self.request.GET.get('termo') or self.request.session.get('termo')
        qs = super().get_queryset(*args, **kwargs)

        if not termo:
            return qs

        self.request.session['termo'] = termo

        qs = qs.filter(
            Q(nome__icontains=termo) |
            Q(descricao__icontains=termo)
        )

        self.request.session.save()
        return qs


class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'

# Gerencia a lógica de inserção e atualização
class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
        )
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(
                self.request,
                'Produto não existe'
            )
            return redirect(http_referer)

        variacao = get_object_or_404(models.Variacao, id=variacao_id)
        variacao_estoque = variacao.estoque
        produto = variacao.produto

        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ''
        preco_unitario = float(variacao.preco)
        preco_unitario_promocional = float(variacao.preco_promocional)
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem

        if imagem:
            imagem = imagem.name
        else:
            imagem = ''

        if variacao.estoque < 1:
            messages.error(
                self.request,
                'Estoque insuficiente'
            )
            return redirect(http_referer)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if variacao_id in carrinho:
            quantidade_carrinho = carrinho[variacao_id]['quantidade']
            quantidade_carrinho += 1

            if variacao_estoque < quantidade_carrinho:
                messages.warning(
                    self.request,
                    f'Estoque insuficiente para {quantidade_carrinho}x no '
                    f'produto "{produto_nome}". Adicionamos {variacao_estoque}x '
                    f'no seu carrinho.'
                )
                quantidade_carrinho = variacao_estoque

            carrinho[variacao_id]['quantidade'] = quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo'] = preco_unitario * \
                quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo_promocional'] = preco_unitario_promocional * \
                quantidade_carrinho
        else:
            carrinho[variacao_id] = {
                'produto_id': produto_id,
                'produto_nome': produto_nome,
                'variacao_nome': variacao_nome,
                'variacao_id': variacao_id,
                'preco_unitario': preco_unitario,
                'preco_unitario_promocional': preco_unitario_promocional,
                'preco_quantitativo': preco_unitario,
                'preco_quantitativo_promocional': preco_unitario_promocional,
                'quantidade': 1,
                'slug': slug,
                'imagem': imagem,
            }

        self.request.session.save()

        messages.success(
            self.request,
            f'Produto {produto_nome} {variacao_nome} adicionado ao seu '
            f'carrinho {carrinho[variacao_id]["quantidade"]}x.'
        )

        if self.request.GET.get('comprar'):
            return redirect('produto:resumodacompra')

        return redirect(http_referer)

# Remove completamente uma variação de produto específica do carrinho
class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
        )
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            return redirect(http_referer)

        if not self.request.session.get('carrinho'):
            return redirect(http_referer)

        if variacao_id not in self.request.session['carrinho']:
            return redirect(http_referer)

        carrinho = self.request.session['carrinho'][variacao_id]

        messages.success(
            self.request,
            f'Produto {carrinho["produto_nome"]} {carrinho["variacao_nome"]} '
            f'removido do seu carrinho.'
        )

        del self.request.session['carrinho'][variacao_id]
        self.request.session.save()
        return redirect(http_referer)


class Carrinho(View):
    def get(self, *args, **kwargs):
        contexto = {
            'carrinho': self.request.session.get('carrinho', {})
        }

        return render(self.request, 'produto/carrinho.html', contexto)

#revisão do pedido
class ResumoDaCompra(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:criar')

        perfil = Perfil.objects.filter(usuario=self.request.user).exists()

        if not perfil:
            messages.error(
                self.request,
                'Usuário sem perfil.'
            )
            return redirect('perfil:criar')

        if not self.request.session.get('carrinho'):
            messages.error(
                self.request,
                'Carrinho vazio.'
            )
            return redirect('produto:lista')

        contexto = {
            'usuario': self.request.user,
            'carrinho': self.request.session['carrinho'],
        }

        return render(self.request, 'produto/resumodacompra.html', contexto)

class RemoverProduto(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        produto = get_object_or_404(models.Produto, slug=slug)
        nome_produto = produto.nome
        produto.delete()

        messages.success(
            self.request,
            f'O anúncio do produto "{nome_produto}" foi removido com sucesso.'
        )
        return redirect('produto:lista')

class CriarProduto(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        form = ProdutoForm()
        formset = VariacaoFormSet()
        return render(self.request, 'produto/criar.html', {
            'form': form,
            'formset': formset
        })

    def post(self, *args, **kwargs):
        form = ProdutoForm(self.request.POST, self.request.FILES)
        formset = VariacaoFormSet(self.request.POST)

        if form.is_valid() and formset.is_valid():
            produto = form.save(commit=False)
            produto.tipo = 'V'  # Definir tipo como 'Variável'
            
            produto.preco_marketing = 0
            produto.preco_marketing_promocional = 0

            # Salva primeiro para gerar o ID do produto e permitir as variações
            produto.save()

            # Vincula as variações ao produto e salva no banco
            formset.instance = produto
            formset.save()

            variacoes = produto.variacao_set.all()
            if variacoes.exists():
                produto.preco_marketing = variacoes.order_by('preco').first().preco

                # Se houver variações com promoção, mostra o menor preço promocional
                variacoes_promocionais = variacoes.exclude(preco_promocional=0).order_by('preco_promocional')
                if variacoes_promocionais.exists():
                    produto.preco_marketing_promocional = variacoes_promocionais.first().preco_promocional
                
                # Salva o produto novamente
                produto.save()

            messages.success(self.request, f'Produto "{produto.nome}" anunciado com sucesso!')
            return redirect('produto:lista')

        return render(self.request, 'produto/criar.html', {
            'form': form,
            'formset': formset
        })
