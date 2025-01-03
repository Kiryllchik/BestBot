import datetime

class Diary():
    def __init__(self):
        self.records = {}
    
    def add_diary_entry(self, date, note):
        if date not in self.records: #create new data key if there is no such date in records dict
            self.records[date] = [] 
        self.records[date].append(note) #add the note to exact date
            
    def get_diary_entry(self, date):
        if date in self.records:
            print(self.records[date])
        

    
