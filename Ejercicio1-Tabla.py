
num1=int(input('Dame el numero para la multiplicacion'))


def Tabla(valorResul):
    for x in range(1,11):
        print("{0} x {1} = {2}".format(valorResul, x, valorResul * x))

Tabla(num1)
