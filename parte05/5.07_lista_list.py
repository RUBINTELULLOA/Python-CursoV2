# Tipo de dato compuesto: lista
# Las listas son un tipo de dato dinámico

# 1. Creación de una lista:
numeros = [2, 4, 6, 8, 10]
print('Tipo de dato de la variable numeros:', type(numeros))
print('Cantidad de elementos:', len(numeros))
print('Contenido:', numeros)

print()

# 2. Acceso a los elementos de una lista:
dos = numeros[0]
print('El primer elemento (índice 0) de la lista es:', dos)
diez = numeros[4]
print('El último elemento (índice 4) de la lista es:', diez)

diez = numeros[-1]
print('El último elemento (índice -1) de la lista es:', diez)

print()

subseccion = numeros[1:4]
print('Tipo de dato de la variable subseccion:', type(subseccion))
print('Cantidad de elementos:', len(subseccion))
print('Contenido:', subseccion)

print()

# Acceso con desempaquetamiento:
print('Acceso a datos de una lista con desempaquetamiento:')
cuatro, seis, ocho = subseccion
print(cuatro, seis, ocho)

print()

# Acceso a un índice no existen:
# Izquierda a derecha: 0 hasta n - 1
# Derecha a izquierda: -1 hasta -n

# valor = numeros[8] # Genera ValueError
# valor = numeros[-6] # Genera ValueError

print()

# 2. Modificación de una lista:
print('2. Modificación de elementos de una lista:')
print('El primer elemento (índice 0) de la lista es:', numeros[0])
numeros[0] = 1
print('El primer elemento (índice 0) de la lista es:', numeros[0])

print()

print('El último elemento (índice -1) de la lista es:', numeros[-1])
numeros[-1] = 12
print('El último elemento (índice -1) de la lista es:', numeros[-1])

print()

# Iteración de listas:
# Iteración de lista con ciclo while:
print('Iteración de lista con ciclo while:')

i = 0
while i < len(numeros):
    print('Índice: {} - Valor: {}'.format(i, numeros[i]))
    i += 1

print()

print('Iteración de lista con ciclo while (del último elemento al primero):')

i = len(numeros) - 1
while i >= 0:
    print('Índice: {} - Valor: {}'.format(i, numeros[i]))
    i -= 1

print()

print('Iteración con índices de una lista con un ciclo for:')

for i in range(0, len(numeros)):
    print('Índice: {} - Valor: {}'.format(i, numeros[i]))

print()

print('Iteración con índices de una lista con un ciclo for (último hacia el primer elemento):')

for i in range(len(numeros) - 1, -1, -1):
    print('Índice: {} - Valor: {}'.format(i, numeros[i]))

print()

print('Iteración por elemento de una lista usando un ciclo for:')

for n in numeros:
    print('Valor: {}'.format(n))

print()

print('Iteración de lista con la función `enumerate()`:')

for i, v in enumerate(numeros):
    print('Índice: {} - Valor: {}'.format(i, v))