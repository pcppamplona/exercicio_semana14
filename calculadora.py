def potencia (a, b):
  pass

def divisao (a, b):
  pass

def multiplicacao (a, b):
  return a*b

def subtracao (a, b):
  return a - b

def soma (a, b):
  return a + b

a = int(input("Digite o primeiro valor"))
b = int(input ("Digite o segundo valor"))

operacao = input("+: Soma\n-: Subtração\n*: Multiplicação\n/: Divisão\n**: Exponenciação")
if operacao == '+':
  resultado = soma(a, b)
elif operacao == '-':
  resultado = subtracao(a,b)
elif operacao == '*':
  resultado = multiplicacao(a, b)
elif operacao == '/':
  resultado = a // b
else:
  resultado = a ** b
print (resultado)