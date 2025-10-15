class Books:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f'Title: {self.title} | Author: {self.author} | Year: {self.year}'

book1 = Books("Harry Potter and the philosopher's stone","J.K. Rowling",'1997')
book2 = Books("Harry Potter and the chamber of secrets","J.K. Rowling",'1998')
book3 = Books('The Hobbit','J.R.R.','1937')

print()
print(book1.get_info())
print(book2.get_info())
print(book3.get_info())