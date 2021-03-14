import random

def generateAvatar():
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vogais = ['a', 'e', 'i', 'o', 'u']

    nome = []

    avatar = ""

    for i in range(5):
        palavra = random.choice(consoantes)
        if i == 1:
            palavra = random.choice(vogais)
            nome.append(palavra)
        elif i == 4:
            palavra = random.choice(vogais)
            nome.append(palavra)
        else:
            nome.append(palavra)

    for x in nome:
        avatar += x

    return avatar.capitalize()