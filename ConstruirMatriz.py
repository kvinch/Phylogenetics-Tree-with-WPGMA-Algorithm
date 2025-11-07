import math

def calcularDiferencias(A, B): #Las longitudes deben ser iguales entre sí
    longitud = len(A) #Saca la longitud del OTUS A
    diff = 0 # Número de diferencias, inicia en 0

    for i in range(longitud): # Se itera para revisar las diferencias
        if A[i] != B[i]:
            diff += 1
            
    diff = diff/longitud #Se revisan el porcentaje de diferencias
    
    #Jukes-Cantor 1969, se calcula la corrección con la fórmula -3/4 * log(1 - 4/3*f)
    if (diff >= 0.75):
        print("No se puede calcular, la distancia saldrá negativa.")
        return None
    

    d = - 3/4 * math.log(1- 4/3 * diff)

    return round(d, 2) #Se redondea para 2 decimales

def construirMatriz(otus):
    n = len(otus) #Se saca el largo de las secuencias
    matriz = []
    for k in range(n):
        fila = [0]*n
        matriz.append(fila) #Se crea una matriz nxn de acuerdo al largo de las secuencias 
    
    for i in range(n):
        for j in range(n):
            di = calcularDiferencias(otus[i],otus[j]) #Se calculan el porcentaje de diferencias entre cada OTUS
            matriz[i][j] = di #La matríz es simétrica, entonces el [i][j] es igual que el [j][i]
            matriz[j][i] = di 
    
    return matriz

def imprimirMatriz(matriz): #Función nomas para imprimir matriz
    for fila in matriz: 
        print(fila)
