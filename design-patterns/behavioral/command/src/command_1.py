class Light:
    # Receiver - Luz Inteligente

    def __init__(self, name: str, room_name: str) -> None:
        self.name = name  # Nome da luz
        self.room_name = room_name  # Nome do cômodo onde a luz está localizada
        self.color = 'Default color'  # Cor padrão da luz

    def on(self) -> str:
        # Liga a luz e retorna uma mensagem indicando que a luz está ON
        return f'{self.name} no {self.room_name} está ON'

    def off(self) -> str:
        # Desliga a luz e retorna uma mensagem indicando que a luz está OFF
        return f'{self.name} no {self.room_name} está OFF'

    def change_color(self, color: str) -> str:
        # Muda a cor da luz e retorna uma mensagem com a nova cor
        self.color = color
        return f'{self.name} no {self.room_name} está {self.color}'


class ICommand:
    # Interface de comando

    def execute(self) -> None:
        # Executa o comando - deve ser implementado por classes concretas
        pass

    def undo(self) -> None:
        # Desfaz o comando - deve ser implementado por classes concretas
        pass


class LightOnCommand(ICommand):
    # Comando concreto para ligar a luz

    def __init__(self, light: Light) -> None:
        self.light = light  # Instância da luz a ser controlada

    def execute(self) -> str:
        # Liga a luz e retorna a mensagem resultante
        return self.light.on()

    def undo(self) -> str:
        # Desliga a luz e retorna a mensagem resultante
        return self.light.off()


class LightChangeColor(ICommand):
    # Comando concreto para mudar a cor da luz

    def __init__(self, light: Light, color: str) -> None:
        self.light = light  # Instância da luz a ser controlada
        self.color = color  # Nova cor para a luz
        self._old_color = self.light.color  # Armazena a cor anterior para desfazer

    def execute(self) -> str:
        # Muda a cor da luz e armazena a cor anterior
        self._old_color = self.light.color
        return self.light.change_color(self.color)

    def undo(self) -> str:
        # Restaura a cor anterior da luz
        return self.light.change_color(self._old_color)


class RemoteController:
    # Invoker que armazena e executa comandos

    def __init__(self) -> None:
        self._buttons = {}  # Dicionário para associar botões a comandos
        self._undos = []  # Lista para armazenar comandos executados para desfazer

    def button_add_command(self, name: str, command: ICommand) -> None:
        # Adiciona um comando a um botão específico
        self._buttons[name] = command

    def button_pressed(self, name: str) -> str:
        # Executa o comando associado ao botão pressionado
        if name in self._buttons:
            result = self._buttons[name].execute()
            self._undos.append((name, 'execute'))
            return result
        return "Botão não encontrado"

    def button_undo(self, name: str) -> str:
        # Desfaz o comando associado ao botão pressionado
        if name in self._buttons:
            result = self._buttons[name].undo()
            self._undos.append((name, 'undo'))
            return result
        return "Botão não encontrado"

    def global_undo(self) -> str:
        # Desfaz a última operação realizada, seja execute ou undo
        if not self._undos:
            return 'Nada para desfazer'

        button_name, action = self._undos.pop()

        if action == 'execute':
            return self._buttons[button_name].undo()
        else:
            return self._buttons[button_name].execute()


if __name__ == "__main__":
    # Instâncias de luz para representar luzes em diferentes cômodos
    bedroom_light = Light('Luz do quarto', 'Quarto')
    bathroom_light = Light('Luz do banheiro', 'Banheiro')

    # Comandos concretos para controlar as luzes
    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light, 'Blue')
    bedroom_light_red = LightChangeColor(bedroom_light, 'Red')

    # Controlador remoto que associa botões a comandos
    remote = RemoteController()

    # Configurações de botões do controle remoto
    remote.button_add_command('first_button', bedroom_light_on)
    remote.button_add_command('second_button', bathroom_light_on)
    remote.button_add_command('third_button', bedroom_light_blue)
    remote.button_add_command('fourth_button', bedroom_light_red)

    # Teste de pressionar e desfazer comandos
    print(remote.button_pressed('first_button'))
    print(remote.button_undo('first_button'))

    print(remote.button_pressed('second_button'))
    print(remote.button_undo('second_button'))

    print(remote.button_pressed('third_button'))
    print(remote.button_pressed('fourth_button'))
    print(remote.button_undo('fourth_button'))

    # Desfaz todas as operações uma a uma
    print(remote.global_undo())
    print(remote.global_undo())
    print(remote.global_undo())
    print(remote.global_undo())
    print(remote.global_undo())
