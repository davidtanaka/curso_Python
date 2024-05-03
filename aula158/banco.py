import contas
import pessoas

class Banco:
    def __init__(
        self, agencias: list[int] | None = None, 
        clientes: list[pessoas.Pessoa] | None = None, 
        contas: list[contas.Conta] | None = None
    ):
        
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False
    
    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False
    
    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False
    

    def _checa_se_conta_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    
    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_cliente(cliente, conta)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'
    
if __name__ == '__main__':
    c1 = pessoas.Cliente('Davi', 16)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Mauro', 59)
    cp1 = contas.ContaPoupanca(222, 111, 17)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        print(c1.conta)