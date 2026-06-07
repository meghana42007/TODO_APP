import tkinter as tk


class Dashboard(tk.Frame):
    """
    Displays task statistics like:
    - Total tasks
    - Completed
    - Pending
    """

    def __init__(self, parent):
        super().__init__(parent)

        self.total_label = tk.Label(self, font=("Arial", 12))
        self.completed_label = tk.Label(self, font=("Arial", 12))
        self.pending_label = tk.Label(self, font=("Arial", 12))

        self.total_label.pack()
        self.completed_label.pack()
        self.pending_label.pack()

    def update(self, total, completed, pending):
        """Update dashboard values"""
        self.total_label.config(text=f"Total Tasks: {total}")
        self.completed_label.config(text=f"Completed: {completed}")
        self.pending_label.config(text=f"Pending: {pending}")