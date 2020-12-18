print('*'*15, 'Python Calculadora','*'*15)

print('Selecione o número da equação desejada: ')


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


calc = ['1 - Soma', '2 - Subtração', '3 - Multiplicação', '4 - Divisão']
for i in calc:
    print(i)

escolha = input(' Digite sua opção (1/2/3/4): ')

num1 = int(input(' Digite o primeiro número: '))
num2 = int(input(' Digite o segundo número: '))

if escolha == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif escolha == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif escolha == '3':
    print(num1, "X", num2, "=", multiply(num1, num2))
elif escolha == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

