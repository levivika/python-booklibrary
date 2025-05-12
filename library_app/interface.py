class LibraryInterface:
    def __init__(self, library):
         self.library = library
         self.user_action = None
         self.text_menu = ("Welcome to library\n"
                           "Choose your menu item (0-5)\n"
                           "1. See al books\n"
                           "2. Add a book\n"
                           "3. Show a quantity of books \n"
                           "4. Search a quantity of books \n"
                           "5. Search book by author \n"
                           "----------------------------\n"
                           "0. Leave the program"

                           )


    def print_main_menu(self):
        print(self.text_menu)
        self.user_action = input('>>> ')
        self.process_main_menu()

    def process_main_menu(self):
        if self.user_action == "1":
            print("Func 'all books'")
        elif self.user_action == '2':
            print("Func 'Add a book'")
        else:
            print('Choose your menu item')
    def process_main_menu(self):
        while True:
            match self.user_action:
                case '1':
                    books = self.library.book_list()
                    if books:
                        print('list of the books: ')
                        self.print_books(books)
                        self.print_main_menu()
                    else:
                        print('No books')
                    self.print_main_menu()
                case '2':
                    self.add_book()
                    self.print_main_menu()
                case '5':
                    self.find_books_by_author()
                    self.print_main_menu()
                case '4':
                    pass

    def print_books(self, books):
        for book in books:
            print(f'ID - {book}')
            print(f'author - {books[book]['author']}')
            print(f'name - {books[book]['title']}')
            print(f'year - {books[book]['year']}')
            print(f'status - {books[book]['status']}')
            print('------------')

    def add_book(self):
        author = input('author: ')
        title = input('title: ')
        year = input('year: ')
        try:
            self.library.book_add(author=author, title=title, year=year)
            print('Book added success')
        except Exception as err:
            print(f'error - {err}')

    def find_books_by_author(self):
        author = input('Write author of book:\n >>>')
        books = self.library.find_book_by_author(author=author)
        if books:
            self.print_books(books)
        else:
            print('nothing found')



















