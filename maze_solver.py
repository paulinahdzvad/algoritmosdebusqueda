import collections

def solve_maze_bfs(maze, start, end):
    """Resuelve el laberinto usando el algoritmo de Búsqueda en Amplitud (BFS)."""
    rows, cols = len(maze), len(maze[0])
    queue = collections.deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        (curr_row, curr_col), path = queue.popleft()

        if (curr_row, curr_col) == end:
            return path

        # Movimientos posibles: derecha, izquierda, abajo, arriba
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc

            if 0 <= next_row < rows and 0 <= next_col < cols and \
               maze[next_row][next_col] == 0 and (next_row, next_col) not in visited:
                visited.add((next_row, next_col))
                queue.append(((next_row, next_col), path + [(next_row, next_col)]))

    return None  # No se encontró camino


# Laberinto ejemplo
MAZE = [
        [0,1,0,0,0,0,1,0,0,0],
        [0,1,0,1,1,0,1,0,1,0],
        [0,0,0,0,1,0,0,0,1,0],
        [1,1,1,0,1,1,1,0,1,0],
        [0,0,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,1,0,1,0],
        [0,1,1,1,1,0,1,0,1,0],
        [0,0,0,0,1,0,0,0,1,0],
        [0,1,1,0,0,0,1,0,0,0]
    ]

START = (0, 0)
END = (9, 9)
