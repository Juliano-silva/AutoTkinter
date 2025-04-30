class config:
    def __init__(self,root,link:str,Rota:str):
        self.link = link
        self.root = root
        self.Rota = Rota

    def btnLink(self):
        self.root.destroy()
        if(self.Rota == "add"):
            from static.Rotas import AddRouta
        elif(self.Rota == "api"):
            from static.Rotas import ApiRouta
        elif(self.Rota == "automation"):   
            from static.Rotas import AutomationRouta