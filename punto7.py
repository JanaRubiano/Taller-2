'''
Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. 
Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
[list] --> [list[str]]
>>> vowel_finder(["Woolf", 6, no])
>>> Woolf
>>> vowel_finder(["sí", "no", "w", 0])
>>> No existe
'''

def vowel_finder(lista:list) -> list:
    cadenasConVocales = [] # se crea una lista para guradar las cadenas que tengan más de 2 vocales.
    for elmt in lista:
        if type(elmt) == str: # se chequea que el elemento se trate de un string.
            counter = [char for char in elmt if char in "AEIOUaeiou"] # se guardan las vocales del elemento x en una lista.
            if len(counter) > 1: # si hay más de una, se añade el elemento a la lista de vocales.
                cadenasConVocales.append(elmt)
    if len(cadenasConVocales) == 0: # si no se guradaron elementos en la lista de vocales, se retorna que no existe.
        return "No existe"
    else:
        return cadenasConVocales
    
if __name__ == "__main__":
    lista = []
    n = int(input("Ingrese el número de elmentos que va a tener la lista: "))
    for x in range(n):
        elmt = input("Ingrese un elemento: ")
        lista.append(elmt)
    res = vowel_finder(lista)
    print(res)
