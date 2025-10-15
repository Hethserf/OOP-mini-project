class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def __str__(self):
        status = "✅ Done" if self.done else "🕓 Not done"
        return f"{self.title} - {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add(self, title):
        """افزودن تسک جدید به لیست"""
        task = Task(title)
        self.tasks.append(task)
        print(f"✅ Task '{title}' added.")

    def mark_done(self, title):
        """علامت زدن تسک به عنوان انجام‌شده"""
        for task in self.tasks:
            if task.title == title:
                task.done = True
                print(f"🎯 Task '{title}' marked as done.")
                return
        print(f"⚠️ Task '{title}' not found!")

    def show_tasks(self):
        """نمایش تمام تسک‌ها"""
        if not self.tasks:
            print("📭 No tasks yet.")
            return

        print("📝 To-Do List:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
            
todo = ToDoList()
todo.add("Study Python")
todo.add("Go for a walk")
todo.show_tasks()

todo.mark_done("Study Python")
todo.show_tasks()
