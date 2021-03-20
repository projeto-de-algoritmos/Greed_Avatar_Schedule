import prettytable
from utils import avatar as AV
from utils import image as IMG
from utils import trabalho as TSK
from utils import greed as GD

from prettytable import PrettyTable
import time

avatar = AV.generateAvatar()
elemento, dobra_especial = AV.generateElemento()

tabela = PrettyTable()
tabela.field_names = ["Nome do problema", "Duração problema", "Dead line do problema", "Localização"]

print(f'Água, Terra, Fogo e Ar somente o Avatar é capaz de dominar os quatro elementos e manter o equilíbrio do mundo')
# time.sleep(2)
# IMG.main()
# time.sleep(2)
print(f'Bem-vindo(a) a uma nova era, desde as aventuras de Korra o mundo mudou completamente e com ele novas tecnologias e inovações foram surgindo, apesar disso muitos desequilíbrios ainda acontecem é por isso o avatar deverá estar lá para ajudar a manter o equilíbrio na balança do mundo')
if dobra_especial == "":
    print(f'Após Korra surgi um novo avatar seu nome é {avatar} nascido um dobrador de {elemento}')
else:
    print(f'Após Korra surgi um novo avatar seu nome é {avatar} nascido um dobrador de {elemento}, o descobrimento de novas sub-drobas afetou também a linhagem avatar, {avatar} é capaz de dobrar também {dobra_especial}')
print(f'{avatar} assim como todos os outros avatares, tem um time de amigos que o ajuda em sua jornada, e você faz parte dele, apesar de não ter nenhum poder de dobra, você com o domínio das tecnologias criadas nessa nova era, ajuda o grupo a tomar decisões')

print(f'Seu objetivo é que {avatar} consiga cumprir todos os seus objetivos nas 4 nações sem que haja nenhum atraso')
print('Por isso você pode criar os problemas que o avatar terá que resolver, ou pegar problemas já criados:')
escolha = int(input('1- Criar problemas\n2- Pegar problemas prontos\n'))

tabalhosList = []

if escolha == 1:
    print('Você assumiu o comando e vai escolher as situações que o avatar terá que ajudar, você deverá escolher a quantidade de problemas a serem resolvidos, o nome desse problema, a duração e o dead line do problema, assim como a qual tribo esse problema pertence. Boa sorte membro do equipe avatar!')
    
    qtdProblemas = int(input('Quantos problemas você gostaria de resolver? '))
    for i in range(qtdProblemas):
        nomeProblema = input('Nome do problema: ')
        duracao = float(input('Duração problema: '))
        deadLine = float(input('Dead line do problema: '))
        print("Problema pertencente a qual tribo:")
        for t in TSK.localizacoes:
            print(f"{t} - {TSK.localizacoes.get(t)}")
        tribo = int(input()) 
        tabalhosList.append(TSK.trabalho(nomeProblema, duracao, deadLine, tribo))
        tabela.add_row([nomeProblema, duracao, deadLine, TSK.localizacoes.get(tribo)])
        
else:
    print(f'O mundo já possui alguns problemas que devem ser lidados, dentre eles é trazer a união do mundo espiritual com as outras nações, por isso foi dado a tarefa ao avatar {avatar} de abrir esses portais nas outras tribos, para que dessa forma todos possam se conectar.')

    tabalhosList.append(TSK.trabalho('Abrir portal para o mundo espiritual no Templo do Ar do Norte', 2, 2, 4))
    tabalhosList.append(TSK.trabalho('Abrir portal para o mundo espiritual no Reino da Terra', 2, 4, 2))
    tabalhosList.append(TSK.trabalho('Abrir portal para o mundo espiritual na Nação do Fogo', 2, 1, 3))
    tabalhosList.append(TSK.trabalho('Abrir portal para o mundo espiritual no Templo do Ar do Sul', 2, 8, 5))
    tabalhosList.append(TSK.trabalho('Voltar a Cidade República', 2, 18, 6))

    for j in tabalhosList:
        tabela.add_row([j.nome, j.duracao, j.deadLine, j.localizacao])
    

print(tabela)


finalTable = PrettyTable()
finalTable.field_names = ["Localização anterior", "Localização do problema", "Tempo de Viagem", "Problema","Feito em", "Duração problema", "Dead line do problema", "Over Time"]


minL = GD.minLat()

times, tastksDone, overTime, travelTime = minL.minDelay(tabalhosList)

for index, t in enumerate(tastksDone):
    if index == 0:
        finalTable.add_row([TSK.localizacoes.get(6), t.localizacao, travelTime[index], t.nome, times[index], t.duracao, t.deadLine, overTime[index]])
    else:
        finalTable.add_row([tastksDone[index - 1].localizacao, t.localizacao, travelTime[index], t.nome, times[index], t.duracao, t.deadLine, overTime[index]])

print(finalTable)