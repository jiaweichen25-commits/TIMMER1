import tkinter as tk

secondi = 0
in_esecuzione =False

def aggiorna():
    global secondi
    minuti = secondi // 60
    seconds = secondi % 60 
    etichetta.config(text=f"{minuti:02d}:{seconds:02d}")
    finestra.after(1000, aggiorna) 
    if in_esecuzione:
        secondi += 1 
def start():
    global in_esecuzione
    in_esecuzione = True

def stop():
    global in_esecuzione
    in_esecuzione = False

def reset():
    global secondi, in_esecuzione
    secondi = 0
    in_esecuzione = False


finestra = tk.Tk()
finestra.title("Study Timer")
finestra.geometry("400x300")

etichetta = tk.Label(finestra, text="00:00", font=("Arial", 48))
etichetta.pack(pady=40)

frame_btn = tk.Frame(finestra)
frame_btn.pack(pady=40)

btn_start = tk.Button(frame_btn, text="Start", command=start)
btn_start.pack(side="left", padx=10)

btn_stop = tk.Button(frame_btn, text="Stop", command=stop)
btn_stop.pack(side="left", padx=10)

btn_reset = tk.Button(frame_btn, text="Reset", command=reset )
btn_reset.pack(side="left", padx=10)




aggiorna()
finestra.mainloop()
