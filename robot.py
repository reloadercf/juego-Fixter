class Robot:
    poblacion=0
    def __init__(self, name, lenguaje, color, altura, mascota):
        self.name=name
        self.lenguaje=lenguaje
        self.color=color
        self.altura=altura
        self.mascota=mascota

        Robot.poblacion+=1

    def hablar(self):
        print('Hola soy un robot y me llamo', self.name)
        print('se hablar:', self.lenguaje)
        print('soy de color', self.color)
        print('mido', self.altura)
        print('tengo un', self.mascota)

    def destruir(self):
        Robot.poblacion-=1
        print(self.name, 'acaba de ser destruido')

    @classmethod
    def cuantos(cls):
        print('poblacion de Robots acutal:',cls.poblacion)


booty=Robot('booty boot', 'portugues', 'cafe', 50, 'tucan')
booty.hablar()
booty.cuantos()
booty.destruir()
booty.cuantos()