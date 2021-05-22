import calculator as c
class calculatorTest:
    

    def sumaTest(value1, value2):
        
        resto = value1 + value2

        return resto
   
calculadora = c.Calculator
print ("Inserte dos numero enteros para realizar una suma")

operand1 = int(input())
operand2 = int(input())

if calculatorTest.sumaTest(operand1, operand2) == calculadora.suma(operand1,operand2):
    print ("prueba correcta")

else:
    print("prueba incorrecta")