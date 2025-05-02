import tkinter as tk
from static.package.database import DataBS
from static.package.Configuration import config,Padronizar
from selenium import webdriver


root = tk.Tk()
root.geometry(config.geometria)
root.configure(background=config.background)
MyApp = Padronizar(root)

MyApp.LabelTk("Lista de APIS",config.background,10,20,config.font)
Lb = tk.Listbox(root,background=config.background,fg=config.font,width=500)


for i in range(0,len(DataBS(escolha="select",databaseName="Apis_DB",valor1="url"))):
    Lb.insert(i, str(DataBS(escolha="select",databaseName="Apis_DB",valor1="url")[i][0]))
    Lb.pack()

def OpenApi(conteudo):
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\Users\ronal\AppData\Local\Google\Chrome\User Data")
    driver = webdriver.Chrome(options=options)

    driver.get(conteudo)

def get_selected_items():
    selected_indices = Lb.curselection()
    selected_items = [Lb.get(i) for i in selected_indices]
    Select_Itens = str(DataBS(escolha="selectEspecificar",databaseName="Apis_DB",valor1="apis_urls",valor2="url",valor3=f"{selected_items[0]}")[0])
    Select_Itens = Select_Itens.replace("\\","").replace("'","").replace('"',"").replace("([","").replace(")]","").split(",")


    for j in range(len(Select_Itens)):
        tk.Button(root, text=Select_Itens[j], background="#2f2f2f", fg="white", font=("Helvetica", 10),cursor="hand2",padx=10, pady=10,command=lambda j=j: OpenApi(Select_Itens[j])).pack()

MyApp.ButtonTK("Listar Urls",10,10,get_selected_items)

MyApp.LabelTk("",config.background,10,20,config.font)

root.mainloop()