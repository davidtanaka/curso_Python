def singleton(the_class):
    instances = {}  # Dicionário para armazenar a única instância de cada classe.

    def get_class(*args, **kwargs):
        # Verifica se a classe já foi instanciada e está no dicionário `instances`
        if the_class not in instances:
            # Se não, cria uma nova instância e a armazena em `instances`
            instances[the_class] = the_class(*args, **kwargs)
        # Retorna a instância existente (ou recém-criada)
        return instances[the_class]
    
    return get_class


@singleton
class AppSettings:
    def __init__(self):
        self.tema = 'Escuro'
        self.font = '20px'

if __name__ == '__main__':
    appsettins1 = AppSettings()
    appsettins1.tema = 'Claro'
    print(appsettins1.tema)

    appsettins2 = AppSettings()
    print(appsettins2.tema)