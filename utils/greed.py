from utils import trabalho
from utils import grafo as GF


class minLat:
    def __init__(self) -> None:
        self.graph = GF.Grafo(False)

        self.graph.addElo(GF.Node("Tribo da Agua"), Node("Tribo do Fogo"), 1)
        self.graph.addElo(GF.Node("Tribo da Agua"), Node("Tribo do Ar"), 2)
        self.graph.addElo(GF.Node("Tribo da Agua"), GF.Node("Tribo da Terra"), 1)
        
        self.graph.addElo(GF.Node("Tribo da Terra"), GF.Node("Tribo do Fogo"), 2)
        self.graph.addElo(GF.Node("Tribo da Terra"), GF.Node("Tribo do Ar"), 1)
        self.graph.addElo(GF.Node("Tribo da Terra"), GF.Node("Tribo da Agua"), 1)

        self.graph.addElo(GF.Node("Tribo do Ar"), GF.Node("Tribo do Fogo"), 1)
        self.graph.addElo(GF.Node("Tribo do Ar"), GF.Node("Tribo da Terra"), 1)
        self.graph.addElo(GF.Node("Tribo do Ar"), GF.Node("Tribo da Agua"), 2)

        self.graph.addElo(GF.Node("Tribo do Fogo"), GF.Node("Tribo do Ar"), 1)
        self.graph.addElo(GF.Node("Tribo do Fogo"), GF.Node("Tribo da Terra"), 2)
        self.graph.addElo(GF.Node("Tribo do Fogo"), GF.Node("Tribo da Agua"), 1)

    def minDelay(self, ListaDeTarefas: list):

        ListaDeTarefas.sort(key=lambda x: x.deadLine)

        currnTime = 0
        tastksDone = []
        overTime = []

        for index, task in enumerate(ListaDeTarefas):
            tastksDone.append(task)
            overTime.append(currnTime - task.deadLine)
            currnTime += task.duracao + self.graph.getWeight(task.localizacao, next(ListaDeTarefas).localizacao)
        
        return currnTime, tastksDone, overTime


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