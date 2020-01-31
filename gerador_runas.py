#gerador de runas, provavelmente na sequencia do Uthark
import random

def geraRuna():    
    #definir variaveis locais
    runa_significado = None
    runa_escolhida = None
    
    #Lista de runas
    dic_runas = {
    #Primeiro Aetir
        "Ur":"ᚢ",
        "Thurs":"ᚦ",
        "As":"ᚫ",
        "Raid":"ᚱ",
        "Ken":"ᚲ",
        "Gifu":"ᚷ",
        "Wynja":"ᚹ",
        "Hagal":"ᚺ",
    #Segundo Aetir
        "Naud":"ᚾ",
        "Is":"ᛁ",
        "Jara":"ᛃ",
        "Perthra":"ᛈ",
        "Eihwaz":"ᛇ",
        "Algiz":"ᛉ",
        "Sol":"ᛋ",
        "Tyr":"ᛏ",
    #Terceiro Aetir
        "Bjarka":"ᛒ",
        "Eh":"ᛖ",
        "Manaz":"ᛗ",
        "Laguz":"ᛚ",
        "Ing":"ᛜ",
        "Odal":"ᛟ",
        "Dagaz":"ᛞ",
        "Fehu":	"ᚠ"
    }

    #Transforma dicionario em lista
    runas_list = list(dic_runas.items())
    #print(runas_list)

    #Passa os valores da runa escolhida para cada uma das variáveis
    runa_significado , runa_escolhida = random.choice(runas_list)

    return(print(runa_significado, runa_escolhida))


geraRuna()