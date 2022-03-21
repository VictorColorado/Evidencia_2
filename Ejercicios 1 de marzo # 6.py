class saludo:
    def saludar(self,nombre):
        print('Hola',nombre)
nombre=input('Introducetunombre:')
s=saludo()
s.saludar(nombre)