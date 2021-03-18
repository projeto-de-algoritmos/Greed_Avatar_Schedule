from trabalho import trabalho
from grafo import Grafo, Node, Elo


class minLat:
    def __init__(self) -> None:
        self.graph = Grafo(False)

        self.graph.addElo(Node("Tribo da Agua"), Node("Tribo do Fogo"), 1)
        self.graph.addElo(Node("Tribo da Agua"), Node("Tribo do Ar"), 2)
        self.graph.addElo(Node("Tribo da Agua"), Node("Tribo da Terra"), 1)
        
        self.graph.addElo(Node("Tribo da Terra"), Node("Tribo do Fogo"), 2)
        self.graph.addElo(Node("Tribo da Terra"), Node("Tribo do Ar"), 1)
        self.graph.addElo(Node("Tribo da Terra"), Node("Tribo da Agua"), 1)

        self.graph.addElo(Node("Tribo do Ar"), Node("Tribo do Fogo"), 1)
        self.graph.addElo(Node("Tribo do Ar"), Node("Tribo da Terra"), 1)
        self.graph.addElo(Node("Tribo do Ar"), Node("Tribo da Agua"), 2)

        self.graph.addElo(Node("Tribo do Fogo"), Node("Tribo do Ar"), 1)
        self.graph.addElo(Node("Tribo do Fogo"), Node("Tribo da Terra"), 2)
        self.graph.addElo(Node("Tribo do Fogo"), Node("Tribo da Agua"), 1)

    def minDelay(ListaDeTarefas: list):
        
        ultimoTrabalho = trabalho()
        ListaDeTarefas.sort(key=lambda x: x.deadLine)
        tarefasFeitas = []

        startJ = 0

        for j in ListaDeTarefas:
            tarefasFeitas.append(j)
            s[j] = t
            f[j] = t + tj
            t = t + tj
        print([s[j], f[j]])








minLat()














# def printMaxActivities(s, f):
#     f.sort()
#     print(s)
#     print(f)
#     n = len(f)
#     print ("The folling activities are selected")
#     i = 0 # a primeira é sempre selecionada
#     print(i)

#     for j in range(n):
#         # print(s[j], f[i])
#         if s[j] >= f[i]:
#             print(j)
#             i = j

# s = [1, 3, 0, 5, 8, 5]
# f = [2, 4, 6, 7, 9, 9]

# s1 = [0, 1, 3, 3, 4, 5, 6, 8]
# f1 = [6, 4, 5, 8, 7, 9, 10, 11]

# printMaxActivities(s1, f1)