from library_app.db import Session

def main():
    session = Session.session_maker()

if __name__ == '__main__':
    main()