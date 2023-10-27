import os

def getTags(path:str):
    if os.path.exists(path):
        with open(path, 'r') as arquivo:
            tags = []
            text = arquivo.read().split("/")
            for item in text:
                tags.append(item)
            return tags[0: len(tags)-1]
    else:
        with open(path, 'w') as arquivo:
            arquivo.write(changeToFile(createTags()))
        return getTags()

def createTags():
    tags = []
    while True:
        value = input(f'Escreva a tag {len(tags)+1}:\n')
        tags.append(value)
        if input("Quer adivionar mais uma tag? (y/n)\n") == "n":
            break
    return tags

def changeToFile(tagsArray):
    line = ""
    for tag in tagsArray:
        line += tag + "/"
    return line