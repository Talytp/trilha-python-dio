a = int(input("Valor de a: "))

b = int(input("Valor de b: "))

def subtrair (a,b):
    return a - b

def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(a, b, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(a, b, subtrair)

op = somar

print(op(23,56))