# Essa funcão deverá calcular o desconto dos produtos:
# com base nos parâmetros recebidos, como nivel do usuario

def calcular_desconto(infs: dict):
    desconto_regular = 5
    desconto_premium = 10
    desconto_vip = 15

    match infs:
        case {'tipo_usuario': 'Regular', 'valor_compra': valor_compra} if isinstance(valor_compra, (int, float)):
            valor_final = valor_compra * (1 - desconto_regular / 100)
            return f'Sua compra com o tipo de usuário "{infs["tipo_usuario"]}" e o valor final é de R$ {valor_final:.2f}'
        
        case {'tipo_usuario': 'Premium', 'valor_compra': valor_compra} if isinstance(valor_compra, (int, float)):
            valor_final = valor_compra * (1 - desconto_premium / 100)
            return f'Sua compra com o tipo de usuário "{infs["tipo_usuario"]}" e o valor final é de R$ {valor_final:.2f}'
        
        case {'tipo_usuario': 'Vip', 'valor_compra': valor_compra} if isinstance(valor_compra, (int, float)):
            valor_final = valor_compra * (1 - desconto_vip / 100)
            return f'Sua compra com o tipo de usuário "{infs["tipo_usuario"]}" e o valor final é de R$ {valor_final:.2f}'
        
        case _:
            return 'Tipo de usuário inválido ou valor de compra inválido.'

# Testes
print(calcular_desconto({'tipo_usuario': 'Regular', 'valor_compra': 150.15}))        
print(calcular_desconto({'tipo_usuario': 'Premium', 'valor_compra': 150.15}))        
print(calcular_desconto({'tipo_usuario': 'Vip', 'valor_compra': 150.15}))        
print(calcular_desconto({'tipo_usuario': 'Invalido', 'valor_compra': 150.15}))  # Caso inválido
      