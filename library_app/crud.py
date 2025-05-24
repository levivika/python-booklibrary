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

    def show_the_quantity_books(self, session):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        result = len(books)
        return result



    def get_book_by_title(self, session, title):
        session.seek(0)
        data=json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        result={}
        for book in books:
            if books[book]['title'].lower().find(title.lower()) != -1:
                result[book] = books[book]
        return result

    def get_books_by_author(self, session, author):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        result = {}
        for book in books:
            if books[book]['author'].lower().find(author.lower()) != -1:
                result[book] = books[book]
        return result



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

    def show_the_status(self, session, title):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})

        for book_id, book_data in books.items():
            if book_data['title'].lower() == title.lower():
                return book_data.get('status', 'Статус не указан')
        return 'Книга не найдена'






crud = LibraryCRUD()














