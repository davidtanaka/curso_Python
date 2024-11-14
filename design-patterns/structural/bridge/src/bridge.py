"""
Bridge é um padrão de projeto estrutural que
tem a intenção de desacoplar uma abstração
da sua implementação, de modo que as duas
possam variar e evoluir independentemente.
"""

from abc import ABC, abstractmethod

# Interface que define os métodos básicos de um controle remoto
class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self) -> None: ...
    
    @abstractmethod
    def decrease_volume(self) -> None: ...

    @abstractmethod
    def power(self) -> None: ...


# Implementação concreta do controle remoto que usa a interface IRemoteControl
class RemoteControl(IRemoteControl):
    def __init__(self, device: 'IDevice') -> None:
        # O controle remoto "segura" um dispositivo (componente de implementação)
        self._device = device

    # Método para aumentar o volume do dispositivo, se ele estiver ligado
    def increase_volume(self) -> None:
        if self._device.power:
            self._device.volume += 10

    # Método para diminuir o volume do dispositivo, se ele estiver ligado
    def decrease_volume(self) -> None:
        if self._device.power:
            self._device.volume -= 10

    # Alterna o estado de energia do dispositivo (liga/desliga)
    def power(self) -> None:
        self._device.power = not self._device.power


# Extensão de RemoteControl que adiciona uma função de "mudo" para o controle remoto
class RemoteControlWithMute(RemoteControl):
    # Método para silenciar o dispositivo, configurando o volume para 0
    def mute(self) -> None:
        self._device.volume = 0


# Interface que define um dispositivo (ex: TV, rádio), com propriedades de volume e energia
class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self) -> int: ...

    @volume.setter
    @abstractmethod
    def volume(self, volume: int): ...

    @property
    @abstractmethod
    def power(self) -> bool: ...

    @power.setter
    @abstractmethod
    def power(self, power: bool): ...


# Implementação concreta de um dispositivo (TV)
class TV(IDevice):
    def __init__(self):
        self._volume = 10  # Volume inicial
        self._power = False  # Estado de energia inicial (desligado)
        self._name = self.__class__.__name__  # Nome da classe

    # Propriedade que retorna o volume atual
    @property
    def volume(self) -> int:
        return self._volume

    # Setter para ajustar o volume, limitando entre 0 e 100, e verificando se a TV está ligada
    @volume.setter
    def volume(self, volume: int):
        if not self._power:
            print(f'{self._name} is not on, please turn device ON')
            return

        # Limita o volume entre 0 e 100
        if volume > 100:
            self._volume = 100
        elif volume < 0:
            self._volume = 0
        else:
            self._volume = volume
        print(f'Volume is now {self._volume}')

    # Propriedade que retorna o estado de energia (True para ligado, False para desligado)
    @property
    def power(self) -> bool:
        return self._power

    # Setter para alternar o estado de energia e imprimir o novo estado (ON/OFF)
    @power.setter
    def power(self, power: bool):
        self._power = power
        state = "ON" if self._power else "OFF"
        print(f'{self._name} turned {state}')


# Classe Radio que herda de TV, simulando outro tipo de dispositivo
class Radio(TV): ...


if __name__ == "__main__":
    # Criação de uma instância de TV e uma instância de controle remoto para controlá-la
    tv = TV()
    remote = RemoteControl(tv)

    # Operações com o controle remoto
    remote.increase_volume()  # Tenta aumentar o volume, mas a TV está desligada
    remote.power()            # Liga a TV
    remote.increase_volume()   # Aumenta o volume várias vezes
    remote.decrease_volume()   # Diminui o volume
    remote.power()             # Desliga a TV

    print()
    # Criação de uma instância de rádio e de um controle remoto com função de mudo
    radio = Radio()
    remote = RemoteControlWithMute(radio)

    remote.increase_volume()  # Tenta aumentar o volume, mas o rádio está desligado
    remote.power()            # Liga o rádio
    remote.increase_volume()   # Aumenta o volume várias vezes
    remote.decrease_volume()   # Diminui o volume
    remote.mute()              # Silencia o rádio (define o volume para 0)
