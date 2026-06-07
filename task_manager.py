import json
import os
from datetime import datetime


class TaskManager:
    """
    Handles all backend logic:
    - Add / Edit / Delete tasks
    - Save & Load JSON
    - Manage task data structure
    """

    def __init__(self, file_path="data/tasks.json"):
        self.file_path = file_path
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    self.tasks = json.load(f)
            except:
                self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.file_path, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task, priority="Medium", category="General", due_date=""):
        """Add a new task"""
        self.tasks.append({
            "task": task,
            "priority": priority,
            "category": category,
            "due_date": due_date,
            "completed": False,
            "created_at": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        })
        self.save_tasks()

    def delete_task(self, index):
        """Delete task by index"""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def update_task(self, index, new_task):
        """Edit task text"""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["task"] = new_task
            self.save_tasks()

    def toggle_complete(self, index):
        """Mark task as complete/incomplete"""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.save_tasks()

    def search_tasks(self, query):
        """Search tasks by keyword"""
        return [
            t for t in self.tasks
            if query.lower() in t["task"].lower()
        ]

    def stats(self):
        """Return dashboard stats"""
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t["completed"]])
        pending = total - completed

        return total, completed, pending