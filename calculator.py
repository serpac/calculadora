class Calculator():

    def suma(operand1, operand2):
        result = operand1 + operand2
      
        return result 

    def resta(operand1, operand2):
        
        result = operand1 - operand2
       
        return result

    def multiplicacion(operand1, operand2):
        
        result = operand1 * operand2
       
        return result
    
    def division(operand1, operand2):
        
        result = operand1 / operand2
     
        return result
    
    def raiz(operand1):


        x = Calculator.division(operand1, 2)

        for i in range(15):
            if Calculator.multiplicacion(x,x) == operand1:
                result = x
               
              
            else:
                division = Calculator.division(operand1, x)
                suma = Calculator.suma(x, division)
                lastdivision = Calculator.division(suma, 2)
                x = lastdivision 
                result = x       
    
        return result
        
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


    finalValue = Calculator.suma(operand1, operand2)

elif (operation == "2"):
    

    print ("Inserte dos número enteros para realizar una resta ")

    operand1 = int(input())
    operand2 = int(input())


    finalValue = Calculator.resta(operand1, operand2)

elif (operation == "3"):
    

    print ("Inserte dos número enteros para realizar una multiplicación ")

    operand1 = int(input())
    operand2 = int(input())


    finalValue = Calculator.multiplicacion(operand1, operand2)

elif (operation == "4"):
    

    print ("Inserte dos número enteros para realizar una división ")

    operand1 = int(input())
    operand2 = int(input())


    finalValue = Calculator.division(operand1, operand2)

elif (operation == "5"):
    

    print ("Inserte un número entero para realizar una raiz cuadrada ")

    operand1 = int(input())
    

    finalValue = Calculator.raiz(operand1)

print("el resultado de la operacion es: "+ str(finalValue))