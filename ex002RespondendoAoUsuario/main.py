from name import Name
from answer import Answer

answer = Answer()

name = Name(
    input('Digite o seu nome: ')
)

answer.handleAnswer(name)
