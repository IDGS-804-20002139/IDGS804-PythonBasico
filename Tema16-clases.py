import os


class Operasbas():  # Nombre de la clase y si son dos  se separa con coma#
    # Propiedades de Clase
    num1 = 0
    num2 = 0
    res = 0
    # Construtor

    def _init_(self, a, b):
        self.num1 = a
        self.num2 = b

    def suma(self):
        self.res = self.num1+self.num2

    def resta(self):
        self.res = self.num1/self.num2

    # Metodos de Clase


def main():
    os.system('cls')
    obj = Operasbas(3, 4)
    obj.suma()
    print("La suma es: {}".format(obj.res))


if __name__ == "__main__":
    main()
