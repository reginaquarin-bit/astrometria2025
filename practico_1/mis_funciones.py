# %%
import numpy as np
def glc(n, x0, a=57, c=1, m=256):

    numeros_pp = []
    for i in range(n):
        x = (c + a*x0) % m
        numeros_pp.append(x/m)
        x0 = x

    return numeros_pp



# %%
def generador_congruencia_lineal_enteros(n, x0, a=1664525, c=1013904223, m=2**32): 
    #n: cantidad de números aleatorios a generar
    #x0: semilla
    #a: multiplicador
    #c: incremento
    #M: Módulo

    numeros_enteros = []
    for i in range(n):
        x = (c + a*x0) % m
        numeros_enteros.append(x) #guarda cada numero en una lista
        x0 = x
    return numeros_enteros

def generador_congruencia_lineal(n, x0, a=1664525, c=1013904223, m=2**32):
    return np.array(generador_congruencia_lineal_enteros(n,x0,a,c,m))/m #objeto de python con valores y metodos asociados
                                                            #los array solo admiten valores de tipo iguales





# %%

def generador_fibonacci_enteros(n , x0, j=24, k=55, m=2**32):
    numeros = generador_congruencia_lineal_enteros(k, x0, a=57, c=1)
    for i in range(k, k+n): #toma de k hasta k+n-1, el ultimo no lo cuenta
        numeros.append ((numeros[i-j]+numeros[i-k]) % m) #estamos generando el numero k-esimo
    return numeros[k:] #te devuelve de k en adelante

def generador_fibonacci(n, x0, j =24, k=55, m=2**32):
    return np.array(generador_fibonacci_enteros(n,x0,j,k,m))/m





# %%

import numpy as np
def generador_galaxias(n):
    galaxias = []

    X = generador_fibonacci(n,142)
    for x in X:
        if (0 <= x) and (x < 0.4):
            galaxias.append("eliptica")
        elif (0.4 <= x) and (x < 0.7):
            galaxias.append("espiral")
        elif (0.7 <= x) and (x < 0.9):
            galaxias.append("enana")
        else:
            galaxias.append("irregular")
    return galaxias

g = generador_galaxias(20)
print(g)
# %%
import numpy as np
def monty_hall():
    vector = ["cabra", "cabra", "auto"]
    while(True):
        puertas = np.random.permutation(vector)
        elección = int(input("Elija una puerta 1,2 o 3: "))
        if puertas[elección-1] == "auto":
            print("ganó")
        else:
            print("perdió")

    

#%%
def ejemplo():
    nombre = input("nombre")
    edad = int(input("edad"))
    año_de_nacimiento = 2025 - edad
    print(f"su nombre es {nombre}")
    print(f"su año de nacimiento fue {año_de_nacimiento:06d}")

# %%
