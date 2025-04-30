import tkinter as tk
from static.Config import config

root = tk.Tk()
root.geometry("500x500")
root.configure(background="#252563")

Rota_dicionario = [
    ["Adicionar","add"],
    ["Api Lista","api"],
    ["Automação Lista","automation"]
]

for i in range(3):
    tk.Button(root,text=f"{Rota_dicionario[i][0]}",command=lambda i=i:config(root=root,link="Red",Rota=f"{Rota_dicionario[i][1]}").btnLink()).pack()

root.mainloop()