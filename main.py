from avatar import generateAvatar
from avatar import generateElemento

avatar = generateAvatar()
elemento, dobra_especial = generateElemento()

while(dobra_especial != 'metal e lava'):
    print(avatar, elemento, dobra_especial)
    avatar = generateAvatar()
    elemento, dobra_especial = generateElemento()

print(avatar, elemento, dobra_especial)