from abc import ABC, abstractmethod

class Order:
    # Classe de contexto que mantém uma referência ao estado atual do pedido

    def __init__(self) -> None:
        # Define o estado inicial do pedido como 'PaymentPending'
        self.state: 'OrderState' = PaymentPending(self)

    def pending(self) -> str:
        # Delegação do comportamento 'pending' para o estado atual
        return self.state.pending()

    def approve(self) -> str:
        # Delegação do comportamento 'approve' para o estado atual
        return self.state.approve()

    def reject(self) -> str:
        # Delegação do comportamento 'reject' para o estado atual
        return self.state.reject()

class OrderState(ABC):
    # Classe abstrata base para representar o estado de um pedido
    
    def __init__(self, order: 'Order') -> None:
        # Inicializa o estado com uma referência ao pedido associado
        self.order = order

    @abstractmethod
    def pending(self) -> str: ...
    # Método abstrato 'pending' a ser implementado por subclasses

    @abstractmethod
    def approve(self) -> str: ...
    # Método abstrato 'approve' a ser implementado por subclasses

    @abstractmethod
    def reject(self) -> str: ...
    # Método abstrato 'reject' a ser implementado por subclasses

class PaymentPending(OrderState):
    # Estado específico que representa o pagamento pendente
    
    def pending(self) -> str:
        # Retorna uma mensagem indicando o estado atual
        return f'O estado atual é {self.__class__.__name__}'

    def approve(self) -> str: 
        # Transita para o estado de pagamento aprovado
        self.order.state = PaymentApproved(self.order)
        return 'Pagamento aprovado'

    def reject(self) -> str:
        # Transita para o estado de pagamento rejeitado
        self.order.state = PaymentRejected(self.order)
        return 'Pagamento recusado'

class PaymentApproved(OrderState):
    # Estado específico que representa o pagamento aprovado

    def approve(self) -> str:
        # Retorna uma mensagem indicando o estado atual
        return f'O estado atual é {self.__class__.__name__}'
    
    def pending(self) -> str: 
        # Transita para o estado de pagamento pendente
        self.order.state = PaymentPending(self.order)
        return 'Pagamento pendente'

    def reject(self) -> str: 
        # Transita para o estado de pagamento rejeitado
        self.order.state = PaymentRejected(self.order)
        return 'Pagamento recusado'

class PaymentRejected(OrderState):
    # Estado específico que representa o pagamento rejeitado

    def reject(self) -> str:
        # Retorna uma mensagem indicando o estado atual
        return f'O estado atual é {self.__class__.__name__}'
    
    def approve(self) -> str:
        # Informa que o pagamento já foi rejeitado e não pode ser aprovado
        return 'Pagamento já recusado.'

    def pending(self) -> str:
        # Informa que o pagamento já foi rejeitado e não pode estar pendente
        return 'Pagamento já recusado.'
    
if __name__ == '__main__':
    # Exemplo de uso do padrão de projeto State
    order = Order()
    print(order.pending())   # Estado atual: 'PaymentPending'
    print(order.approve())   # Transição para 'PaymentApproved'
    print(order.pending())   # Transição para 'PaymentPending'
    print(order.reject())    # Transição para 'PaymentRejected'
    print(order.pending())   # Retorna 'Pagamento já recusado.'
    print(order.approve())   # Retorna 'Pagamento já recusado.'
