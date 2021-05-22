import calculator as c
class calculatorTest:
    

    def sumaTest(value1, value2):
        
        resultado = value1 + value2

        return resultado
   
    def restaTest(value1, value2):

        resto = value1 - value2

        return resto
calculadora = c.Calculator
print ("Inserte dos numero enteros para realizar una resta")

operand1 = int(input())
operand2 = int(input())

if calculatorTest.restaTest(operand1, operand2) == calculadora.resta(operand1,operand2):
    print ("prueba correcta")

else:
    print("prueba incorrecta")