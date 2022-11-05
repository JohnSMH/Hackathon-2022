def Calculadora():
    try:
        print("Calculadora")
        print("1. Suma")
        print("2. Resta")
        print("Seleccione la opcion deseada")
        opcion = input()
        print("Bases:")
        print("1. Binario")
        print("2. Decimal")
        print("3. Hexadecimal")
        print("Seleccione la opcion deseada")
        base = input()
        if opcion == "1":
            if base == "1":
                print("Ingrese el primer numero")
                num1 = input()
                print("Ingrese el segundo numero")
                num2 = input()
                print("El resultado es: ", bin(int(num1, 2) + int(num2, 2)))
            elif base == "2":
                print("Ingrese el primer numero")
                num1 = input()
                print("Ingrese el segundo numero")
                num2 = input()
                print("El resultado es: ", int(num1) + int(num2))
            elif base == "3":
                print("Ingrese el primer numero")
                num1 = input()
                print("Ingrese el segundo numero")
                num2 = input()
                print("El resultado es: ", hex(int(num1, 16) + int(num2, 16)))
        elif opcion == "2":
            if base == "1":
                print("Ingrese el primer numero")
                num1 = input()
                print("Ingrese el segundo numero")
                num2 = input()
                print("El resultado es: ", bin(int(num1, 2) - int(num2, 2)))
            elif base == "2":
                print("Ingrese el primer numero")
                num1 = input()
                print("Ingrese el segundo numero")
                num2 = input()
                print("El resultado es: ", int(num1) - int(num2))
            elif base == "3":
                print("Ingrese el primer numero")
                num1 = input()
                print("Ingrese el segundo numero")
                num2 = input()
                print("El resultado es: ", hex(int(num1, 16) - int(num2, 16)))
    except:
        print("Error volver a intentar")

Calculadora()