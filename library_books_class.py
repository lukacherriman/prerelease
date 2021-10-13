class StockItems:
    def __init__(self, title, on_loan, date_acquired):
        self._title = title
        self._on_loan = on_loan
        self._date_acquired = date_acquired


class LibraryBooks(StockItems):
    def __init__(self, author, isbn):
        super.__init__()
        self._author = author
        self._ISBN = isbn

    def set_loan(self):
        return

    def display_details(self):
        return

    def return_loan(self):
        return

    def get_ISBN(self):
        return self._ISBN

    def get_author(self):
        return self._author


class CD(StockItems):
    def __init__(self, artist, ):
        super.__init__(title, on_loan, date_acquired)
        self._artist = artist


jumble = CD("Luka")


