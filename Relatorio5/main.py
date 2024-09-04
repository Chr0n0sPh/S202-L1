from database import Database
from writeAJson import writeAJson
from bookModel import BookModel
from cli import PersonCLI

db = Database(database="Biblioteca", collection="Livros")
bookmodel = BookModel(database=db)

# bookmodel.create_book("Harry Potter","J.K. Rowling",1994,50.00)

bookmodel.read_book_by_id("66d83bfe74e8fac43ddb79bb")

# personCLI = PersonCLI(personModel)
# personCLI.run()
