def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisao por zero nao permitida")
    return a / b

if __name__ == "__main__":
    print("Calculadora simples")
    print(f"2 + 3 = {somar(2, 3)}")
    print(f"10 - 4 = {subtrair(10, 4)}")
    print(f"3 * 7 = {multiplicar(3, 7)}")
    print(f"15 / 3 = {dividir(15, 3)}")
