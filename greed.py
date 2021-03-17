from trabalho import trabalho
from trabalho import elo


def minDelay(ListaDeTarefas: list):
    # n eh uma lista das deadlines

    ultimoTrabalho = trabalho()
    ListaDeTarefas.sort(key=lambda x: x.deadLine)
    tarefasFeitas = []

    startJ = 0

    for j in ListaDeTarefas:
        tarefasFeitas.append(j)
        # Assing job j to interval [t, t + tj]
        # tarefasFeitas[j] = [t, t + tempo de duracao]
        # Atribuir tempo de duracao das tarefas
        s[j] = t
        f[j] = t + tj
        t = t + tj
    print([s[j], f[j]])























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