"""
Este código implementa um exemplo do padrão de projeto State usando o contexto de um rádio de carro. 
O `Sound` funciona como um sistema de áudio que pode alternar entre dois modos de reprodução: rádio 
(`RadioMode`) e música (`MusicMode`). Cada modo tem um comportamento específico para avançar (`press_next`) 
e retroceder (`press_prev`). O `Sound` pode trocar de modo dinamicamente, o que altera a forma como o sistema 
responde aos comandos, simulando a funcionalidade básica de um rádio de carro com mudança de estação e controle de faixas.

Explicação das classes:
- `Sound`: classe principal que representa o sistema de áudio de um carro, com a capacidade de mudar entre 
  os modos de rádio e música. Ela mantém o estado de reprodução e delega os comandos de "próximo" e 
  "anterior" ao modo atual.
- `PlayMode`: classe abstrata que define a interface para os modos de reprodução. Contém métodos abstratos 
  para `press_next` e `press_prev`, que cada modo específico deve implementar.
- `RadioMode`: modo que representa a funcionalidade de rádio, onde `press_next` e `press_prev` alteram 
  a frequência da estação em 100 unidades.
- `MusicMode`: modo que representa a funcionalidade de reprodução de música, onde `press_next` e 
  `press_prev` avançam ou retrocedem faixas de música.

Explicação dos `type hints`:
- `self.mode: 'PlayMode'`: indica que o atributo `mode` será uma instância de `PlayMode`.
- `self.playing: int`: especifica que `playing` é um contador inteiro que representa o estado da reprodução.
- Nos métodos, usamos `'PlayMode'` entre aspas para evitar um erro de referência circular, pois `PlayMode` 
  ainda não está definido no momento da declaração.
"""

from abc import ABC, abstractmethod

class Sound:
    # Classe principal que representa o sistema de áudio de um carro.
    
    def __init__(self) -> None:
        # Inicializa o modo padrão como rádio e o contador de reprodução como 0.
        self.mode: 'PlayMode' = RadioMode(self)
        self.playing: int = 0

    def change_mode(self, mode: 'PlayMode') -> None:
        # Alterna o modo de reprodução, reiniciando a contagem de reprodução.
        print(f'Mudando para o modo {mode.__class__.__name__}')
        self.playing = 0
        self.mode = mode

    def press_next(self) -> None:
        # Avança a reprodução no modo atual.
        self.mode.press_next()
        print(self)

    def press_prev(self) -> None:
        # Retrocede a reprodução no modo atual.
        self.mode.press_prev()
        print(self)

    def __str__(self) -> str:
        # Representação em string do estado atual da reprodução.
        return str(self.playing)

class PlayMode(ABC):
    # Classe abstrata que define a interface de um modo de reprodução.
    
    def __init__(self, sound: 'Sound') -> None:
        # Inicializa o modo de reprodução com uma referência ao objeto Sound.
        self.sound = sound

    @abstractmethod
    def press_next(self) -> None: ...
    # Método abstrato que avança a reprodução.

    @abstractmethod
    def press_prev(self) -> None: ...
    # Método abstrato que retrocede a reprodução.

class RadioMode(PlayMode):
    # Classe que representa o modo de rádio.
    
    def press_next(self) -> None:
        # Avança a frequência da rádio em 100.
        self.sound.playing += 100

    def press_prev(self) -> None: 
        # Retrocede a frequência da rádio em 100, sem permitir que fique negativa.
        self.sound.playing -= 100 if self.sound.playing > 0 else 0

class MusicMode(PlayMode):
    # Classe que representa o modo de música.
    
    def press_next(self) -> None:
        # Avança para a próxima faixa.
        self.sound.playing += 1

    def press_prev(self) -> None: 
        # Retrocede para a faixa anterior, sem permitir valores negativos.
        self.sound.playing -= 1 if self.sound.playing > 0 else 0

if __name__ == '__main__':
    # Exemplo de uso do sistema de áudio.
    sound = Sound()
    sound.press_next()  # Avança no modo de rádio
    sound.press_next()
    sound.press_next()
    sound.press_prev()
    sound.press_prev()

    print()

    # Altera para o modo de música e controla faixas.
    sound.change_mode(MusicMode(sound))
    sound.press_next()
    sound.press_next()
    sound.press_next()
    sound.press_next()
    sound.press_prev()
    sound.press_prev()
