from time import sleep
from threading import Thread
from threading import Lock

"""
class MeuThread(Thread):
    def __init__(self, texto: str, tempo: int):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 2)
t1.start()

t2 = MeuThread('Thread 2', 4)
t2.start()

t3 = MeuThread('Thread 3', 6)
t3.start()

for i in range(20):
    print(i)
    sleep(1)
"""

"""def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
t1.start()
# t1.join()

# t2 = Thread(target=vai_demorar, args=('Olá mundo 2!', 1))
# t2.start()

# t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 2))
# t3.start()

while t1.is_alive():
    print('Esperando a thread.')
    sleep(2)

print('Thread acabou!')"""

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return
        
        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingressos. '
              f'Ainda temos {self.estoque} em estoque.')
        
        self.lock.release()

if __name__ == '__main__':
    ingressos = Ingressos(10)
    
    for i in range(20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)
