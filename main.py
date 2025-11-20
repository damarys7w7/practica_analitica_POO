from FiguraGeometrica import FiguraGeometrica
from Triangulo import Triangulo
from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Cilindro import Cilindro
from Paralelograma import Paralelograma
from Trapecio import Trapecio

while True:
    print("-----------------MENU------------")
    print("triangulo (1) ")
    print("circulo (2) ")
    print("cuadrado (3) ")
    print("rectangulo (4) ")
    print("cilindro (5)")
    print("paralelograma (6)")
    print("trapecio (7)")
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

    elif opcion =="5":
        radio=float(input("digite el radio del cilindro:"))
        altura=float(input("digite la altura del cilindro:"))
        cl= Cilindro("cilindro")
        cl.radio=radio
        cl.altura=altura
        print("al area del cilindro es:",cl.area())    

    elif opcion =="6":
        base=float(input("digite la base del paralelograma:"))
        altura=float(input("digite la altura del paralelograma:"))
        pl= Paralelograma("paralelograma")
        pl.base=base
        pl.altura=altura
        print("al area del paralelograma es:",pl.area())

    elif opcion == "7":
        base_mayor = float(input("Digite la base mayor del trapecio: "))
        base_menor = float(input("Digite la base menor del trapecio: "))
        altura = float(input("Digite la altura del trapecio: "))
        tr = Trapecio("Trapecio")
        tr.base_mayor = base_mayor
        tr.base_menor = base_menor
        tr.altura = altura
        print("El área del trapecio es:", tr.area())

    else: 
        opcion == "0"
        print("fin del programa")
        break
