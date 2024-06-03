# try, except, else e finally
# a = 18
# b = 0
# c = a / b

try:
     a = 18
     b = 0
     # print(b[0])
     print('Linha 1'[1000])
     c = a / b
     print('Linha 2')
except ZeroDivisionError as e:
     print(e.__class__.__name__)
     print(e)
except NameError:
     print('ERRO: B não esta defenido')
except(TypeError, IndexError) as error:
     print('ERRO: TypeError ou indexerror')
     print('Msg: ', error)
     print('Nome:', error.__class__.__name__)
except Exception:
     print('ERRO DESCONHECIDO')

print()