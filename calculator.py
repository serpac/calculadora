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
                return x
              
            else:
                division = Calculator.division(operand1, x)
                suma = Calculator.suma(x, division)
                lastdivision = Calculator.division(suma, 2)
                x = lastdivision        
    
        return x
        
        # return 0