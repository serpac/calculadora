import calculator as c
class calculatorTest:
    

    def sumaTest(value1, value2):
        
        resultado = value1 + value2

        return resultado
   
    def restaTest(value1, value2):

        resto = value1 - value2

        return resto
    
    def multiplicacionTest(value1, value2):
    
        resto = value1 * value2

        return resto
calculadora = c.Calculator
print ("seleccione la operación que quiere realizar")
print ("1- Suma")
print ("2- Resta")
print ("3- Multiplicacion")
print ("4- Division")
print ("5- Raiz")
operation = input()

if (operation == "1"):


    print ("Inserte dos numero enteros para realizar una suma ")

    operand1 = int(input())
    operand2 = int(input())


    if calculatorTest.sumaTest(operand1, operand2) == calculadora.suma(operand1,operand2):
        print ("prueba correcta")

    else:
        print("prueba incorrecta")

elif (operation == "2"):
    

    print ("Inserte dos numero enteros para realizar una resta ")

    operand1 = int(input())
    operand2 = int(input())


    if calculatorTest.restaTest(operand1, operand2) == calculadora.resta(operand1,operand2):
        print ("prueba correcta")

    else:
        print("prueba incorrecta")

elif (operation == "3"):
    

    print ("Inserte dos numero enteros para realizar una multiplicacion ")

    operand1 = int(input())
    operand2 = int(input())


    if calculatorTest.multiplicacionTest(operand1, operand2) == calculadora.multiplicacion(operand1,operand2):
        print ("prueba correcta")

    else:
        print("prueba incorrecta")
