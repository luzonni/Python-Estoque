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

    def add(self, produto:Produto):
        newId = produto.getID()
        for p in self.getList():
            if p.getID() == newId:
                return
        self.getList().append(produto)
        
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
        if os.path.exists(path):
           self.buildFile()
        arquivo = open(path, 'r')
        produtos = arquivo.read().split("/")[0:-1]
        for produto in produtos:
            produto = produto.split(":")
            self.getList().append(Produto(produto[0], produto[1], produto[2], produto[3]))
        self.clearFile()
    
    def closeList(self):
        path = self.getPath()
        arquivo = open(path, 'a')
        for produto in self.getList():
            arquivo.write(str(produto)+"/")