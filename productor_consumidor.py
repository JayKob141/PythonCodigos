import threading
from time import sleep

class ProductorConsumidor(threading.Thread):
    def __init__(self,recurso,id,cantidad = 1):
        # If the subclass overrides the constructor, it must make sure to invoke the base 
        # class constructor (Thread.__init__()) before doing anything else to the thread.
        threading.Thread.__init__(self)
        self.recurso = recurso
        self.cantidad = cantidad
        self.id = id

class Consumidor(ProductorConsumidor):

    def run(self):
        for i in range(0,self.cantidad):
            value = self.recurso.consumir(thread = self)
            while value == 0:
                value = self.recurso.consumir(thread = self)

class Productor(ProductorConsumidor):
    def run(self):
        for i in range(0,self.cantidad):
            # TODO: COLOCAR UN LIMITE AL RECURSO
            self.recurso.incrementar(thread = self)

class Recurso:
    def __init__(self):
        self.lock = threading.Lock()
        self.valor = 0
    def consumir(self,thread):
        value = 0
        self.lock.acquire()
        # NO PONER return entre acquire, release: que solo haya 1 punto de salida
        if self.valor == 0:
            value = 0
        else:
            print(thread.id," CONSUMIENDO, valor actual del recurso = ",self.valor)
            value = 1
            self.valor = self.valor - 1
        self.lock.release()
        return value
    def incrementar(self,thread):
        self.lock.acquire()
        self.valor = self.valor + 1 
        print(thread.id," PRODUCIENDO, valor actual del recurso = ",self.valor)
        self.lock.release()

hilos = []
recurso = Recurso()
for i in range(0,30):
    consumidor = Consumidor(recurso, "C-" + str(i) )
    productor  = Productor(recurso, "P-" + str(i) )
    hilos.append( consumidor )
    hilos.append( productor )

for hilo in hilos:
    hilo.start()

print("Soy el main thread!")

