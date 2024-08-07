#Criando a Clase Aula
class Aula:
    aluno = []

    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = self.aluno

    def adicionar_aluno(self, nome):
        self.alunos.append(nome)

    def listar_preseca(self):
        print(f"Presença na aula sobre {self.assunto}, ministrada pelo {self.professor.nome}:")
        for aluno in self.alunos:
            aluno.presenca()

