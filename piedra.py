from random import randint
a=randint(1, 3)
if a==1:
    c="piedra"

elif a==2:
    c="papel"
    
elif a==3:
    c="tijera"

#1 es igual a piedra
#2 es igual a papel
#3 es tijera
class maquina:
    def __init__(self, soy, saludo, opciones):
        self.soy=soy
        self.saludo=saludo
        self.opciones=opciones
        

    def saludar(self):
        print('Me llamo',self.soy)
        print('Jugemos piedra, papel o tijera',self.saludo)
        print('te doy las siguientes opciones:', self.opciones)


iniciar=maquina('MAc',' bienvenido','igresa los numeros para elegir: 1 piedra, 2 papel, 3 tijera')
iniciar.saludar()
jugada=input("cual es tu jugada? ")

jugada=int(jugada)




if jugada ==a:
    print('Empate jaja elegi ',c)

elif jugada==1 and a==2:
    print('Pierdes elegi ', c)

elif jugada==1 and a==3:
    print('Ganas yo elegi ', c)

elif jugada==2 and a==1:
    print('Ganas yo elegi ', c)

elif jugada==2 and a==3:
    print('Pierdes jaja elegi ', c)

elif jugada==3 and a ==1:
    print('Pierdes yo elegi', c)

elif jugada==3 and a==2:
    print('Ganas yo elegi', c)
