def isValidPos(laberinto, row, col):
    """
    Verifica si una posición dada es válida en el laberinto.
    """
    rows, cols = len(laberinto), len(laberinto[0])
    if 0 <= row < rows and 0 <= col < cols and laberinto[row][col] != '#':
        return True
    return False

def canRotate(laberinto, row, col):
    """
    Verifica si es posible rotar la barra en la posición dada sin colisionar con obstáculos.
    """
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if not isValidPos(laberinto, r, c):
                return False
    return True

def move(laberinto, row, col, direction):
    """
    Realiza los movimientos permitidos y retorna la nueva posición.
    """
    if direction == 'up':
        if isValidPos(laberinto, row - 1, col):
            return row - 1, col
    elif direction == 'down':
        if isValidPos(laberinto, row + 1, col):
            return row + 1, col
    elif direction == 'left':
        if isValidPos(laberinto, row, col - 1):
            return row, col - 1
    elif direction == 'right':
        if isValidPos(laberinto, row, col + 1):
            return row, col + 1
    return row, col

def solution(laberinto):
    rows, cols = len(laberinto), len(laberinto[0])
    queue = [(0, 0, 'horizontal', 0)]  # (fila, columna, orientación, movimientos)
    visited = set()

    while queue:
        row, col, orientation, moves = queue.pop(0)
        if (row, col, orientation) == (rows - 1, cols - 3, 'horizontal'):
            return moves

        if (row, col, orientation) in visited:
            continue
        visited.add((row, col, orientation))

        # Intentar rotar la barra si es posible
        if canRotate(laberinto, row, col) and orientation == 'horizontal':
            queue.append((row, col, 'vertical', moves + 1))
            queue.append((row, col, 'horizontal', moves + 1))

        # Intentar mover en todas las direcciones
        for direction in ['up', 'down', 'left', 'right']:
            new_row, new_col = move(laberinto, row, col, direction)
            queue.append((new_row, new_col, orientation, moves + 1))

    return -1

laberinto1 = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['#', '.', '.', '.', '#', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
             ['.', '#', '.', '.', '.', '.', '.', '#', '.'],
             ['.', '#', '.', '.', '.', '.', '.', '#', '.']]
print(solution(laberinto1))

laberinto2 = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['#', '.', '.', '.', '#', '.', '.', '#', '.'],
             ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
             ['.', '#', '.', '.', '.', '.', '.', '#', '.'],
             ['.', '#', '.', '.', '.', '.', '.', '#', '.']]
print(solution(laberinto2))
