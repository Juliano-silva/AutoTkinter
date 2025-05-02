import tkinter as tk
from static.package.database import DataBS
from static.package.Configuration import config
from selenium import webdriver


root = tk.Tk()
root.geometry(config.geometria)
root.configure(background=config.background)

Tabela_apis_text = tk.Label(root, text="Tabela de Apis", background="#252525", fg="white").pack()

Escolha = tk.Label(root, text="", background="#252525", fg="white")

Btn_lista = []

def limpar_botoes():
    """Remove todos os botões existentes da lista e da interface."""
    for botao in Btn_lista:
        botao.destroy()
    Btn_lista.clear()  # Limpa a lista de botões

def openAPI(conteudo):
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\Users\ronal\AppData\Local\Google\Chrome\User Data")
    driver = webdriver.Chrome(options=options)

    driver.get(conteudo)

def Abrir(text, i=None):
    ApiRef = str(DataBS("selectESC","apis_urls",25)[0]).replace("\\","").replace("'","").replace('"',"").replace("([","").replace(")]","").split(",")
    Escolha.configure(text=f"{text[0]}")
    limpar_botoes()  # Limpa os botões antes de criar novos

    Escolha.pack()

    for i in range(len(ApiRef)):
        botao = tk.Button(root, text=ApiRef[i], background="#252525", fg="white",command=lambda i=i: openAPI(ApiRef[i])).pack()
        Btn_lista.append(botao)  # Adiciona o botão à lista

for i in range(2):
    Tabela_apis = tk.Button(root, text=DataBS("select", "url", None)[i], padx=200, pady=50,command=lambda i=i: Abrir(DataBS("select", "url", None)[i])).pack()
root.mainloop()