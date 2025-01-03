import diary


class User:
    def __init__ (self, id, name, goals, reminders, status, diarys):
        self.id = id
        self.name = name
        self.goals = goals
        self.reminders = reminders
        self.status = status
        self.diarys = diary.Diary()






