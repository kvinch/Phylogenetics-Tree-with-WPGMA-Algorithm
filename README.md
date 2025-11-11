## Árboles filogenéticos utilizando el algoritmo WPGMA con diferentes estructuras de datos

## Descripción 🕹️
Este proyecto implementa algoritmos de **análisis filogenético** utilizando estructuras de datos como `MinHeap` y `HashTable`.  
Permite construir árboles evolutivos a partir de matrices de distancias mediante el método **WPGMA**.

## Instalación ⚙️
1. Clona este repositorio con el comando: *git clone https://github.com/kvinch/ProyectoED2.git*.
2. Entra a la carpeta del proyecto e instala los requerimientos (opcionales): *pip install -r requerimientos.txt*.
3. Ejecuta el programa principal que está en main.py. Puedes cambiar las secuencias de OTUS de acuerdo a tu agraado.

## Ejemplo 📄

- Tienes unas secuencias de OTUS = ["ATCGATCGATCGAT",
    "ATCGATCGATCGAA",
    "ATCGATCGATCAAA",
    "ATCGATCGAACAAA",
    "TACGTACGTACGTC",
    "CATGTACGTACGTA"]
  
- Se crea una matriz de distancias con la fórmula de Jukes-Cantor (1969), *dónde se utiliza la fórmula de correción: -3/4 * log(1 - 4/3*f)*
  
- A partir de esta matriz, se crea la matriz con formato:
[-0.0, 0.08, 0.16, 0.25, 1.08, 1.46]
[0.08, -0.0, 0.08, 0.16, 1.08, 1.08]
[0.16, 0.08, -0.0, 0.08, 1.46, 1.46]
[0.25, 0.16, 0.08, -0.0, 1.08, 1.08]
[1.08, 1.08, 1.46, 1.08, -0.0, 0.25]
[1.46, 1.08, 1.46, 1.08, 0.25, -0.0]

- Finalmente, nos da el resultado del newick (((A:0.04,B:0.04):0.04125,(C:0.04,D:0.04):0.04125):0.53,(E:0.125,F:0.125):0.48625000000000007);
- Como paso opcional, se utilizaron librerías para que ayuden a la visualización del árbol filogenético a partir del newick resultante.
  <img width="1098" height="695" alt="image" src="https://github.com/user-attachments/assets/6af64211-45a0-4c5d-b019-c0b9f104f4d7" />

## Estructura del proyecto 🦖

