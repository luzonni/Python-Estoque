class Produto:
  
  def __init__(self, id:int, nome:str, quantidade:int, tagId:int):
    self.__id = id
    self.__nome = nome
    self.__quantidade = quantidade
    self.__tagId = tagId

  def __str__(self):
    return f'{self.id}:{self.nome}:{self.quantidade}:{self.tagId}'

  @property
  def id(self) -> int:
    return self.__id
  
  @property
  def nome(self) -> str:
    return self.__nome
  
  @nome.setter
  def nome(self, nome:str):
    self.__nome = nome
  
  @property
  def quantidade(self) -> int:
    return self.__quantidade
  
  @quantidade.setter
  def quantidade(self, Amount:str):
    self.__quantidade = Amount
  
  @property
  def tagId(self) -> int:
    return self.__tagId
  
  @tagId.setter
  def tagId(self, newTagId):
    self.__tagId = newTagId