from abc import ABC, abstractmethod

# Define a interface para objetos observáveis
class IObservable(ABC):
    """ Interface para objetos que podem ser observados. """

    @property
    @abstractmethod
    def state(self): 
        pass  # Método para obter o estado atual do objeto

    @abstractmethod
    def add_observer(self, observer: 'IObserver') -> None: 
        pass  # Método para adicionar um observador

    @abstractmethod
    def remove_observer(self, observer: 'IObserver') -> None: 
        pass  # Método para remover um observador

    @abstractmethod
    def notify_observers(self) -> None: 
        pass  # Método para notificar todos os observadores

# Implementação concreta de uma estação meteorológica observável
class WeatherStation(IObservable):
    """ Estação meteorológica que pode ser observada por dispositivos. """

    def __init__(self) -> None:
        self._observers: list[IObserver] = []  # Lista de observadores
        self._state: dict = {}  # Estado atual da estação

    @property
    def state(self) -> dict:
        return self._state  # Retorna o estado atual

    @state.setter
    def state(self, state_update: dict) -> None:
        # Atualiza o estado se houver mudanças e notifica observadores
        new_state: dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self) -> None:
        # Reseta o estado e notifica observadores
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: 'IObserver') -> None:
        # Adiciona um observador à lista
        self._observers.append(observer)

    def remove_observer(self, observer: 'IObserver') -> None:
        # Remove um observador se ele estiver na lista
        if observer not in self._observers:
            return
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        # Notifica todos os observadores sobre uma mudança no estado
        for observer in self._observers:
            observer.update()
        print()

# Define a interface para objetos que observam o WeatherStation
class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: 
        pass  # Método chamado quando o observável é atualizado

# Implementação de um observador representando um Smartphone
class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name  # Nome do dispositivo
        self.observable = observable  # Objeto que o smartphone observa

    def update(self) -> None:
        # Ação tomada quando o estado do observable é atualizado
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} '
              f'acabou de ser atualizado => {self.observable.state}')

# Implementação de um observador representando um Notebook
class Notebook(IObserver):
    def __init__(self, observable: IObservable) -> None:
        self.observable = observable  # Objeto observado pelo notebook

    def show(self) -> None:
        # Exibe o estado atual com uma mensagem personalizada
        state = self.observable.state
        print('Sou o note e vou fazer outra coisa com esses dados', state)

    def update(self) -> None:
        # Chama o método `show` quando o estado do observable é atualizado
        self.show()

# Classe fachada para simplificar a interação com a estação meteorológica e dispositivos
class WeatherStationFacade:
    def __init__(self) -> None:
        # Cria instâncias de WeatherStation e dispositivos observadores
        self.weather_station = WeatherStation()

        self.smartphone = Smartphone('iPhone', self.weather_station)
        self.outro_smartphone = Smartphone('Outro Smartphone', self.weather_station)
        self.notebook = Notebook(self.weather_station)

        # Adiciona dispositivos observadores à estação meteorológica
        self.weather_station.add_observer(self.smartphone)
        self.weather_station.add_observer(self.outro_smartphone)
        self.weather_station.add_observer(self.notebook)

    def add_observer(self, observer: IObserver) -> None:
        # Adiciona um observador extra ao sistema
        self.weather_station.add_observer(observer)

    def remove_observer(self, observer: IObserver) -> None:
        # Remove um observador do sistema
        self.weather_station.remove_observer(observer)

    def change_state(self, state: dict) -> None:
        # Altera o estado da estação meteorológica e notifica observadores
        self.weather_station.state = state

    def remove_smartphone(self) -> None:
        # Remove o iPhone da lista de observadores
        self.weather_station.remove_observer(self.smartphone)

    def reset_state(self):
        # Reseta o estado da estação meteorológica e notifica observadores
        self.weather_station.reset_state()

# Código principal que utiliza a fachada para simplificar operações
if __name__ == "__main__":
    weather_station = WeatherStationFacade()

    weather_station.change_state({'temperature': '30'})
    weather_station.change_state({'temperature': '32'})
    weather_station.change_state({'humidity': '90'})

    weather_station.remove_smartphone()
    weather_station.reset_state()

    weather_station.change_state({'temperature': '30'})
    weather_station.change_state({'temperature': '32'})
    weather_station.change_state({'humidity': '90'})
