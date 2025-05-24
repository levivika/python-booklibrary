import uuid
from wsgiref.validate import validator
from .db import Session
from .crud import crud

class LibraryApp:
    '''
    основная бизнес логика приложения
    '''
    def __init__(self, session: Session):
        self.session = session

    def book_add(self, title, author, year):
        book_id = uuid.uuid4().hex[:68]
        title = title
        author = author
        year = year
        return crud.book_add(self.session, book_id, title, author, year)

    def book_list(self):
        books = crud.book_list(self.session)
        return books

    #def book_delete(self, book_id):
        #book_id = validators.validate_book_id(self.session, book_id)
        #crud.get_book_by_id(self.session, book_id)
        #crud.book_delete(self.session, book_id)

    #def get_book_status(self, book_id):
        #book_id = validators.validate_book_id(self.session, book_id)
        # book_status = crud.get_book_status(self.session, book_id)
        #return book_status

    def find_book_by_author(self, author):
        books = crud.get_books_by_author(session = self.session, author = author)
        return books
    def get_book_by_title(self, title):
        books = crud.get_book_by_title(session = self.session, title = title)
        return books

    def show_the_quantity_books(self):
        books = crud.show_the_quantity_books(self.session)
        return books

    def show_the_status(self, title):
        return crud.show_the_status(self.session, title)