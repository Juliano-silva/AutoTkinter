
import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Simple Table Example")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=("Name", "Age", "City"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("City", text="City")

# Insert some sample data
data = [
    ("Alice", 30, "New York"),
    ("Bob", 25, "Los Angeles"),
    ("Charlie", 35, "Chicago"),
]

for item in data:
    tree.insert("", "end", values=item)

# Pack the Treeview widget
tree.pack(expand=True, fill='both')

# Start the Tkinter event loop
root.mainloop()
