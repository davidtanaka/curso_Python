# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template
import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula183.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='Davi',
    valor=converte_para_brl(1_234),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

# texto = '''
# Prezado(a) $nome,

# Informamos que sua mensalidade será cobrada no valor ${valor} no dia $data. Caso
# deseje cancelar o serviço, entre em contato com $empresa pelo telefone $telefone.

# Atenciosamente

# ${empresa}
# Abraços.
# '''

# Poderia criar meu demilitador. Mas não é recomendado
# class MyTemplate(string.Template):
#     delimiter = '%'

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))