from avatar import generateAvatar
from avatar import generateElemento
from image import main
import time

avatar = generateAvatar()
elemento, dobra_especial = generateElemento()

print(f'Água, Terra, Fogo e Ar somente o Avatar é capaz de dominar os quatro elementos e manter o equilíbrio do mundo')
time.sleep(2)
main()
time.sleep(2)
print(f'Bem-vindo(a) a uma nova era, desde as aventuras de Korra o mundo mudou completamente e com ele novas tecnologias e inovações foram surgindo, apesar disso muitos desequilíbrios ainda acontecem é por isso o avatar deverá estar lá para ajudar a manter o equilíbrio na balança do mundo')
if dobra_especial == "":
    print(f'Após Korra surgi um novo avatar seu nome é {avatar} nascido um dobrador de {elemento}')
else:
    print(f'Após Korra surgi um novo avatar seu nome é {avatar} nascido um dobrador de {elemento}, o descobrimento de novas sub-drobas afetou também a linhagem avatar, {avatar} é capaz de dobrar também {dobra_especial}')
print(f'{avatar} assim como todos os outros avatares, tem um time de amigos que o ajuda em sua jornada, e você faz parte dele, apesar de não ter nenhum poder de dobra, você com o domínio das tecnologias criadas nessa nova era, ajuda o grupo a tomar decisões')

print(f'Seu objetivo é que {avatar} consiga cumprir todos os seus objetivos nas 4 nações sem que haja nenhum atraso')
print('Por isso você pode criar os problemas que o avatar terá que resolver, ou pegar problemas já criados:')
int(input('1- Criar problemas\n2- Pegar problemas prontos'))

# Possiveis atividades

# Agua
triboAgua = ['']

# Terra
triboTerra = ['']

# Fogo
triboFogo = ['']

# Ar
triboAr = ['']