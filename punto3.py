'''
Se ingresan dos números enteros y se determina si son números espejo.
[int, int] --> [bool]
>>> numerosEspejo(12, 21)
>>> True
'''
def numerosEspejo(n1:int, n2:int) -> bool:
    if n1 == int(str(n2)[::-1]): # se convierte uno de los números a string y se invierte, luego se vuelve a convertir a int para compararlo con el otro número.
        return True
    else:
        return False
    
if __name__ == "__main__":
    n1 = int(input("Ingrese un entero: "))
    n2 = int(input("Ingrese un entero: "))
    res = numerosEspejo(n1, n2)
    print(res)