from FiguraGeometrica import FiguraGeometrica
from Triangulo import Triangulo
from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

while True:
    print("-----------------MENU------------")
    print("triangulo (1) ")
    print("circulo (2) ")
    print("cuadrado (3) ")
    print("rectangulo (4) ")
    print("Cerrar (0) ")

    opcion = input("digite el numero de la figura que desea hallar el area: ")
    if opcion == "1":
        base = int(input("digite la base: "))
        altura = int(input("digite la altura: "))
        tr = Triangulo(altura,base)
        print("el area del triangulo es: ",tr.area())
    elif opcion =="2":
        radio = int(input("digite el radio: "))
        ci = Circulo(radio)
        print("El area del circulo es:",ci.area())
    elif opcion == "3":
        lado = float(input("digite el lado del cuadrado: "))
        cu = Cuadrado(lado)
        print("El area del cuadrado es:",cu.area())
    elif opcion == "4":
        base = float(input("digite la base: "))
        altura = float(input("digite la altura: "))
        re = Rectangulo(base,altura)
        print("El area del rectangulo es:",re.area())


    else: 
        opcion == "0"
        print("fin del programa")
        break
    