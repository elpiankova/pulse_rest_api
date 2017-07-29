import requests


class PulseRestAPI:
    def __init__(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"

    def delete_book(self, book):
        response = requests.delete(self.base_url + '/books/{}/'.format(book.id))
        return response

    def create_book(self, book):
        response = requests.post(self.base_url + '/books/', data=book.dict())
        return response

    def modify_book(self, book):
        pass

    def get_books(self):
        pass

    def get_book(self, book):
        pass
