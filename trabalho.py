

class trabalho:
	
	def __init__(self, nome:str, deadLine:float, localizacao:int) -> None:
		"""
		nome:str
			Nome da tarefa que deve ser feita
		
		deadLine:float
			Para quando a tarefa deve ser feita
		
		localizacao:int
			Onde a tarefa esta, 0 - Tribo da agua, 1 - Tribo do Fogo, 2 - Tribo do ar, 3 - Tribo da Terra
		"""
		self.nome = nome
		self.deadLine = deadLine
		self.localizacao = localizacao


class elo:
	def __init__(self, loc1:int, loc2:int, peso:float) -> None:
			self.loc1 = loc1
			self.loc2 = loc2
			self.peso = peso

	