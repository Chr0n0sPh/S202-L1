#Criando a Classe Professor
class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self):
        assunto = input("Digite um assunto: ")
        print(f"O Professor {self.nome} está ministrando uma aula sobre {assunto}")