import tkinter as tk
from static.package.Configuration import config,Padronizar

root = tk.Tk()
root.geometry(config.geometria)
root.configure(background=config.background)

Valor = tk.StringVar()
Listbox = tk.Listbox(root,background=config.background,fg=config.font,highlightbackground=config.background,borderwidth=0)

Adicionar = Padronizar(root)
Automation = Padronizar(root)

# Adicionar APIS
Adicionar.LabelTk("Adicionar uma API",config.background,7,10,"white")
Adicionar.InputTk("Adicionar uma URL: ",10,10)
Adicionar.ButtonTK_Return("Enviar URL",10,10)


# Adicionar Automatizar
Adicionar.LabelTk("Adicionar uma Automação",config.background,7,10,"white")
Automation.InputTk("Adicionar uma URL: ",10,10)
Automation.InputTk("Quantidade de conteudo: ",10,10)
Automation.InputTk("Qual o tipo da Url: ",10,10)
Automation.ButtonTK_Return("Enviar URL",10,10)

root.mainloop()