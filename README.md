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

5. Desarrollar un programa que permita determinar el Mínimo Común Múltiplo de dos números enteros. Abordar el problema desde la perspectiva iterativa como recursiva.

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

… 



