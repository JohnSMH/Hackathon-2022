import Problema1_Calculadora
import Problema2_SumaVocales
import Problema3_Factorial
import Problema4_Porciones

def MenuPrincipal():
    condicion = True
    while condicion:
        print("Menu Principal")
        print("1. Calculadora")
        print("2. Suma de vocales")
        print("3. Factorial")
        print("4. Porciones")
        print("Seleccione la opcion deseada")
        opcion = input()
        if opcion == "1":
            Problema1_Calculadora.Calculadora()
        elif opcion == "2":
            string = input("Ingresa palabra:")
            print (Problema2_SumaVocales.ContadorVocales(string))
        elif opcion == "3":
            num = int(input("Introduce un número:"))
            print(Problema3_Factorial.factorial(num))
        elif opcion == "4":
            Problema4_Porciones.Porciones()
        else:
            print("Opcion no valida")
        print("Desea continuar? (S/N)")
        respuesta = input()
        if respuesta == "N":
            condicion = False

MenuPrincipal()