"""
Bridge é um padrão de projeto estrutural que
tem a intenção de desacoplar uma abstração
da sua implementação, de modo que as duas
possam variar e evoluir independentemente.

Abstração é uma camada de alto nível para algo.
Geralmente, a abstração não faz nenhum trabalho
por conta própria, ela delega parte ou todo o
trabalho para a camada de implementação.

RELEMBRANDO: Adapter é um padrão de projeto
estrutural que tem a intenção de permitir
que duas classes que seriam incompatíveis
trabalhem em conjunto através de um "adaptador".

Diferença (GOF pag. 208) - A diferença chave
entre esses padrões está nas suas intenções...
...O padrão Adapter faz as coisas funcionarem
APÓS elas terem sido projetadas; o Bridge as
faz funcionar ANTES QUE existam...
"""
from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self) -> None: ...

    @abstractmethod
    def decrease_volume(self) -> None: ...

    @abstractmethod
    def power(self) -> None: ...


class RemoteControl(IRemoteControl):
    def __init__(self, device: 'IDevice') -> None:
        self._device = device

    def increase_volume(self) -> None:
        if self._device.power:
            self._device.volume += 10

    def decrease_volume(self) -> None:
        if self._device.power:
            self._device.volume -= 10

    def power(self) -> None:
        self._device.power = not self._device.power


class RemoteControlWithMute(RemoteControl):
    def mute(self) -> None:
        self._device.volume = 0

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


class TV(IDevice):
    def __init__(self):
        self._volume = 10
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int):
        if not self._power:
            print(f'{self._name} is not on, please turn device ON')
            return

        if volume > 100:
            self._volume = 100
        elif volume < 0:
            self._volume = 0
        else:
            self._volume = volume
        print(f'Volume is now {self._volume}')

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool):
        self._power = power
        state = "ON" if self._power else "OFF"
        print(f'{self._name} turned {state}')


class Radio(TV): ...

if __name__ == "__main__":
    tv = TV()
    radio = Radio()

    remote = RemoteControl(tv)

    remote.increase_volume()
    remote.power()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.power()
    remote.increase_volume()
    remote.power()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()

    print()
    remote = RemoteControlWithMute(radio)

    remote.increase_volume()
    remote.power()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.power()
    remote.increase_volume()
    remote.power()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    print('MUTE')
    remote.mute()