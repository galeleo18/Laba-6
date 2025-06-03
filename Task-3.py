class Task:
    def __init__(self, DateStart, DateEnd, Description):
        self.DateStart = DateStart
        self.DateEnd = DateEnd
        self.Description = Description

tasks = [
    Task("01-05-2025", "05-05-2025", "Учёба"),
    Task("07-05-2025", "12-05-2025", "Учёба"),
    Task("14-05-2025", "19-05-2025", "Учёба"),
    Task("21-05-2025", "26-05-2025", "Учёба"),
    Task("28-05-2025", "28-05-2025", "Отдых")
]

latest_task = tasks[0]
for t in tasks:
    if t.DateEnd > latest_task.DateEnd:
        latest_task = t

print(f"Последняя задача: {latest_task.Description}, заканчивается {latest_task.DateEnd}")