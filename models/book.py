class Book:
    def __init__(self, title=None, author=None, id=None):
        self.title = title
        self.author = author
        self.id = id

    def __str__(self):
        return "<Book: {}, author: {}>".format(self.title, self.author)

    def dict(self):
        full_dict = self.__dict__
        return {key: full_dict[key]
                for key in full_dict
                if full_dict[key] is not None}


if __name__ == "__main__":
    b = Book("Some name", author="sfd", id=12)
    print(b.dict())
