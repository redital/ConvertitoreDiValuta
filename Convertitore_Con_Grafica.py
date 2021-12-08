from Funzioni_Costruttore_Lista import *
from Funzioni_Convertitore_Valuta import *
import tkinter as tk

left=1

indice_riferimento=-1
for i in range(len(lista_valute)):
    if lista_valute[i][1]=="EUR" and lista_valute[i][0]=='Euro':
        indice_riferimento=i

lista_indici=[]

def acquisizioneCon():
    global testo
    testo=barra_input_quantità.get()

def acquisizioneEl():
    global indice_riferimento
    if int(indice_riferimento)==lista.index(tk.ANCHOR)-1:
        indice_riferimento=-1
    eliminazione(lista.index(tk.ANCHOR))
    stampa()
    output.delete('1.0',tk.END)
    stampa_config()

def acquisizioneIns():
    global indice_riferimento
    valuta=['Euro','EUR',1.0]
    valuta[0]=barra_input0.get()
    valuta[1]=barra_input1.get()
    valuta[2]=barra_input2.get()
    inserimento(valuta)
    if indice_riferimento==-1 and valuta[0]=='Euro'and valuta[1]=='EUR':
        indice_riferimento=len(lista_valute)-1
    stampa()
    output.delete('1.0',tk.END)
    stampa_config()

def stampa():
    listaconscroll.grid(row=3,column=left,sticky="WE")
    scrollbar.grid(row=3,column=left+1,sticky="WSN",pady=20)
    lista.grid(row=3,column=left,sticky="WE",pady=20)
    lista.configure(background="white")
    lista.delete(0,tk.END)
    lista.insert(tk.END,"{:<23s} {:<8s} {:<20s}".format("Nome","Codice","Tasso"))
    for i in range(len(lista_valute)):
        lista.insert(tk.END,"{:<23s} {:<8s} {:<20s}".format(lista_valute[i][0],lista_valute[i][1],str(lista_valute[i][2])))

def stampa_config():
    if indice_riferimento>=0:
        text="Conversione da " + lista_valute[indice_riferimento][1]
        if lista_indici!=[]:
            text=text + " in " + lista_valute[lista_indici[0]][1]
            for i in range(1,len(lista_indici)):
                if i==len(lista_indici)-1:
                    text=text + " e " + lista_valute[lista_indici[i]][1]
                else:
                    text=text + ", " + lista_valute[lista_indici[i]][1]
        output.insert(tk.END,text)

def inser():

    inviodel.grid_forget()
        
    testobarra0.grid(row=4,column=left,sticky="WE")
    testobarra0.configure(background="light blue")
    barra_input0.grid(row=5,column=left,sticky="WE",padx=10)

    testobarra1.grid(row=6,column=left,sticky="WE")
    testobarra1.configure(background="light blue")
    barra_input1.grid(row=7,column=left,sticky="WE",padx=10)

    testobarra2.grid(row=8,column=left,sticky="WE")
    testobarra2.configure(background="light blue")
    barra_input2.grid(row=9,column=left,sticky="WE",padx=10)
    stampa()

    invioins.grid(row=10,column=left,pady=20)


def elim():
    testobarra0.grid_forget()
    barra_input0.grid_forget()
    testobarra1.grid_forget()
    barra_input1.grid_forget()
    testobarra2.grid_forget()
    barra_input2.grid_forget()
    invioins.grid_forget()
    
    inviodel.grid(row=6,column=left,pady=20)
    

def refer():
    global indice_riferimento
    if lista.index(tk.ANCHOR)<=len(lista_valute) and lista.index(tk.ANCHOR)>0:
        output.delete('1.0',tk.END)
        indice_riferimento=lista.index(tk.ANCHOR)-1
        stampa_config()
        

def select():
    output.delete('1.0',tk.END)
    global lista_indici
    lista_indici=selezione(lista.index(tk.ANCHOR)-1,lista_indici)
    stampa_config()
    
    
def deselect():
    output.delete('1.0',tk.END)
    global lista_indici
    lista_indici=deselezione(lista.index(tk.ANCHOR)-1,lista_indici)
    stampa_config()
    

def conv():
    output.delete('2.0',tk.END)
    testo=barra_input_quantità.get()
    flag=0
    if testo=="":
        flag=1
        testo='Indicare la quantità di valuta da convertire'
        messaggio_errore(testo)
    if indice_riferimento==-1:
        flag=1
        testo='Nessuna valuta selezionata come riferimento'
        messaggio_errore(testo)
    if lista_indici==[]:
        flag=1
        testo='Nessuna valuta selezionata per la conversione'
        messaggio_errore(testo)
    if flag==0:
        text=conversione(indice_riferimento,lista_indici,testo)
        output.insert(tk.END,text)    


#=============organizzazione finestra===================================
window = tk.Tk()
window.title("Convertitore di Valuta")
window.geometry("570x670")
window.minsize(width=570,height=650)
#window.resizable(False,False)
window.configure(background="light blue")
#window.rowconfigure(1)
window.columnconfigure(0,weight=1)
window.columnconfigure(3,weight=1)

sopra=tk.Label(window)
sopra.grid(row=0,column=1,sticky="N")
sopra.configure(background="light blue")

costruzione=tk.Label(sopra)
costruzione.grid(row=0,column=left,sticky="NE")
costruzione.configure(background="light blue")

costruziones=tk.Label(sopra)
costruziones.grid(row=0,column=0,sticky="WN")
costruziones.configure(background="light blue")

#=============stampa lista==============================================

listaconscroll=tk.Label(costruzione)
listaconscroll.configure(background="light blue")
scrollbar=tk.Scrollbar(listaconscroll)
lista=tk.Listbox(listaconscroll,width=40,font=('consolas',10))
scrollbar.config(command=lista.yview)
lista.config(yscrollcommand=scrollbar.set)

#=============per funzione di inserimento===============================

pulsante_add=tk.Button(costruzione,text="Aggiungere una valuta",command=inser,width=25)
pulsante_add.grid(row=0,column=left,sticky="WE",pady=10,padx=10)

testobarra0 = tk.Label(costruzione,text="Inserire nome valuta")
barra_input0 = tk.Entry(costruzione)

testobarra1 = tk.Label(costruzione,text="Inserire codice valuta")
barra_input1 = tk.Entry(costruzione)

testobarra2 = tk.Label(costruzione,text="Inserire tasso di cambio rispetto all'euro")
barra_input2 = tk.Entry(costruzione)

invioins=tk.Button(costruzione,text="INVIO",command=acquisizioneIns)

#=============per funzione di eliminazione==============================


pulsante_del=tk.Button(costruzione,text="Rimuovere una valuta",command=elim,width=25)
pulsante_del.grid(row=1,column=left,sticky="WE",padx=10)

inviodel=tk.Button(costruzione,text="INVIO",command=acquisizioneEl)

#=============per funzione di riferimento===============================

pulsante_refer=tk.Button(costruziones,text="Cambia valuta di riferimento",command=refer,width=25)
pulsante_refer.grid(row=0,column=0,sticky="N",padx=10,pady=10)

#=============per funzione di selezione=================================

pulsante_select=tk.Button(costruziones,text="Aggiungi a selelezione",command=select,width=25)
pulsante_select.grid(row=4,column=0,sticky="N",padx=10)

pulsante_deselect=tk.Button(costruziones,text="Rimuovi da selelezione",command=deselect,width=25)
pulsante_deselect.grid(row=5,column=0,sticky="N",padx=10,pady=10)

#=============per funzione di conversione===============================

pulsante_conv=tk.Button(costruziones,text="CONVERTI",command=conv,font=("Courier",25,'bold'))
pulsante_conv.grid(row=9,column=0,sticky="N",padx=10,pady=10)

spingiinfondo=tk.Label(costruziones)
spingiinfondo.grid(row=9,column=0,sticky="S",padx=10,pady=155)
spingiinfondo.configure(background="light blue")

distanza=tk.Label(costruziones)
distanza.grid(row=6,column=0,sticky="WE",padx=10)
distanza.columnconfigure(0,weight=1)
distanza.columnconfigure(3,weight=1)
distanza.rowconfigure(0)
distanza.configure(background="light blue")

barra_input_quantità = tk.Entry(distanza,width=8)
barra_input_quantità.grid(row=0,column=2)

testobarraquantità = tk.Label(distanza,text="Quantità")
testobarraquantità.grid(row=0,column=1,sticky="WE")
testobarraquantità.configure(background="light blue")

scrollbar_output=tk.Scrollbar(window)
scrollbar_output.grid(row=10,column=2,sticky="WSN")
#scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
output=tk.Text(window,height=10,width=58,yscrollcommand=scrollbar.set,font=("Courier",9))
output.config(yscrollcommand=scrollbar.set)
output.grid(row=10,column=1,sticky="SEW")
scrollbar_output.config(command=output.yview)

#=============pulsante di aiuto=========================================
def aiuto():
    window=tk.Tk()
    window.title("Aiuto")
    window.geometry("675x450")
    window.resizable(False,True)
    window.rowconfigure(0,weight=1)
    window.columnconfigure(0,weight=1)
    window.columnconfigure(3,weight=1)
    scrollbar=tk.Scrollbar(window)
    scrollbar.grid(row=0,column=2,sticky="WSN",pady=15)
    lettura=open("NON_TOCCARE.txt","r").readlines()
    testo=""
    for i in range (len(lettura)):
        testo=testo+lettura[i]
    messaggio=tk.Text(window, font=("TimesNewRomans",11))
    messaggio.grid(row=0,column=1,pady=15,sticky="NS")
    messaggio.insert(tk.END,testo)
    scrollbar.config(command=messaggio.yview)
    messaggio.config(yscrollcommand=scrollbar.set)
    
pulsante_aiuto=tk.Button(window,text="Problemi? Premi qui!",command=aiuto,font=("Courier",7,'bold'))
pulsante_aiuto.grid(row=11,column=1,columnspan=2,sticky="SEW",pady=3)

#=======================================================================

stampa()
stampa_config()

window.mainloop()
