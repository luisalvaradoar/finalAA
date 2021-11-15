def leer_matriz():
    matriz_texto = open("input.txt", "r")
    matriz = []
    for fila in matriz_texto.read().split("\n"):
        matriz.append([int(i) for i in fila.split(" ")])
    return matriz
A = leer_matriz()
puntos_silla = []
N = len(A)
#revisar esquinas
#esquina superior izquierda
if A[0][0] >= A[1][0] and A[0][0] <= A[0][1]:
    puntos_silla.append((0,0))
elif A[0][0] <= A[1][0] and A[0][0] >= A[0][1]:
    puntos_silla.append((0,0))
#esquina superior derecha
if A[0][N - 1] >= A[0][N - 2] and A[0][N - 1] <= A[1][N - 1]:
    puntos_silla.append((0, N - 1))
elif A[0][N - 1] <= A[0][N - 2] and A[0][N - 1] >= A[1][N - 1]:
    puntos_silla.append((0, N - 1))
#esquina inferior izquierda
if A[N - 1][0] >= A[N - 2][0] and A[N - 1][0] <= A[N - 1][1]:
    puntos_silla.append((N - 1, 0))
elif A[N - 1][0] <= A[N - 2][0] and A[N - 1][0] >= A[N - 1][1]:
    puntos_silla.append((N - 1, 0))
#esquina inferior derecha
if A[N - 1][N - 1] >= A[N - 1][N - 2] and A[N - 1][N - 1] <= A[N - 2][N - 1]:
    puntos_silla.append((N - 1, N - 1))
#revisar laterales verticales
#lateral izquierdo
for i in range(1, N - 1):
    if A[i][0] <= A[i - 1][0] and A[i][0] <= A[i + 1][0] and A[i][0] >= A[i][1]:
        puntos_silla.append((i, 0))
    elif A[i][0] >= A[i - 1][0] and A[i][0] >= A[i + 1][0] and A[i][0] <= A[i][1]:
        puntos_silla.append((i, 0))
#lateral derecho
for i in range(1, N - 1):
    if A[i][N - 1] <= A[i - 1][N - 1] and A[i][N - 1] <= A[i + 1][N - 1] and A[i][N - 1] >= A[i][N - 2]:
        puntos_silla.append((i, N - 1))
    elif A[i][N - 1] >= A[i - 1][N - 1] and A[i][N - 1] >= A[i + 1][N - 1] and A[i][N - 1] <= A[i][N - 2]:
        puntos_silla.append((i, N - 1))
#revisar laterales horizontales
#lateral superior
for i in range(1, N - 1):
    if A[0][i] <= A[0][i - 1] and A[0][i] <= A[0][i + 1] and A[0][i] >= A[1][i]:
        puntos_silla.append((0, i))
    elif A[0][i] >= A[0][i - 1] and A[0][i] >= A[0][i + 1] and A[0][i] <= A[1][i]:
        puntos_silla.append((0, i))
#lateral inferior
for i in range(1, N - 1):
    if A[N - 1][i] <= A[N - 1][i - 1] and A[N - 1][i] <= A[N - 1][i + 1] and A[N - 1][i] >= A[N - 2][i]:
        puntos_silla.append((N - 1, i))
    elif A[N - 1][i] >= A[N - 1][i - 1] and A[N - 1][i] >= A[N - 1][i + 1] and A[N - 1][i] <= A[N - 2][i]:
        puntos_silla.append((N - 1, i))

#revisar centros
for i in range(1, N - 1):
    for j in range(1, N - 1):
        if A[i][j] <= A[i][j - 1] and A[i][j] <= A[i][j + 1] and A[i][j] >= A[i - 1][j] and A[i][j] >= A[i + 1][j]:
            puntos_silla.append((i, j))
        elif A[i][j] >= A[i][j - 1] and A[i][j] >= A[i][j + 1] and A[i][j] <= A[i - 1][j] and A[i][j] <= A[i + 1][j]:
            puntos_silla.append((i, j))

print(len(puntos_silla))
"""
for silla in puntos_silla:
    print('({},{})'.format(silla[0] + 1, silla[1] + 1))"""