import pytest
from models.book import Book
from pulse_rest_api import PulseRestAPI


@pytest.fixture(scope="session")
def app():
    return PulseRestAPI()

books = [
    {"title": "sfs fsedf", "author": "sdfsd sdvfsd"},
    {"title": "12312", "author": "1231"},
    {"title": "выапвыа", "author": "sdfsd sdvfsd"}
]

books_repr = [str(book) for book in books]


@pytest.fixture(params=books, ids=books_repr)
def book(request, app):
    book_fixture = Book(title=request.param["title"], author=request.param["author"])
    yield book_fixture
    app.delete_book(book_fixture)
