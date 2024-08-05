from Professor import Professor
from Aluno import Aluno
from Aula import Aula

professor = Professor('Jonas')

aluno1 = Aluno('Paulo Pivoto')
aluno2 = Aluno("João")

aula = Aula(professor, "Banco de Dados 2")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.listar_preseca()





