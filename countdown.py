import tkinter as tk

secondi = 0
secondi_totali = 0
in_esecuzione =False

def aggiorna():
    global secondi, secondi_totali
    minuti = secondi // 60
    seconds = secondi % 60 
    etichetta.config(text=f"{minuti:02d}:{seconds:02d}")
    min_tot = secondi_totali // 60
    sec_tot = secondi_totali % 60
    etichetta_totale.config(text=f"{min_tot:02d}:{sec_tot:02d}") 
    finestra.after(1000, aggiorna) 
    if in_esecuzione:
        secondi -= 1 
        secondi_totali += 1
        if secondi <= 0:
            stop()

def start():
    global in_esecuzione
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
    global secondi
    minuti = int(campo.get())
    secondi = minuti * 60

def toggle(event=None):
    if in_esecuzione:
        stop()
    else:
        start()

finestra = tk.Tk()
finestra.title("Study Timer")
finestra.geometry("400x550")

etichetta = tk.Label(finestra, text="00:00", font=("Arial", 48))
etichetta.pack(pady=40)

etichetta_totale = tk.Label(finestra, text="tempo totale: 00:00", font=("Arial", 14))
etichetta_totale.pack(pady=40)

frame_btn = tk.Frame(finestra)
frame_btn.pack(pady=40)

#btn_start = tk.Button(frame_btn, text="Start", command=start)
#btn_start.pack(side="left", padx=10)

#btn_stop = tk.Button(frame_btn, text="Stop", command=stop)
#btn_stop.pack(side="left", padx=10)
btn_toggle = tk.Button(frame_btn, text="Start", command=toggle)
btn_toggle.pack(side="left", padx=10)

btn_reset = tk.Button(frame_btn, text="Reset", command=reset )
btn_reset.pack(side="left", padx=10)

btn_imposta = tk.Button(frame_btn, text="Imposta", command=imposta)
btn_imposta.pack(side="left", padx=30)

#finestra.bind("", start)    # "" per start
#finestra.bind("", stop)     # "" per pausa
finestra.bind("|", reset)    # "|" per reset
finestra.bind("\\", toggle) # "\" sia per start che stop

campo = tk.Entry(finestra,  width=5, font=("Arial", 24))
campo.pack(pady=10)
campo.bind("<Return>", imposta)  # Return = tasto Invio  # "i" per imposta

aggiorna()
finestra.mainloop()

