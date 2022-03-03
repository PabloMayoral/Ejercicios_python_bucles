'''def operaciones(a,operador,b):
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        return a / b
    else:
        raise Exception ('erroraco')

try:
    print(operaciones(9,'*',7) )
    print(operaciones(9,'+',7) )
except:
    print('error')'''





def calculadora(**operacion):
    op1 = operacion.get('op1')
    op2 = operacion.get('op2')
    op = operacion.get('op')
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    else:
        raise Exception ('erroraco')

print(calculadora(op1 = 5, op2 = 10, op = '+'))