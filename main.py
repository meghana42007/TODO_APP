import tkinter as tk
from ui.app_ui import TodoApp

# Create main window
root = tk.Tk()

# Run app
app = TodoApp(root)

root.mainloop()