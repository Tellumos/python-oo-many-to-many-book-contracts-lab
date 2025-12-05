class Author:
    all = []
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contracts for contracts in Contract.all if contracts.author == self]
    
    def books(self):
        return [contracts.book for contracts in Contract.all if contracts.author == self]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        sum = 0
        for royalty in [contracts.royalties for contracts in Contract.all if contracts.author == self]:
            sum += royalty
        return sum

class Book:
    all = []
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contracts for contracts in Contract.all if contracts.book == self]
    
    def authors(self):
        return [contracts.author for contracts in Contract.all if contracts.book == self]


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise ValueError("Not an instance of Author class")
        if isinstance(book, Book):
            self.book = book
        else:
            raise ValueError("Not an instance of Book class")
        if isinstance(date, str):
            self.date = date
        else:
            raise ValueError("Not a string")
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise ValueError("Not an integer")
        
        Contract.all.append(self)
     
    @classmethod
    def contracts_by_date(cls, date):
        return [contracts for contracts in cls.all if contracts.date == date]
