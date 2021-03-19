

localizacoes = {0:"Tribo da Água do Sul", 1: "Tribo da Água do Norte", 2:"Reino da Terra", 3: "Nação do Fogo", 4: "Templo do Ar do Norte", 5: "Templo do Ar do Sul", 6: "Cidade República"}

class trabalho:
	
	def __init__(self, nome:str, duracao:int ,deadLine:float, localizacao:int) -> None:
		"""
		nome:str
			Nome da tarefa que deve ser feita
		
		deadLine:float
			Para quando a tarefa deve ser feita
		
		localizacao:int
			Onde a tarefa esta, 0 - Tribo da agua, 1 - Tribo da Terra, 2 - Tribo do Fogo, 3 - Tribo do ar
		"""
		self.nome = nome
		self.duracao = duracao
		self.deadLine = deadLine
		self.localizacao = localizacoes.get(localizacao)
	