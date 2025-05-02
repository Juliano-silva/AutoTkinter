import tkinter as tk
from static.package.Configuration import config


root = tk.Tk()

root.title = "Automação"
root.geometry(config.geometria)
root.configure(background=config.background)



root.mainloop()