'''
Pprograma que pide 5 números reales y calcula los siguientes valores estadísticos:

El promedio
La mediana
El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
Ordenar los números de forma ascendente
Ordenar los números de forma descendente
La potencia del mayor número elevado al menor número
La raíz cúbica del menor número
'''

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
