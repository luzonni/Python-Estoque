
from Produto import Produto
from Produto import insert
from Produto import getter
from Tagger import getTags

TAGS:list = getTags()

insert(0, "Tijolo", 1000, 0)

print(getter(0))

