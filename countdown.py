import tkinter as tk
from datetime import datetime


secondi = 0
secondi_totali = 0
in_esecuzione =False
secondi_sessione = 0

def aggiorna():
    global secondi, secondi_totali
    minuti = secondi // 60
    seconds = secondi % 60 
    etichetta.config(text=f"{minuti:02d}:{seconds:02d}")
    min_tot = secondi_totali // 60
    sec_tot = secondi_totali % 60
    etichetta_totale.config(
    text=f"tempo totale: {min_tot:02d}:{sec_tot:02d}"
)
    finestra.after(1000, aggiorna) 
    if in_esecuzione and secondi > 0:
        secondi -= 1 
        secondi_totali += 1

        if secondi <= 0:
            salva_sessione()
            stop()

def start():
    global in_esecuzione

    libro = campo_libro.get().strip()
    pagine = campo_pagine.get().strip()
    pagina_finale = campo_pagina_finale.get().strip()

    if libro == "" or pagine == "" or pagina_finale == "":
        return


    if secondi <= 0:
        return

    in_esecuzione = True
    btn_toggle.config(text="Stop")


def stop():
    global in_esecuzione
    in_esecuzione = False
    btn_toggle.config(text="Start")

def reset(event=None):
    global secondi, in_esecuzione
    secondi = 0
    in_esecuzione = False

def imposta(event=None):
    global secondi, secondi_sessione
    minuti = int(campo.get())
    secondi = minuti * 60
    secondi_sessione = secondi

def toggle(event=None):
    if in_esecuzione:
        stop()
    else:
        start()

def salva_sessione(): 
    pagine_lette = campo_pagine.get()
    libro = campo_libro.get()
    pagina_finale = campo_pagina_finale.get()

    if libro == "" or pagine_lette == "" or pagina_finale == "":
        return

    adesso = datetime.now()
    minuti = secondi_sessione // 60

    with open("sessioni.txt", "a") as file:
        file.write(
            f"{adesso.strftime('%d/%m/%Y %H:%M')} - "
            f"Libro: {libro} - "
            f"{minuti} minuti - "
            f"{pagine_lette} pagine lette -\n "
            f"Siamo arrivati a pagina {pagina_finale}\n"

        )

finestra = tk.Tk()
finestra.title("Study Timer")
finestra.geometry("400x550")

etichetta = tk.Label(finestra, text="00:00", font=("Arial", 48))
etichetta.pack(pady=40)

etichetta_totale = tk.Label(finestra, text="tempo totale: 00:00", font=("Arial", 14))
etichetta_totale.pack(pady=40)



frame_btn = tk.Frame(finestra)
frame_btn.pack(pady=40)

btn_toggle = tk.Button(frame_btn, text="Start", command=toggle)
btn_toggle.pack(side="left", padx=10)

btn_reset = tk.Button(frame_btn, text="Reset", command=reset )
btn_reset.pack(side="left", padx=10)

btn_imposta = tk.Button(frame_btn, text="Imposta", command=imposta)
btn_imposta.pack(side="left", padx=30)


finestra.bind("|", reset)    # "|" per reset
finestra.bind("\\", toggle) # "\" sia per start che stop


frame_minuti = tk.Frame(finestra)
frame_minuti.pack(anchor="w", padx=20, pady=5)
tk.Label(frame_minuti, text="Durata sessione (minuti)").pack(side="left")
campo = tk.Entry(frame_minuti, width=5, font=("Arial", 16))
campo.pack(side="left", padx=5)
campo.bind("<Return>", imposta)

frame_pagine = tk.Frame(finestra)
frame_pagine.pack(anchor="w", padx=20, pady=5)
tk.Label(frame_pagine, text="Pagine lette").pack(side="left")
campo_pagine = tk.Entry(frame_pagine, width=5, font=("Arial", 16))
campo_pagine.pack(side="left", padx=5)

frame_libro = tk.Frame(finestra)
frame_libro.pack(anchor="w", padx=20, pady=5)
tk.Label(frame_libro, text="Nome libro").pack(side="left")
campo_libro = tk.Entry(frame_libro, width=20, font=("Arial", 14))
campo_libro.pack(side="left", padx=5)

frame_raggiunto = tk.Frame(finestra)
frame_raggiunto.pack(anchor="w", padx=20, pady=5)
tk.Label(frame_raggiunto, text="Pagina raggiunta").pack(side="left")
campo_pagina_finale = tk.Entry(frame_raggiunto, width=5, font=("Arial", 14))
campo_pagina_finale.pack(side="left", padx=5)

aggiorna()
finestra.mainloop()

