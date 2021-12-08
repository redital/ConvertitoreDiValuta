from Funzioni_Costruttore_Lista import lista_valute
import tkinter as tk


def selezione(tmp,lista_indici): 
    i=0
    for i in range((len(lista_valute))):
        if tmp==i and i not in lista_indici:
            lista_indici.append(i)
    return lista_indici

def deselezione(tmp,lista_indici):
    i=0
    for i in range((len(lista_indici))):
        if tmp==lista_indici[i]:
            del lista_indici[i]
    return lista_indici


def conversione(indice_riferimento,lista_indici,tmp):
    text="\n"
    valuta_riferimento=float(tmp)
    valuta_riferimento=valuta_riferimento/float(lista_valute[indice_riferimento][2])
    i=0
    for i in lista_indici:
        text= text + str(round(valuta_riferimento*float(lista_valute[indice_riferimento][2]),2)) + " " + lista_valute[indice_riferimento][0] + " equivalgono a " + str(round(valuta_riferimento*float(lista_valute[i][2]),2)) + " " + lista_valute[i][0] + "\n"
    return text
