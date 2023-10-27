class Produto:
  
  def __init__(self, id:int, nome:str, quantidade:int, tag_id:int):
    self.__id = id
    self.__nome = nome
    self.__quantidade = quantidade
    self.__tag_id = tag_id

  def __str__(self):
    return f'{self.getID()}:{self.getNome()}:{self.getAmount()}:{self.getTagID()}'

  def getID(self) -> int:
    return self.__id
  
  def getNome(self) -> str:
    return self.__nome
  
  def setNome(self, nome:str):
    self.__nome = nome
  
  def getAmount(self) -> int:
    return self.__quantidade
  
  def setAmount(self, Amount:str):
    self.__quantidade = Amount
  
  def getTagID(self) -> int:
    return self.__tag_id
  
  def changeTagID(self, newTag):
    self.__tag_id = newTag