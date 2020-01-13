#gerador de runas, provavelmente na sequencia do Uthark
import random
#from PIL import Image

runas_uthark = [
#Primeiro Aetir
    "Ur",
    "Thurs",
    "As",
    "Raid",
    "Ken",
    "Gifu",
    "Wynja",
    "Hagal",
#Segundo Aetir
    "Naud",
    "Is",
    "Jara",
    "Perthra",
    "Eihwaz",
    "Algiz",
    "Sol",
    "Tyr",
#Terceiro Aetir
    "Bjarka",
    "Eh",
    "Manaz",
    "Laguz",
    "Ing",
    "Odal",
    "Dagaz",
    "Fehu"
]

#Misturar tres vezes, uma pra cada norna
#Para Urd
random.shuffle(runas_uthark)
#Para Verdandi
random.shuffle(runas_uthark)
#Para Skuldi
random.shuffle(runas_uthark)

#Tira uma runa e a exclui da lista
escolheRuna = random.choice(runas_uthark)
runas_uthark.remove(escolheRuna)
print(escolheRuna)