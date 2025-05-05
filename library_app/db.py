import os
import json

class LibraryDB:
    def __init__(self, dbname):
        if os.path.exists(dbname):
            self.db_file = open(dbname, 'r+', encoding='UTF-8') #for reading
        else:
            self.db_file = open(dbname, 'w+', encoding='utf-8')
            initial_data = {
                'library':
                    {
                        'books':
                            {

                            }
                    }
            }
            json.dump(initial_data, self.db_file, indent=2)
    def session_maker(self):
        return self.db_file

Session = LibraryDB(dbname='books.json')