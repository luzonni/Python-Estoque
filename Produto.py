import os

class Produto:
  def __init__(self, id:int, nome:str, quantidade:int, tag_id:int):
    self.id = id
    self.nome = nome
    self.quantidade = quantidade
    self.tag_id = tag_id

  # TODO transformar em formato JSON
  def __str__(self):
    return f'{self.id}:{self.nome}:{self.quantidade}:{self.tag_id}'

  def somaQuantidade(self, valor):
    self.Quantidade += valor

  def subtraiQuantidade(self, valor):
    self.Quantidade -= valor

def insert(id:int, name:str, amount:int, tag_id:int):
    path = "Banco.txt"
    produto = Produto(id, name, amount, tag_id)
    if os.path.exists(path):
        with open(path, 'a') as arquivo:
            arquivo.write(str(produto)+"/")
    else:
        with open(path, 'w') as arquivo:
            arquivo.write(str(produto)+"/")

def getter(id:int):
    path = "Banco.txt"
    if not os.path.exists(path):
        raise FileNotFoundError("Arquivo de banco não encontrado")
    arquivo = open(path, 'r')
    item = arquivo.read().split("/")[id].split(":")
    return Produto(item[0], item[1], item[2], item[3])
