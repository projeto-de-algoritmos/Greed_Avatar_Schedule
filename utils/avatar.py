import random


class elemento:
	def __init__(self, nome_elemento: str) -> None:
			self.nome = nome_elemento
			self.subDobras = []

	def add_sub_dobra(self, nome_sub_dobra:str, chance_de_acontecer:float): #TODO: Mudar para porcentagem.
		self.subDobras += [nome_sub_dobra] * chance_de_acontecer

	def getSubDobra(self, escolha:int):
		if escolha > len(self.subDobras):
			return ""
		else:
			return self.subDobras[escolha - 1]



def generateAvatar():
	consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
	vogais = ['a', 'e', 'i', 'o', 'u']

	avatar = ""

	for i in range(5):
			if i == 1 or i == 4:
					avatar += random.choice(vogais)
			else:
					avatar += random.choice(consoantes)

	return avatar.capitalize()


def generateElemento():

	elementos = {"ar": elemento("ar"), "fogo": elemento("fogo"), "terra": elemento("terra"), "água": elemento("água")}

	nomeElemento, objElemento = random.choice(list(elementos.items()))

	# Sub-Dobras
	elementos["água"].add_sub_dobra("sangue", 1)

	elementos["fogo"].add_sub_dobra("raio", 1)

	elementos["terra"].add_sub_dobra("metal", 5)
	elementos["terra"].add_sub_dobra("lava", 4)
	elementos["terra"].add_sub_dobra("metal e lava", 1)


	return nomeElemento, objElemento.getSubDobra(random.randint(1, 10))