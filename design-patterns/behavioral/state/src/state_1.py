"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""
from abc import ABC, abstractmethod

class Order:
    # Context
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> str:
        return self.state.pending()

    def approve(self) -> str:
        return self.state.approve()

    def reject(self) -> str:
        return self.state.reject()
    
class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> str: ...

    @abstractmethod
    def approve(self) -> str: ...

    @abstractmethod
    def reject(self) -> str: ...


class PaymentPending(OrderState):
    def pending(self) -> str:
        return f'O estado atual é {self.__class__.__name__}'

    def approve(self) -> str: 
        self.order.state = PaymentApproved(self.order)
        return 'Pagamento aprovado'

    def reject(self) -> str:
        self.order.state = PaymentRejected(self.order)
        return 'Pagamento aprovado'


class PaymentApproved(OrderState):
    def approve(self) -> str:
        return f'O estado atual é {self.__class__.__name__}'
    
    def pending(self) -> str: 
        self.order.state = PaymentPending(self.order)
        return 'Pagamento Pendente'

    def reject(self) -> str: 
        self.order.state = PaymentRejected(self.order)
        return 'Pagamento Recusado'


class PaymentRejected(OrderState):
    def reject(self) -> str:
        return f'O estado atual é {self.__class__.__name__}'
    
    def approve(self) -> str:
        return 'Pagamento já recusado.'

    def pending (self) -> str:
        return 'Pagamento já recusado.'
    
if __name__ == '__main__':
    order = Order()
    print(order.pending())
    print(order.approve())
    print(order.pending())
    print(order.reject())
    print(order.pending())
    print(order.approve())
