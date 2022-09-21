import datetime
import sys

last_id = 0

class Diary:
    def __init__(self, memo, tags=" "):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
    
    def match(self, filter):
        return  filter in self.memo or self.tags
    

class Diarybook:
    def __init__(self):
        self.diaries = []
    
    def new_diary(self, memo, tags=""):
        self.diaries.append(Diary(memo, tags))
    
    def search_diary(self, filter):
        return [diary for diary in self.diaries if diary.match(filter)]

class Menu:
    def __init__(self):
        self.diarybook = Diarybook()
        self.choices = {
            "1" : self.show_diaries,
            "2" : self.add_diary,
            "3" : self.search_diaries,
            "4" : self.quit
        }
    
    def display_menu(self):
        print("""
            Notebook Management
            1. Show diaries
            2. Add diary 
            3. Search diaries
            4. Quit
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option : ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(choice + "is not a valid choice")
    
    def show_diaries(self, diaries=None):
        if not diaries:
            diaries = self.diarybook.diaries
        for diary in diaries:
            print("{0}".format(diary.memo))

    def add_diary(self):
        memo = input("Enter a memo :  ")
        self.diarybook.new_diary(memo)
        print("Notes has been added to the diary")
    
    def search_diaries(self):
        filter = input("Search for : ")
        diaries = self.diarybook.search_diary(filter)
        self.show_diaries(diaries)

    
    def quit(self):
        print("Thanks for using diary book notes, see u :)")
        sys.exit(0)

Menu().run()

# d1 = Diary("so grateful for today :D")
# print(d1.memo, d1.id, d1.creation_date)