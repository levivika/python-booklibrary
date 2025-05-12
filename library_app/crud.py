import json
class LibraryCRUD:
    def get_book_by_id(self, session, book_id):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        book = books.get(book_id)
        return book
    def book_list(self, session):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        return books

    def get_books_by_author(self, session, author):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        result = {}
        for book in books:
            if books[book]['author'].lower().find(author.lower()) != -1:
                result[book] = books[book]
        return result

    def get_books_by_title(self):
        pass


    def book_add(self, session, book_id, author, title, year):
        session.seek(0)
        data = json.loads(session.read())
        book_object ={
            book_id: {
                'author': author,
                'title': title,
                'year': year,
                'status': 'в наличии'
            }
        }
        data['library']['books'].update(book_object)
        session.seek(0)
        json.dump(data, session, indent =2, ensure_ascii=False)
        return True

crud = LibraryCRUD()














