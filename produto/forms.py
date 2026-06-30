from django import forms
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from .models import Produto, Variacao


class VariacaoObrigatoria(BaseInlineFormSet):
    def _construct_form(self, i, **kwargs):
        form = super(VariacaoObrigatoria, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome', 'descricao', 'imagem',
        ]

VariacaoFormSet = inlineformset_factory(
    Produto,
    Variacao,
    fields=['nome', 'preco', 'preco_promocional', 'estoque'],
    extra=1,
    formset=VariacaoObrigatoria,
    can_delete=True
)
