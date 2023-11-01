import os
from Produto import Produto

class Estoque:
    
    def __init__(self, path:str):
        self.__path = path
        self.__list = []
        self.openList()
    
    def getPath(self):
        return self.__path
    
    def getList(self):
        return self.__list
    
    def buildFile(self):
        with open(self.getPath(), 'w') as arquivo:
            arquivo.write("")
    
    def clearFile(self):
      with open(self.getPath(), 'w') as arquivo:
            arquivo.write("")
            
    def isEmpty(self) -> bool:
        if len(self.getList()) == 0:
            return True
        return False

    def add(self, produto:Produto) -> bool:
        newId = produto.getID()
        for p in self.getList():
            if p.getID() == newId:
                return False
        self.getList().append(produto)
        return True
        
    def get(self, id:int):
         for p in self.getList():
            if p.getID() == id:
                return p
        
    def remove(self, id:int):
        for p in self.getList():
            if p.getID() == id:
                self.getList().remove(p)
    
    def openList(self):
        path = self.getPath()
        if not os.path.exists(path):
           self.buildFile()
        arquivo = open(path, 'r')
        produtos = arquivo.read().split("/")[0:-1]
        for produto in produtos:
            produto = produto.split(":")
            self.getList().append(Produto(int(produto[0]), produto[1], int(produto[2]), int(produto[3])))
        self.clearFile()
    
    def closeList(self):
        path = self.getPath()
        arquivo = open(path, 'a')
        for produto in self.getList():
            arquivo.write(str(produto)+"/")