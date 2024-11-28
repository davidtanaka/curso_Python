from re import findall
from pprint import pprint

text = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
'''

pattern = findall(r'<([a-z]{1,3})>(.*?)<\/\1>', text)

# Retorna: ['Frase 1', 'Eita', 'Qualquer frase', '1']
content = [content for _, content in pattern]

# pprint(content)


# Exercício 2 - Extrair Endereços IPs:
# Escreva uma função extrair_ips(texto) que usa uma regex
# para capturar todos os endereços IP válidos
# (formato xxx.xxx.xxx.xxx, onde cada segmento é de 0 a 255).

def extract_ips(ip: str) -> list:
    # Regex corrigida para capturar IPs, ignorando delimitadores como vírgulas
    pattern = findall(r'\b((?:[0-9]{1,3}\.){3}[0-9]{1,3})(?=\s|,|$)', ip)
    # Validando intervalo de 0 a 255
    valid_ips = [addr for addr in pattern if all(0 <= int(octet) <= 255 for octet in addr.split('.'))]
    return valid_ips

text = "Servidores: 192.168.0.1, 10.0.0.255, 256.100.50.25"  
# Deve retornar: ['192.168.0.1', '10.0.0.255']
solution = extract_ips(text)
print(solution)
