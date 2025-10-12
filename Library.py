class LibraryItem:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        
    def get_title(self):
        return self.title
    
    def get_year(self):
        return self.year
    
class Book(LibraryItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author
        
    def get_author(self):
        return self.author

class DVD(LibraryItem):
    def __init__(self, title, year, duration):
        super().__init__(title, year)
        self.duration = duration
        
    def get_duration(self):
        return self.duration
    
            
        