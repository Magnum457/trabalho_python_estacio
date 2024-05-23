from lista_produtos import ListaProdutos as Lista
from produto import Produto # type: ignore

def apresenta_app():
    print("#####################################################################################")
    print("-----Bem-vindo ao app de cadastro de produtos e cálculo de impostos!-----")
    print("#####################################################################################")

def opcoes():
    print("\n\n")
    print("Escolha uma das opções abaixo:")
    print("1 - Cadastrar um produto")
    print("2 - Listar produtos cadastrados")
    print("3 - Calcular imposto")
    print("4 - Sair")

    int_opcao = int(input("Digite a opção desejada: "))

    return int_opcao

def captura_opcao(Lista):
    opcao_selecionada = opcoes()

    match opcao_selecionada:
        case 1:
            return cadastrar_produto(Lista)
        case 2:
            return listar_produtos(Lista)
        case 3:
            return calcular_imposto(Lista, Produto)
        case 4:
            return sair()
        case _:
            return opcao_invalida()
        
def cadastrar_produto(Lista):
    print("-----Cadastrando um novo produto!-----")
    valor = float(input("Digite o valor do novo produto: "))
    nomeItem = input("Digite o nome do novo produto: ")
    qtd = int(input("Digite a quantidade de itens do novo produto: "))

    produto = Produto(valor, nomeItem, qtd)
    Lista.cadastrar_produto(produto)

    print("\n\n")

    return Lista

def listar_produtos(Lista):
    print("-----Listando produtos!-----")
    Lista.listar_produtos()
    print("\n\n")
    return Lista

def sair():
    print("-----Até mais!-----")
    print("\n\n")
    return False

def opcao_invalida():
    print("Opção inválida!")
    return Lista

l = Lista()
while True:
    apresenta_app()
    l = captura_opcao(l)
    if not l:
        break