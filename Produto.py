class Produto:
  
  def __init__(self, id:int, nome:str, quantidade:int, tag_id:int):
    self.__id = id
    self.__nome = nome
    self.__quantidade = quantidade
    self.__tag_id = tag_id

  def __str__(self):
    return f'{self.getID()}:{self.getNome()}:{self.getAmount()}:{self.getTagID()}'

  def getID(self):
    return self.__id
  
  def getNome(self):
    return self.__nome
  
  def getAmount(self):
    return self.__quantidade
  
  def getTagID(self):
    return self.__tag_id
    
  def somaQuantidade(self, valor):
    self.__quantidade += valor

  def subtraiQuantidade(self, valor):
    self.__quantidade -= valor