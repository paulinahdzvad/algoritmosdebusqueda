import streamlit as st
from maze_solver import MAZE, START, END, solve_maze_bfs

st.title("Visualizador de Algoritmo de Búsqueda en Laberinto")

# Función para dibujar el laberinto
def render_maze(maze, path=None):
    if path is None:
        path = []

    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            if (r_idx, c_idx) == START:
                display_row.append("🚀")
            elif (r_idx, c_idx) == END:
                display_row.append("🏁")
            elif (r_idx, c_idx) in path:
                display_row.append("🔷")
            elif col == 1:
                display_row.append("⬛")
            else:
                display_row.append("⬜")
        display_maze.append("".join(display_row))

    st.markdown("<br>".join(display_maze), unsafe_allow_html=True)


# Sidebar
st.sidebar.header("Opciones")
algorithm = st.sidebar.selectbox("Selecciona el algoritmo", ["BFS", "DFS (no implementado)", "A* (no implementado)"])
solve_button = st.sidebar.button("Resolver Laberinto")

# Mostrar laberinto inicial
render_maze(MAZE)

# Lógica del botón
if solve_button:
    if algorithm == "BFS":
        path = solve_maze_bfs(MAZE, START, END)
        if path:
            st.success("¡Camino encontrado con BFS!")
            render_maze(MAZE, path)
        else:
            st.error("No se encontró un camino.")
    else:
        st.warning(f"El algoritmo {algorithm} aún no está implementado.")
