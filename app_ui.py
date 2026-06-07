import tkinter as tk
from tkinter import messagebox
from models.task_manager import TaskManager
from ui.dashboard import Dashboard
from ui.themes import LIGHT_THEME, DARK_THEME


class TodoApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Advanced To-Do App")
        self.root.geometry("800x600")

        # Theme
        self.theme = LIGHT_THEME

        # Backend
        self.manager = TaskManager()

        self.build_ui()
        self.refresh()

    def build_ui(self):

        # Input box
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Add", command=self.add_task).grid(row=0, column=0)
        tk.Button(btn_frame, text="Delete", command=self.delete_task).grid(row=0, column=1)
        tk.Button(btn_frame, text="Complete", command=self.complete_task).grid(row=0, column=2)
        tk.Button(btn_frame, text="Edit", command=self.edit_task).grid(row=0, column=3)

        # Search
        self.search = tk.Entry(self.root)
        self.search.pack(pady=5)
        self.search.bind("<KeyRelease>", self.search_task)

        # Listbox
        self.listbox = tk.Listbox(self.root, width=80, height=20)
        self.listbox.pack(pady=10)

        # Dashboard
        self.dashboard = Dashboard(self.root)
        self.dashboard.pack(pady=10)

    def refresh(self):
        """Reload tasks in UI"""
        self.listbox.delete(0, tk.END)

        for t in self.manager.tasks:
            status = "✔" if t["completed"] else "✗"
            text = f'{status} [{t["priority"]}] {t["task"]} | {t["category"]}'
            self.listbox.insert(tk.END, text)

        total, completed, pending = self.manager.stats()
        self.dashboard.update(total, completed, pending)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.manager.add_task(task)
            self.entry.delete(0, tk.END)
            self.refresh()

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.manager.delete_task(index)
            self.refresh()
        except:
            messagebox.showerror("Error", "Select a task")

    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.manager.toggle_complete(index)
            self.refresh()
        except:
            messagebox.showerror("Error", "Select a task")

    def edit_task(self):
        try:
            index = self.listbox.curselection()[0]
            new_text = self.entry.get()
            if new_text:
                self.manager.update_task(index, new_text)
                self.refresh()
        except:
            messagebox.showerror("Error", "Select a task and enter new text")

    def search_task(self, event):
        query = self.search.get()

        results = self.manager.search_tasks(query)

        self.listbox.delete(0, tk.END)

        for t in results:
            status = "✔" if t["completed"] else "✗"
            text = f'{status} [{t["priority"]}] {t["task"]}'
            self.listbox.insert(tk.END, text)