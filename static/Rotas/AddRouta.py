import tkinter as tk

root = tk.Tk()
root.geometry("500x600")
root.configure(background="#252525")

tk.Label(root,text="Olá,Mundo").pack()

root.mainloop()