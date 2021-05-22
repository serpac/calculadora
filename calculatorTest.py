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
    
    def divisionTest(value1, value2):
    
        resto = value1 / value2

        return resto
    def raizTest(value1):
        
        x = calculatorTest.divisionTest(value1, 2)
   
        for i in range(15):
            if calculatorTest.multiplicacionTest(x,x) == value1:
                return x
              
            else:
                division = calculatorTest.divisionTest(value1, x)
                suma = calculatorTest.sumaTest(x, division)
                lastdivision = calculatorTest.divisionTest(suma, 2)
                x = lastdivision        
    
        return x

calculadora = c.Calculator
print ("seleccione la operación que quiere realizar")
print ("1- Suma")
print ("2- Resta")
print ("3- Multiplicacion")
print ("4- Division")
print ("5- Raiz")
operation = input()

if (operation == "1"):


    print ("Inserte dos número enteros para realizar una suma ")

    operand1 = int(input())
    operand2 = int(input())


    if calculatorTest.sumaTest(operand1, operand2) == calculadora.suma(operand1,operand2):
        print ("prueba correcta")

    else:
        print("prueba incorrecta")

elif (operation == "2"):
    

    print ("Inserte dos número enteros para realizar una resta ")

    operand1 = int(input())
    operand2 = int(input())


    if calculatorTest.restaTest(operand1, operand2) == calculadora.resta(operand1,operand2):
        print ("prueba correcta")

    else:
        print("prueba incorrecta")

elif (operation == "3"):
    

    print ("Inserte dos número enteros para realizar una multiplicación ")

    operand1 = int(input())
    operand2 = int(input())


    if calculatorTest.multiplicacionTest(operand1, operand2) == calculadora.multiplicacion(operand1,operand2):
        print ("prueba correcta")

    else:
        print("prueba incorrecta")

elif (operation == "4"):
    

    print ("Inserte dos número enteros para realizar una división ")

    operand1 = int(input())
    operand2 = int(input())


    if calculatorTest.divisionTest(operand1, operand2) == calculadora.division(operand1,operand2):
        print ("prueba correcta")

    else:
        print("prueba incorrecta")

elif (operation == "5"):
    

    print ("Inserte un número entero para realizar una raiz cuadrada ")

    operand1 = int(input())
    

    calculatorTest.raizTest(operand1)
    if calculatorTest.raizTest(operand1) == calculadora.raiz(operand1):
        print ("prueba correcta")

    else:
        print("prueba incorrecta")
