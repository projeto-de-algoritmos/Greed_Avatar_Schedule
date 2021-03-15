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