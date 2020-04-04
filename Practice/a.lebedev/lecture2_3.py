class Book:
    name = "Default book"
    year = 2020

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def set(self, name, year):
        self.name = name
        self.year = year


class Fantasy(Book):
    multipart = 1

    def set(self, name, year, multipart):
        self.name = name
        self.year = year
        self.multipart = multipart


lord = Fantasy("Властелин колец", 1937)
lord.set("Властелин колец", 1937, 3)
print(lord.name, lord.year, lord.multipart)

diesouls = Book("Мертвые души", 1842)
print(diesouls.name, diesouls.year)
