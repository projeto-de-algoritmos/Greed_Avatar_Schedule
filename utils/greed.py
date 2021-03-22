from utils import trabalho
from utils import grafo as GF


class minLat:
    def __init__(self) -> None:
        self.graph = GF.Grafo(False) # Criando o grafo, para utilizar as distancias.
        self.graph.createPoints() # Criando as distancias de cada localização

    def minDelay(self, ListaDeTarefas: list):

        ListaDeTarefas.sort(key=lambda x: x.deadLine) # Sort pelas deadLines de cada tarefa

        currnTime = 0
        times = [] # Tempos que cada tarefa foi feita.
        tastksDone = [] # Ordem das tarefas Feitas.
        travelTime = [] # Tempos de viagens para cada tarefa.
        overTime = [] # Tempos de over time para cada tarefa.

        for index, task in enumerate(ListaDeTarefas):
            tastksDone.append(task)

            # Calculando o tempo de viagem da posição atual até a proxima tarefa.
            if index == 0:
                travelTime.append(self.graph.getWeight(trabalho.localizacoes.get(6), task.localizacao)) 
            elif index < len(ListaDeTarefas):
                travelTime.append(self.graph.getWeight(ListaDeTarefas[index - 1].localizacao, task.localizacao)) 

            times.append(currnTime + travelTime[index]) # Tempo de conclusão da tarefa.
            currnTime += task.duracao + travelTime[index] # Tempo atual.
            

            overTime.append(currnTime - task.deadLine) # Overtime de cada tarefa feita.
            
        return times, tastksDone, overTime, travelTime # retorno dos 
