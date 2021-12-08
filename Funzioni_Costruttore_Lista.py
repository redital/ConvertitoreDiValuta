import tkinter as tk

def lettura():
    lista_valute=[['Euro','EUR',1.0]]
    i=1

    try:
        lettura=open("ListaValute.txt","r").readlines()
        for i in range (int((len(lettura)/3))):
            if i!=(int((len(lettura)/3))-1):
                lista_valute.append(['Euro','EUR',1.0])
            for j in range (3):
                lista_valute[i][j]=lettura[((i)*3)+j].strip('\n')
            j=0
    except FileNotFoundError:
        i=i
    return lista_valute

lista_valute=lettura()

def scrittura():
    file_lista=open("ListaValute.txt","w")
    flag=1
    i=0
    j=0
    while flag==1:
        for j in range(3):
            file_lista.write(str(lista_valute[i][j])+"\n")
            j=j+1
        j=0
        if i==len(lista_valute)-1:
            flag=0
        i=i+1
    file_lista.close()
    

def eliminazione(tmp):
    if tmp!=0:
        del lista_valute[int(tmp-1)]
    scrittura()


def inserimento(valuta):
    i=int(len(lista_valute))
    j=0
    lista_valute.append(['Euro','EUR',1.0])
    lista_valute[i][0]=valuta[0]
    lista_valute[i][1]=valuta[1]
    try:
        lista_valute[i][2]=float(valuta[2])
        for j in range(len(lista_valute)-1):
            if lista_valute[i][0]==lista_valute[j][0].strip("\n") or lista_valute[i][1]==lista_valute[j][1].strip("\n"):
                #j=len(lista_valute)
                del lista_valute[i]
                i=0
                testo='Valuta già presente in elenco\nDuplicato eliminato'
                messaggio_errore(testo)
                #print('\nValuta già presente in elenco\nDuplicato eliminato')
    except ValueError:
        del lista_valute[i]
        testo='Solo valori numerici, grazie!\nValuta eliminata'
        messaggio_errore(testo)
        #print("ERRORE! Solo valori numerici, grazie!\nValuta eliminata")
    i=int(len(lista_valute))
    scrittura()


def messaggio_errore(testo):
        window=tk.Tk()
        window.title("ERRORE")
        window.resizable(False,False)
        messaggio=tk.Label(window,text=testo,fg="Red", font=("TimesNewRomans",15),padx=10)
        messaggio.grid(row=0,column=0,padx=15,pady=15)
        window.columnconfigure(0,weight=1)
        window.rowconfigure(0,weight=1)
    
