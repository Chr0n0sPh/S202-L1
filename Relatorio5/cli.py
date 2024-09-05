
class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class BookCLI(SimpleCLI):
    def __init__(self, book_model):
        super().__init__()
        self.book_model = book_model
        self.add_command("create", self.create_book)
        self.add_command("read", self.read_book)
        self.add_command("update", self.update_book)
        self.add_command("delete", self.delete_book)

    def create_book(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano do livro:"))
        preco = float(input("Digite o preco do livro: "))
        self.book_model.create_book(titulo, autor, ano, preco)

    def read_book(self):
        id = input("Informe o id: ")
        book = self.book_model.read_book_by_id(id)
        if book:
            print(f"Titulo: {book['titulo']}")
            print(f"Autor: {book['autor']}")
            print(f"Ano: {book['ano']}")
            print(f"Preço: {book['preco']}")

    def update_book(self):
        id = input("Informe o id: ")
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano do livro:"))
        preco = float(input("Digite o preco do livro: "))
        self.book_model.update_book(id, titulo, autor, ano, preco)

    def delete_book(self):
        id = input("Informe o id: ")
        self.book_model.delete_book(id)
        
    def run(self):
        print("Bem--vindo ao LivroCLI!")
        print("Comandos Disponíveis: create, read, update, delete, quit")
        super().run()
        
