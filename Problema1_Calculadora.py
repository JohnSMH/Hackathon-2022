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
        print("Ingrese el primer numero")
        num1 = input()
        print("Ingrese el segundo numero")
        num2 = input()
        if opcion == "1":
            if base == "1":
                print("El resultado es: ", (bin(int(num1, 2) + int(num2, 2))).replace("0b", ""))
            elif base == "2":
                print("El resultado es: ", int(num1) + int(num2))
            elif base == "3":
                print("El resultado es: ", (hex(int(num1, 16) + int(num2, 16))).replace("0x", ""))
        elif opcion == "2":
            if base == "1":
                print("El resultado es: ", (bin(int(num1, 2) - int(num2, 2))).replace("0b", ""))
            elif base == "2":
                print("El resultado es: ", int(num1) - int(num2))
            elif base == "3":
                print("El resultado es: ", (hex(int(num1, 16) - int(num2, 16))).replace("0x", ""))
            else:
                print("Opcion de base no valida")
        else:
            print("Opcion de operacion no valida")
    except:
        print("Error en los valores ingresados volver a intentar")
