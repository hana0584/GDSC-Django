from library import Library

library = Library()

library.addBook("Book1", "Sydney sheldon", "123", True)
library.addBook("Book2", "Sydney sheldon", "123", True)
library.addBook("Book3", "Sydney sheldon", "123", True)
library.addBook("Book4", "Sydney sheldon", "123", True)

library.registerUser(12, "www", [])
library.registerUser(13, "xxx", [])
library.registerUser(14, "yyy", [])
library.registerUser(11, "zzz", [])

library.handleTransactionBorrow(11, "Book1")
library.handleTransactionBorrow(12, "Book2")
library.handleTransactionBorrow(13, "Book1")
library.handleTransactionBorrow(11, "Book3")

library.getLibraryInformation()
library.getUserInformation()

library.handleTransactionReturn(11, "Book1")
library.handleTransactionReturn(12, "Book2")
library.handleTransactionReturn(13, "Book1")
library.handleTransactionReturn(11, "Book3")

library.getLibraryInformation()
library.getUserInformation()
library.displayTransactionDetail()
