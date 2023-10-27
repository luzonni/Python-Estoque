
from Produto import Produto
from Estoque import Estoque
from Tagger import getTags

# Variavel que possui uma lista de categorias salvas (Antes de rodar a janela)
TAGS:list = getTags()

print(TAGS)

# Inicialização do estoque//banco (Antes de começar a rodar a janeça)
estoque = Estoque("Banco.txt")



estoque.add(Produto(0, "Beterraba", 32, 0))
estoque.add(Produto(1, "Cenoura", 45, 3))
estoque.add(Produto(2, "Couve", 56, 2))
estoque.add(Produto(3, "Repolho", 36, 1))
estoque.add(Produto(4, "Açai", 36, 1))
estoque.add(Produto(5, "Peripessia", 36, 1))

estoque.get(2)

estoque.remove(1)

# Listagem final (Apenas para mostrar no console)
for produto in estoque.getList():
    print(str(produto))
    
# Fechamento do estoque para salvar os arquivos (Sempre no final // finalização da janela)
estoque.closeList()

