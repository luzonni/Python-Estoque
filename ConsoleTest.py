from tools.Produto import Produto
from tools.Estoque import Estoque
from tools.Tagger import Tagger

PATH:str = "res/Banco.db"
Tagger:Tagger = Tagger("res/Tags.db")
TAGS:list = Tagger.getTags()

class IO:
    
    def __init__(self):
        self.__estoque = Estoque(PATH)
        self.__running = True
        self.sistem()
    
    def getEstoque(self):
        return self.__estoque
    
    def sistem(self):
        while self.__running:
            if input("Mostrar tabela? (y/n)") == "y":
                self.showTable()
            elif input("Adicionar item? (y/n)") == "y":
                self.addItem()
            elif input("Editar item? (y/n)") == "y":
                self.editarItem()
            elif input("Finalizar Programa? (y/n)") == "y":
                self.close()
                
    def addItem(self):
        table = self.getEstoque().getList()
        id = len(table)
        nome = input("Escreva o nome do seu produto:\n")
        quantidade = int(input("Escreva a quantidade do seu produto:\n"))
        tag_id = self.pickTag()
        if self.getEstoque().add(Produto(id, nome, quantidade, tag_id)):
            print("Sucesso! Produto adicionado a tabela.")
        else:
            print("Algo não deu certo ;(")
    
    def editarItem(self):
        table = self.getEstoque()
        id = int(input("Qual o ID do produto?\n"))
        if input("Deseja alterar seu nome? (y/n)") == "y":
            table.get(id).nome = input("Novo nome: ")
        elif input("Deseja alterar sua Quantidade? (y/n)") == "y":
            table.get(id).quantidade = int(input("Nova quantidade: "))
        elif input("Deseja alterar sua TAG? (y/n)") == "y":
            tag_id = self.pickTag()
            table.get(id).tagId = tag_id
            
    def pickTag(self) -> int:
        print("Escolha qual a TAG do seu produto:")
        for index in range(len(TAGS)):
            print(f'{index} - [{TAGS[index]}]')
        return int(input())
        
    def showTable(self):
        table = self.getEstoque().getList()
        for item in table:
           print(f'ID: {item.id:_>3} | Nome: {item.nome:_>25} | Quantidade: {item.quantidade:_>9} | TAG: {TAGS[item.tagId]:_>15}')

    def close(self):
        self.__running = False
        self.getEstoque().closeList()


print(" ** ATENÇÃO! Não fechar o console repentinamente, finalize o programa antes para salvar os dados corretamente! ** ")
IO()
