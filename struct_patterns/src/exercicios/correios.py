# Função `verificar_status_pedido` que recebe uma string representando o estado atual de um pedido.

# Utiliza `match` para verificar o valor de `status` e retorna uma mensagem correspondente.

# Casos possíveis:
# - "pendente": Pedido ainda não foi processado.
# - "em transporte": Pedido está a caminho.
# - "entregue": Pedido foi entregue ao destinatário.
# - "cancelado": Pedido foi cancelado.
# - Qualquer outro valor: "Status desconhecido".

# O `_` no `match` atua como um caso padrão, capturando valores não reconhecidos.

def verificar_status_pedido(local: str) -> str:
    match local.lower():
        case 'pendente':
            return 'Seu pedido ainda está pendente'
        case 'em transporte':
            return 'Seu pedido esta sendo transportado'
        case 'entregue':
            return 'Pedido foi entregue ao destinatário.'
        case 'cancelando':
            return 'Seu pedido foi cancelado'
        case _:
            return 'Pedido desconhecido'

# Todas as letras aleatoriamente maiuscúlas para testar o lower
print(verificar_status_pedido('pendente'))
print(verificar_status_pedido('EM TRANSPORTE'))
print(verificar_status_pedido('entRegUe'))
print(verificar_status_pedido('caNCelaNdo'))
