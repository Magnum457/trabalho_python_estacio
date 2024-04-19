from produto import Produto

class ListaProdutos:
  def __init__(self):
    self.produtos = {}

  def cadastrar_produto(self, produto : Produto):
    self.produtos[produto.nomeItem] = produto

  def listar_produtos(self):
    for nomeItem in self.produtos.keys():
      print(f"O produto {nomeItem} tem {self.produtos[nomeItem].qtd} itens e custa {self.produtos[nomeItem].valor}")
      print(f"Contando com os impostos o valor do produto é {self.produtos[nomeItem].calculaImposto()}")

p = Produto(200.0, "mouse", 3)

print(f"O produto novo se chama: ", p.nomeItem)
print(f"O valor do produto é: ", p.valor)
print(f"A quantidade de produtos cadastrados é: ", p.qtd)
print(f"O valor do produtos com impostos é: ", p.calculaImposto())

l = ListaProdutos()

l.cadastrar_produto(p)
l.listar_produtos()
