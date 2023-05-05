'''
Se ingresa un número entero y se retornan los dígitos que componen el número.
[int] --> [lst(int)]
>>> sep_dig(1933)
>>> [1, 9, 3, 3]
'''

def sep_dig(n:int) -> list:
    digitos = [int(num) for num in str(n)] # se convierte el número a un string y se agregan cada dígito del string a una lista. 
    return digitos

if __name__ == "__main__":
    n = int(input("Ingrese un número entero: "))
    lst = sep_dig(n)
    for num in lst:
        print(num)