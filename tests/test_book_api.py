def test_book_creation(app, book):
    response = app.create_book(book)
    # Verification
    assert response.status_code == 201
    response_body = response.json()
    assert 'id' in response_body
    book.id = response_body["id"]
    assert book.dict() == response_body
    # assert book.dict() == app.get_book(book).json()
    # assert book.dict() in app.get_books().json()


def test_book_modification(app, book):
    assert True

