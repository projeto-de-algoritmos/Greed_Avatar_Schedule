

class trabalho:
	
	def __init__(self, nome:str, deadLine:float, localizacao:int) -> None:
		"""
		nome:str
			Nome da tarefa que deve ser feita
		
		deadLine:float
			Para quando a tarefa deve ser feita
		
		localizacao:int
			Onde a tarefa esta, 0 - Tribo da agua, 1 - Tribo da Terra, 2 - Tribo do Fogo, 3 - Tribo do ar
		"""
		self.nome = nome
		self.deadLine = deadLine
		self.localizacao = localizacao
	