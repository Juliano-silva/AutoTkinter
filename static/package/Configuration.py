import tkinter as tk

class config:
    def __init__(self,root,link:str,Rota:str):
        self.link = link
        self.root = root
        self.Rota = Rota

    geometria = ("600x600")
    background = "#252525"
    font = "white"

    def btnLink(self):
        self.root.destroy()
        if(self.Rota == "add"):
            from static.Rotas import AddRouta
        elif(self.Rota == "api"):
            from static.Rotas import ApiRouta
        elif(self.Rota == "automation"):   
            from static.Rotas import AutomationRouta


class Padronizar:
    def __init__(self,root):
        self.root = root
        self.entries = []

    def ButtonTK(self,text:str,pady:int,padx:int,commad) -> None:
        tk.Button(self.root, text=text, background="#2f2f2f", fg="white", font=("Helvetica", 10),cursor="hand2",padx=padx, pady=pady,command=lambda : commad()).pack()
        return True;

    def LabelTk(self,text:str,bk:str,pady:int,padx:int,fg:str):
        tk.Label(self.root, text=text, background=bk, fg=fg, font=("Helvetica", 13),
                 cursor="hand2", padx=padx, pady=pady).pack()
        return True;

    def InputTk(self, text: str, pady: int, padx: int):
        entry = tk.Entry(self.root, background="grey", fg="white", borderwidth=5, width=25)
        entry.pack(padx=padx, pady=pady)

        entry.placeholder_text = text
        self.set_placeholder(entry)

        entry.bind("<FocusIn>", lambda e: self.remove_placeholder(entry))
        entry.bind("<FocusOut>", lambda e: self.set_placeholder(entry))

        self.entries.append(entry)  # Add entry to the list

    def set_placeholder(self, entry):
        if not entry.get():
            entry.insert(0, entry.placeholder_text)
            entry.config(fg='white')

    def remove_placeholder(self, entry):
        if entry.get() == entry.placeholder_text:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def ButtonTK_Return(self, text: str, pady: int, padx: int) -> None:
        button = tk.Button(self.root, text=text, background="#2f2f2f", fg="white", font=("Helvetica", 10),
                           cursor="hand2",
                           padx=padx, pady=pady, command=self.get_input)
        button.pack()

    def get_input(self):
        user_inputs = [entry.get() for entry in self.entries]
        return user_inputs
