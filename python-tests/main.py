from calculadora import soma

print(soma(2, 4))
print(soma(12, -10))
print(soma(11, 9))

try:
    print(soma('12', -1)) # type: ignore
except AssertionError as e:
    print(f'Conta ínvalida: {e}')
