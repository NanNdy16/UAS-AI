import matplotlib.pyplot as plt
from collections import deque

# Representasi labirin
maze = [
    ['S', '0', '1', '0', 'E'],
    ['1', '0', '1', '0', '1'],
    ['1', '0', '0', '0', '1'],
    ['1', '1', '1', '0', '1'],
    ['1', '1', '1', '0', '1'],
]

# Fungsi mencari posisi awal atau akhir
def find_position(maze, target):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == target:
                return (i, j)
    return None

# Validasi langkah
def is_valid(maze, visited, x, y):
    return (0 <= x < len(maze)) and (0 <= y < len(maze[0])) and \
           maze[x][y] != '1' and not visited[x][y]

# Algoritma BFS
def bfs_maze(maze):
    start = find_position(maze, 'S')
    end = find_position(maze, 'E')
    
    queue = deque()
    visited = [[False]*len(maze[0]) for _ in range(len(maze))]
    
    queue.append((start, [start]))
    visited[start[0]][start[1]] = True
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # atas, bawah, kiri, kanan

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(maze, visited, nx, ny):
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)]))
    
    return None

# Fungsi menggambar labirin + jalur solusi
def draw_maze_with_path(maze, path):
    nrows, ncols = len(maze), len(maze[0])
    fig, ax = plt.subplots(figsize=(6, 6))

    # Warna untuk setiap sel
    color_map = {
        '1': 'black',   # dinding
        '0': 'white',   # jalan
        'S': 'blue',    # start
        'E': 'yellow'   # end
    }

    # Gambar sel
    for i in range(nrows):
        for j in range(ncols):
            val = maze[i][j]
            color = color_map.get(val, 'white')
            rect = plt.Rectangle([j, nrows-i-1], 1, 1, facecolor=color, edgecolor='gray')
            ax.add_patch(rect)

    # Gambar jalur solusi (jika ada)
    if path:
        for step in path:
            x, y = step[1], nrows - step[0] - 1
            circ = plt.Circle((x + 0.5, y + 0.5), 0.2, color='red')
            ax.add_patch(circ)

    # Konfigurasi tampilan
    ax.set_xlim(0, ncols)
    ax.set_ylim(0, nrows)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    plt.title("Visualisasi Labirin dan Jalur Tercepat")
    plt.show()

# Jalankan program
solution_path = bfs_maze(maze)
if solution_path:
    print("Rute ditemukan dalam", len(solution_path)-1, "langkah:")
    for step in solution_path:
        print(step)
else:
    print("Tidak ada rute ditemukan.")

draw_maze_with_path(maze, solution_path)
