class Persona:
    poblacion=0

    def __init__(self, name, age, hobby, sex):
        self.name=name
        self.age=age
        self.hobby=hobby
        self.sex=sex
        
    def saludar(self):
        print('hi my name is', self.name)
        print('tengo', self.age)
        print('me gusta',self.hobby)
        print('frecuencia de sex', self.sex)

    @classmethod
    def cuenta(cls):
        print('numero de personas',cls.self)

p=Persona('carlos', 21, 'go to the gymp','numca')
p.saludar()