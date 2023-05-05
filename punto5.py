'''Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. 
'''
def primos(n): # se crea una función para generar los números primos (creada en retos anteriores).
    primos = []
    if n == 1:
        return 1
    for x in range(2, n+1):
        divs_x = []
        for divs in range(2, int(x**0.5) + 1):
            if x%divs == 0:
                divs_x.append(x)
        if len(divs_x) == 0:
            primos.append(x)
    return primos


def MCM(n1:int, n2:int) -> int: # se crea la función para hallar el Mínimo Común Múltiplo entre 2 números.
    primes = primos(max(n1, n2)) # se hace una lista con los números primos del mayor número.
    mcm = 1 # se inicia una variable en 1, la cual será multiplicada por cada divisor.
    x = 0 # x hace las veces de counter.
    while (n1 != 1 or n2 != 1) and x <= len(primes) - 1: # si se cumple que por lo menos uno de los números no sea igual a uno, y que x no sea mayor a la longitud de la lista, se ejecutan las condiciones del ciclo while.
        y = primes[x] # y corresponde a un número primo.
        while n1 % y == 0 or n2 % y == 0: # se hace un segundo ciclo while, donde se cumpla que por lo menos alguno de los números sea divisible sin residuo por el número primo y.
            if n1 % y == 0: # si n1 no tiene residuo, n1 se divide en y, y se hace igual al valor resultante.
                n1 //= y

            if n2 % y == 0: # si n2 no tiene residuo, n2 se divide en y, y se hace igual al valor resultante.
                n2 //= y

            mcm *= y # se multiplica a mcm por y, y se hace iguaol al valor resultante.
        
        x += 1 # solo cuando las condiciones del ciclo while dejan de cumplirse, x aumenta en 1.
    return mcm 
         
if __name__ == "__main__":
    n1 = int(input("Enter an integer: "))
    n2 = int(input("Enter an integer: "))
    res = MCM(n1, n2)
    print(res)