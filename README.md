# Taller 2
### __Desarrollado por: The Bug Hunting Pythons.__

<p align="center">
  <img src="https://user-images.githubusercontent.com/124607045/236589667-741812cd-a5f3-4fd6-b797-b63bd8582732.png" alt="Sublime's custom image"/>
</p>


* **Integrantes:** Jana Rubiano Hurtado, Samuel Villamizar y Ana Maria De Felipe Briñez. 

---

Bienvenidos a este repostorio en el cual explicaremos el desarrollo de códigos en Python para resolver problemas planteados en la clase de programación. 


Para comenzar observaremos el primer punto. 

1. Desarrollar un programa que ingrese un número entero n y separe todos los dígitos que componen el número.

Para lograr el desarrollo de este punto lo que hicimos fue, primero que todo definir las instrucciones dentro de una función mediante un “def”. Esta función lo que hará es tomar un número entero y con ayuda deL “for” va a iterar los dígitos del número, los agregará a la lista, para luego imprimirlos. 

Y bien, Pero… ¿cómo va a iterar los dígitos del número? Bueno, para eso usaremos un “str” que convertirá el número en un string y agregará cada digito del string a lista. 

```python
# Ejemplo. 
def sep_dig(n:int) -> list:
digitos = [int(num) for num in str(n)]
    return digitos
```

Para finalizar, no debemos olvidar utilizar el “if __name__ == "__main__":” para ejecutar la función, además crear un “int(input())” para que el usuario pueda ingresar el número que desee.

**(Revisar archivo adjunto: punto1.py)**

--- 

Avanzando con el desarrollo del taller continuamos con el punto 2. 

2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entrege los digitos tanto de la parte entera como de la decimal.

Este punto tiene cierta similitud con el punto anterior, solo que el nivel de complejidad aumenta y bueno, para el desarrollo de este se genero nuevamente una función, donde definimos las instrucciones del código. Dentro de este básicamente el usuario al ingresar un número decimal deberá hacerlo con su debido punto y aprovecharemos esto para que el código funcione correctamente, de modo que, igual que el punto anterior con ayuda del “for” y “str” vamos a recorrer los dígitos del número, solo que en este caso usaremos un “if”, este if hará lo que se le pide en la instrucción omitiendo el punto. 

```python
# Ejemplo. 
def sep_dig2(n:float) -> list:
    digitos = [int(num) for num in str(n) if num != "."] 
    return digitos
```

Y bien, eso es todo por este lado.

**(Revisar archivo adjunto: punto2.ipynb)**

---

El siguiente punto del taller, es el numeral 3 que consiste en lo siguiente.

3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos.

Este punto del taller lo realizamos, nuevamente definiendo una función con las siguientes instrucciones; primero que todo la función recibirá dos números, convertirá al primero en un string con “str”. Usando slicing y recorriendo el string al revés con -1, vamos a invertir el número; este resultado lo compararemos con el otro número ingresado por el usuario, para comprarlos usaremos el “if”, si estos dos números son iguales la función va a devolver “True” y si no es así, va a devolver “False”. 

```python
# Ejemplo. 
if n1 == n2:
  return True 
else:
  return False 
```
**(Revisar archivo adjunto: punto3.py)**

---

Ahora bien, continuaremos con el siguiente punto.

4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Con cuántos valores de la serie, se tienen errores del 10%, 1%, 0.1% y 0.001%.


<p align="center">
  <img src="https://user-images.githubusercontent.com/124607045/236589006-61eba2f6-d705-48b9-95c3-140f27577b8e.png" alt="Sublime's custom image"/>
</p>


Para comenzar a desarrollar este código debemos comenzar por importar la función math en Python y definir una variable con el valor real de la función coseno. 

```python
# Ejemplo. 
import math
real = math.cos(x)
```

Una vez ya tenemos lo anterior, nuevamente definiremos una función con las siguientes instrucciones: Primero que todo nombraremos variables que consistan en decir “que no se alcanzó a un x porciento de error”, luego,  con “for” y “range” generamos un recorrido para cada número desde el 0 hasta un número n, es decir, con el “range” vamos a crear un intervalo de números enteros que comience en 0 y termine en el número ingresado por el usuario (n), este número(n) representa las veces en las cuales se van a repetir las instrucciones que irán después del “for”. 

```python
# Ejemplo.
error_a = "No suficiente para obtener un error de menos del 10%" 
error_b = "No suficiente para obtener un error de menos del 1%"
for i in range(n): # Tomará cada número en el rango y ejecutará las instrucciones de abajo. 
```

Una vez ya desarrollado lo anterior definiremos las instrucciones que se ejecutaran por cada número tomado en el “for”. En principio estableceremos en una variable la operación de las series de Taylor para calcular el coseno, por cada número que el “for” tome se irá actualizando, sumándose al resultado anterior ya guardado en la variable. 

Cada vez que con el “for” haga una iteración, aparte de actualizar la operación, va a comprobar el error del resultado que se esta guardando en la variable, para ello otra variable va a operar un cálculo para hallar el error.  Y mediante una serie de “if” se verifica en cada iteración qué porcentaje de aproximación se alcanzó y se asigna a error_a, _b, _c o _d, el número de la iteración.  


```python
# Ejemplo. 
aprox += ((-1)**i) * (x**(2*i)) / (math.factorial(2*i)) # “x” será un valor real ingresado por el usuario.  Y aprox representa la operación de las series de Taylor. 
pct = 100/real*abs(real-aprox) # Variable que calcula el error
        # se verifica en cada iteración qué porcentaje de aproximación se alcanzó y se asigna a error_a, _b, _c o _d, el número de la iteración.
        if pct < 0.001 and type(error_d) == str: 
            error_d = i
        if pct < 0.1 and type(error_c) == str:
            error_c = i
```

 Básicamente esta seria la base del código.  **(Revisar archivo adjunto: punto4.ipynb)**

---

Ahora bien, continuaremos con el siguiente punto.

5. Desarrollar un programa que permita determinar el Mínimo Común Múltiplo de dos números enteros.

Y bueno, para desarrollar este punto comenzamos creando una función que calcula los números primos con el fin de luego usarla para calcular el MCM. 

¿Y cómo se hallan los números primos con una función? El funcionamiento de esta función consiste en lo siguiente: 1. Vamos a definir una variable con una lista vacía. 2. Vamos a establecer una condición, si “n” (número ingresado por el usuario) es 1, va a devolver este número. En caso de que no sea así, vamos a crear con “range” un intervalo de números enteros de [0, hasta n]. 3. y con “for” vamos a iterar cada elemento de este intervalo, de modo que con una serie de operaciones hallaremos los números primos. 

```python
# Ejemplo. 
def primos(n): 
    primos = []
    if n == 1:
        return 1
    for x in range(2, n+1): #Iterará cada número en el intervalo
        divs_x = []
        for divs in range(2, int(x**0.5) + 1): #Iterará cada número en el intervalo
            if x%divs == 0: #Establece condición. (Que el modulo entre “x” y “divs” sea 0. 
                divs_x.append(x) # Agregará el resultado a la lista. 
```

Una vez ya tenemos esta función, crearemos una nueva para hallar el MCM de 2 números. 

La función consiste en lo siguiente: 1. Se creará una lista con los números primos del número mayor, usando “max” (que toma el número mayor). 2. Definimos una variable llamada mcm, que toma el valor de 1 con el fin de ser multiplicada por cada divisor. 3. Definiremos otra variable que contará las repeticiones. 4. Usando “while” establecemos las siguientes condiciones: que alguno de los números NO sea igual a 1 y que x (es decir los números primos) NO sea mayor a la longitud de la lista. 5. Si estas se cumplen, seguirá con la siguiente instrucción: Generará la variable y, que corresponde a un número primo y luego se hace un segundo ciclo con while donde se cumpla que por lo menos alguno de los números sea divisible sin residuo por el número primo y. 6. Una vez ya comprobados ente n1 y n2 por cuales números son divisibles, “y” se multiplica por la variable “mcm”. 7. Al completar los ciclos e iteraciones devolverá el valor final del mcm. 

```python
# Ejemplo. 
def MCM(n1:int, n2:int) -> int
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
```

Y bien, eso es todo por este lado. **(Revisar archivo adjunto: punto5.py)**

--- 
Ahora bien, continuaremos con el siguiente punto.

6. Desarrollar un programa que determine si en una lista no existen elementos repetidos.

En este punto es necesario volver a utilizar funciones para determinar elemtos repetidos en una lista. Para ello primero se define la funcion y como variables se trabaja la lista.

En la funcion primero se itera para cada elemto de la lista, con este se guarda en una variable el numero identificado; en el momento en que el numero se repite, el condicional if retorna el valor falso; de lo contrario el ciclo continua hasta finalizar. En el caso que no se repita un elemento de retorna verdadero.

```python
def elemento_repetido(lista:list)-> bool:

    for elmt in lista: # se itera por cada elemento de la lista.
        rep = lista.count(elmt) # se gurada el número de veces que éste aparece en la lista.
        if rep > 1: # si el elemento apareción más de una vez, se retorna False.
            return False
        
    return True
```
La segunda parte del codigo es el que aplica la funcion. Primero se define la lista y luego se define el numero de elementos de la lista como n. Despues se itera en el rago de n (es decir la cantidad de elementos que contendra la lista), y se ingresa el valor de cada elemento de la lista. Al final se utiliza la funcion definida en la parte anterior y se imprime falso (si esta repedido un elemento) o verdadero (si no se repite ningun elemento de la lista).
```python
if __name__ == "__main__":
    lista = []
    n = int(input("Ingrese el número de elmentos que va a tener la lista: "))
    for x in range(n):
        elmt = input("Ingrese un elemento: ")
        lista.append(elmt)
    res = elemento_repetido(lista)
    print(res)
```
7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

Primero se define una lista de cadenas, luego, se define una función que toma una cadena como entrada y devuelve True si la cadena tiene al menos dos vocales y False en caso contrario. Después, se itera sobre cada cadena en la lista usando un bucle for. Dentro del bucle, se llama a la función para verificar si la cadena tiene al menos dos vocales. Si es así, la cadena se imprime y se establece la variable encontrado en True. Finalmente, después del bucle, se verifica si se encontró al menos una cadena con al menos dos vocales. Si no se encontró ninguna cadena, se imprime "No existe".

```python
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
```
8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.

La función listComp toma dos listas como entrada y devuelve una lista que contiene los elementos de la primera lista que no se encuentran en la segunda lista. Primero se crea una lista vacía llamada lista3 para almacenar los elementos de la lista1 que no están en la lista2. Luego, se itera a través de cada elemento de la lista1 usando un bucle for. Si el elemento actual no se encuentra en la lista2, se agrega a la lista3 usando el método append(). Finalmente, se devuelve la lista3.
```python
def listComp(lista1:list, lista2:list) -> list:

    lista3 = [] # se crea una lista para guardar los elementos que no sean comunes entre las dos listas.
    for elmt in lista1: # se itera por la lista1.
        if elmt not in lista2: # si el elemento de la lista1 no está en la lista2, se agrega a lista3.
            lista3.append(elmt)

    return lista3
```
En la sección principal del programa, se definen dos listas vacías llamadas lista1 y lista2. Luego, se solicita al usuario que ingrese el número de elementos que tendrán ambas listas y se almacena en la variable n. A continuación, se utiliza un bucle for para iterar n veces y solicitar al usuario que ingrese un elemento para la lista1 y la lista2 en cada iteración. Los elementos ingresados se agregan a cada lista respectivamente con el método append(). A continuación, se llama a la función listComp con lista1 y lista2 como argumentos y se almacena el resultado en una variable llamada res. Finalmente, se imprime la lista resultante utilizando la función print().
```python
if __name__ == "__main__":
    lista1 = []
    lista2 = []
    n = int(input("Ingrese el número de elmentos que va a tener cada lista: "))
    for x in range(n):
        elmt = input("Ingrese un elemento para la lista 1: ")
        lista1.append(elmt)
    for x in range(n):
        elmt = input("Ingrese un elemento para la lista 2: ")
        lista2.append(elmt)
    res = listComp(lista1, lista2)
    print(res)
```
9. Resolver el punto 7 del taller 1 usando operaciones con vectores

El programa comienza importando la función prod desde el módulo math, que es utilizada para calcular el producto de todos los números en una lista.

La función stats toma una lista de números como argumento y devuelve una lista de resultados. Dentro de la función, se ordena la lista en orden ascendente y descendente y se almacena en dos variables distintas asc_list y desc_list. Luego, se calcula el promedio de los elementos en la lista y se almacena en una variable st[2]. Para obtener la mediana, se toma el tercer elemento de la lista ordenada en orden ascendente, que es el valor del medio si la lista tiene un número impar de elementos o el promedio de los dos valores del medio si la lista tiene un número par de elementos. Este valor se almacena en la variable st[3].

El promedio multiplicativo se calcula multiplicando todos los elementos en la lista y luego tomando la raíz enésima, donde n es el número de elementos en la lista. Este resultado se almacena en la variable st[4].

Para ordenar la lista en orden ascendente y descendente, se utilizan las funciones sorted y reverse, respectivamente, y se almacenan en st[0] y st[1].

Para obtener el mayor número elevado al menor, se toma el primer y último elemento de la lista ordenada en orden ascendente y se eleva el mayor número a la potencia del menor número. Este resultado se almacena en st[5].

Para obtener la raíz cúbica del menor número, se toma el primer elemento de la lista ordenada en orden ascendente y se eleva a la potencia de 1/3. Este resultado se almacena en st[6].

En la sección principal del programa, se pide al usuario que ingrese 5 números reales y se almacenan en una lista llamada lista. Luego, se llama a la función stats con lista como argumento y se almacena el resultado en una variable res. Finalmente, se imprime el resultado. El resultado incluye la lista ordenada en orden ascendente y descendente, el promedio, la mediana, el promedio multiplicativo, el mayor número elevado al menor y la raíz cúbica del menor.

```python
from math import prod 
def stats(lista:list) -> list:
    st = []
    asc_list = sorted(lista)
    desc_list = sorted(lista, reverse=True)
    
    st.append(asc_list)
    st.append(desc_list)
    st.append(sum(lista)/len(lista))
    st.append(asc_list[2])
    st.append(prod(lista)**0.2)
    st.append(asc_list[-1]**asc_list[0])
    st.append(asc_list[0]**(1/3))
    
    return f"Lista ascendent: {st[0]}\nLista descendente: {st[1]}\nPromedio: {st[2]}\nMediana: {st[3]}\nPromedio multiplicativo: {st[4]}\nMayor elevado al menor: {st[5]}\nRaíz cúbica del menor: {st[6]}"


if __name__ == "__main__":
    lista = [int(input("Ingrese un entero: ")) for n in range(5)]
    res = stats(lista)
    print(res)
```
10) Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.

El algoritmo presentado determina si una matriz cuadrada es mágica o no. Primero, se calcula la suma de cada fila y se guarda en una lista llamada suma_filas. Luego, se calcula la suma de cada columna y se guarda en otra lista llamada suma_columnas. Si alguna de las sumas no coincide con las demás, la función retorna False.

Después, se calculan las sumas de las dos diagonales de la matriz y se comparan con la suma de las columnas. Si alguna de las sumas de las diagonales no coincide con la suma de las columnas, la función retorna False. En caso contrario, la función retorna True, indicando que la matriz es mágica.

La función magicMatrix toma como parámetro una matriz cuadrada representada como una lista de listas. La función devuelve un valor booleano que indica si la matriz es mágica o no.

El código calcula la suma de la diagonal izquierda-derecha: se usa una comprensión de lista para invertir la lista de filas y luego se toman los elementos de cada fila correspondientes a la posición de la diagonal. 

```python
def magicMatrix(matrix:list) -> bool:
    m_len = len(matrix)
    suma_filas = [] # se suman las filas.
    for i in range(m_len): 
        lst = matrix[i]
        suma = 0 # se inicia suma en 0
        for j in range(m_len):
            suma += lst[j]
        if len(suma_filas) == 0: # se agregan los valores de suma a suma_columnas si la lista está vacia, o el valor ya guardado es el mismo.
            suma_filas.append(suma)
        elif suma_filas[-1] == suma:
            suma_filas.append(suma)
        else:
            return False
        
    suma_columnas = [] # se suman las columnas.
    for i in range(m_len):
        suma = 0 # se inicia suma en 0
        for j in range(m_len):
            suma += matrix[i][j]
        if len(suma_columnas) == 0: # se agregan los valores de suma a suma_columnas si la lista está vacia, o el valor ya guardado es el mismo.
            suma_columnas.append(suma)
        elif suma_columnas[-1] == suma:
            suma_columnas.append(suma)
        else:
            return False    

    if suma_filas != suma_columnas: # se compara si las listas (que contienen los valores calculados para la suma de cada fila y columna), son iguales.
        return False # si no son iguales la función retorna False.
    
    suma_diagonal1 = 0 # se halla la suma de la diagonal der-izq.
    shifter = 0
    for i in range(m_len):
        suma_diagonal1 += matrix[i][shifter]
        shifter += 1  

    suma_diagonal2 = sum([row[len(matrix) - 1 - i] for i, row in enumerate(matrix)]) # se halla la suma de la diagonal izq-der (se implementaron técnicas novedosas ya que era practicamente lo mismo que para la otra diagonal).

    for i in range(m_len): # se compara si las listas de las diagonales son iguales a la suma_columnas
        if suma_columnas[i] != suma_diagonal1 and suma_columnas != suma_diagonal2:
            return  False

    return True
    

if __name__ == "__main__":
    matrix = []
    n = int(input("Ingrese la dimensión de la matriz (ésta será cuadrada): "))
    for x in range(n):
        lista = []
        for y in range(n):
            elmt = int(input(f"Ingrese un número para la fila {x+1}: "))
            lista.append(elmt)
        matrix.append(lista)
    res = magicMatrix(matrix)

    print(res)
```
