import tkinter as tk
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()
    with open(filepath, 'r') as f:
        content = f.read()
    wEditor.insert('1.0', content)

def save_file():
    filepath = filedialog.asksaveasfilename()
    with open(filepath, 'w') as f:
        f.write(wEditor.get('1.0', 'end'))

window = tk.Tk()
window.title("Notepad do Paraguai")

formButton = tk.Frame(window, relief=tk.RAISED, bd=2)
formButton.grid(row=0, column=0, sticky="ns")
formButton.columnconfigure(0, weight=1)
formButton.columnconfigure(1, weight=1)

btnOpen = tk.Button(formButton, text="Abrir", command=open_file)
btnOpen.grid(row=0, column=0, sticky="ew", padx=1, pady=1)

btnSalvar = tk.Button(formButton, text="Salvar", command=save_file)
btnSalvar.grid(row=0, column=1, sticky="ew", padx=1, pady=1)


wEditor = tk.Text(window)
wEditor.grid(row=0, column=1, sticky="nsew")

window.grid_columnconfigure(1, minsize = 90, weight = 1)
window.grid_rowconfigure(0, minsize = 90, weight = 1)

window.mainloop()
