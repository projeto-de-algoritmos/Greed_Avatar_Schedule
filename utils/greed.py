from time import time_ns
from utils import trabalho
from utils import grafo as GF


class minLat:
    def __init__(self) -> None:
        self.graph = GF.Grafo(False)
        self.graph.createPoints()

    def minDelay(self, ListaDeTarefas: list):

        ListaDeTarefas.sort(key=lambda x: x.deadLine)

        currnTime = 0
        times = []
        tastksDone = []
        travelTime = []
        overTime = []

        for index, task in enumerate(ListaDeTarefas):
            tastksDone.append(task)

            if index == 0:
                # print(f"{trabalho.localizacoes.get(6)} -> {task.localizacao}")
                travelTime.append(self.graph.getWeight(trabalho.localizacoes.get(6), task.localizacao))
            elif index < len(ListaDeTarefas):
                # print(f"{ListaDeTarefas[index - 1].localizacao} -> {task.localizacao} = {self.graph.getWeight(ListaDeTarefas[index - 1].localizacao, task.localizacao)}")
                travelTime.append(self.graph.getWeight(ListaDeTarefas[index - 1].localizacao, task.localizacao))

            times.append(currnTime + travelTime[index])
            currnTime += task.duracao + travelTime[index]
            

            overTime.append(currnTime - task.deadLine)
            
        return times, tastksDone, overTime, travelTime


# def minimumLateness(d, duracao, n):
#     d.sort()
#     t = 0
#     s = []
#     f = []

#     for j in range(n):
#         s.append(t)
#         tempoDuracao = t + duracao[j]
#         f.append(tempoDuracao)
#         t = t + duracao[j]
#         print(s[j], f[j])

# deadLine = [6, 8, 9, 9, 14, 15]
# duracao = [3, 2, 1, 4, 3, 2]


# minimumLateness(deadLine, duracao, len(deadLine))


# pq = minLat()

# pq.minDelay(trabalho("Ola", 15, 25, ))