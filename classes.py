class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    # Getter and Setter methods
    
    def get_title(self):
        return self.title
    
    # Setter method for title
    def set_title(self, title):
        self.title = title
    
    # Getter and Setter for author
    def get_author(self):
        return self.author
    
    # Setter method for author
    def set_author(self, author):
        self.author = author
      
    # Getter and Setter for price  
    def get_price(self):
        return self.price
    
    # Setter method for price
    def set_price(self, price):
        self.price = price
        
class Novel(Book):
    def __init__(self, title, author, price, category):
        super().__init__(title, author, price)
        self.category = category
    
    def get_category(self):
        return self.category
    
    def set_category(self, category):
        self.category = category
    
novel1 = Novel('', '', 0, 'Fiction')

novel1.set_title = ("Harry Potter")
novel1.set_author = ("J.K. Rawling")
novel1.set_price = (450)
novel1.set_category = ("Fiction")

print("title:", novel1.get_title())
print('author:', novel1.get_author())
print("price:", novel1.get_price())
print("category:", novel1.get_category())