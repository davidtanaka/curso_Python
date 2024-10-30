"""
O Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto global de acesso para a mesma.

When discussing which patterns to drop, we found
that we still love them all.
(Not really—I'm in favor of dropping Singleton.
Its use is almost always a design smell.)
- Erich Gamma, em entrevista para informIT
http://www.informit.com/articles/article.aspx?p=1404056
"""

class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # O init será chamado todas as vezes
        self.tema = 'Escuro'
        self.font = '20px'

if __name__ == '__main__':
    appsettins1 = AppSettings()
    appsettins1.tema = 'Claro'
    print(appsettins1.tema)

    appsettins2 = AppSettings()
    print(appsettins2.tema)