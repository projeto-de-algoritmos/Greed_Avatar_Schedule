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

def generateElemento():
    chance = random.randint(1, 100)

    # Elemento

    if chance >= 1 and chance <= 25:
        elemento = "ar"
    elif chance > 25 and chance <= 50:
        elemento = "fogo"
    elif chance > 50 and chance <= 75:
        elemento = "terra"
    else:
        elemento = "água"


    # Sub-Dobras

    dobra_especial = ''

    dobra = random.randint(1, 10)

    sub_dobra_terra = random.randint(1, 10)

    if elemento == 'água' and dobra == 1:
        dobra_especial = 'sangue'
    elif elemento == 'fogo' and dobra == 1:
        dobra_especial = 'raio'
    elif elemento == 'terra':
        if sub_dobra_terra >= 1 and sub_dobra_terra < 5:
            dobra_especial = 'lava'
        elif sub_dobra_terra > 5 and sub_dobra_terra <= 10:
            dobra_especial = 'metal'
        elif sub_dobra_terra == 5:
            dobra_especial = 'metal e lava'

    return elemento, dobra_especial;