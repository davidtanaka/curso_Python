# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MyError(Exception):
     ...


class OtherError(Exception):
     ...

def raising():
     exception_ = MyError('Error f928')
     exception_.add_note('Your error is this')
     raise exception_



try:
     raising()
except (MyError, ZeroDivisionError) as error:
     print(error.__class__.__name__)
     print(error.args)
     print()
     exception_ = OtherError('Throwing the error again')
     raise exception_ from error