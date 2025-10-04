"""Edgar Sebastian Montalvo Duran
    10/10/2025
    Implementacion de Best First Search en python para resolver un laberinto
"""

from collections import deque

INICIO = (0,3)
DESTINO = (4,2)

def Breadth_search(matriz, start, goal):
    filas = len(matriz)
    columnas = len(matriz[0])
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        (i,j),steps=queue.popleft()
        if (i,j) == goal:
            return f"Pasos: {steps}"
        visited.add((i,j))
        for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = i + x, j + y
            if 0<=nx < filas and 0 <= ny < columnas:
                if matriz[nx][ny] == 0 and (nx,ny) not in visited:
                    queue.append(((nx,ny),steps+1))
    return "No hay camino disponible"

matriz = [
    [0,0,1,0,0],
    [1,0,0,0,1],
    [0,1,1,0,1],
    [0,0,1,0,0],
    [1,1,0,0,1]
]



print(Breadth_search(matriz,INICIO,DESTINO))