import time
from threading import Thread


def carro(velocidade, piloto):
    trajeto = 0

    while trajeto < 120:
        trajeto += velocidade
        time.sleep(0.2)
        print("Piloto {}, Km {}\n".format(piloto, trajeto))


t_carro1 = Thread(target=carro, args=[1, "Italo"])
t_carro2 = Thread(target=carro, args=[2, "Leona"])

t_carro1.start()
t_carro2.start()
