#Program tree game checkers 4x4

class TreeNode:
    def __init__(self, name, board_state=None, parent=None):
        self.name = name  # Deskripsi langkah
        self.board_state = board_state # State papan setelah langkah
        self.parent = parent # Referensi ke node parent
        self.children = [] # List node anak
        if parent:
            parent.children.append(self) # Auto-registrasi ke parent
    
    def add_child(self, child_node):
        self.children.append(child_node)

def render_tree(node, indent="", is_last=True): #visual dari tree
    marker = "└── " if is_last else "├── "
    print(indent + marker + node.name)
    
    new_indent = indent + ("    " if is_last else "│   ")
    
    for i, child in enumerate(node.children):
        render_tree(child, new_indent, i == len(node.children)-1)

def initial_board(): #Posisi awal dari pion permainan checker 4x4
    return [
        ['-', 'B', '-', 'B'], #baris 0
        ['-', '-', '-', '-'], #baris 1
        ['-', '-', '-', '-'], #baris 2
        ['W', '-', 'W', '-']  #baris 3
    ]

def print_board(board): #memprint papan checker
    for row in board:
        print(" ".join(row))
    print()

def is_valid(x, y): #cek posisi pion apakah valid
    return 0 <= x < 4 and 0 <= y < 4

def can_move(board, x1, y1, x2, y2, player): #pergerakan maju
    if not is_valid(x2, y2) or board[x2][y2] != '-':
        return False
    dx, dy = x2 - x1, y2 - y1

    # Pergerakan normal: maju diagonal 1 langkah
    # B hanya bisa turun (dx=+1), W hanya bisa naik (dx=-1)
    if player == 'B' and dx == 1 and abs(dy) == 1:
        return True
    elif player == 'W' and dx == -1 and abs(dy) == 1:
        return True
    return False

def can_capture(board, x1, y1, x2, y2, player): #pergerakan menangkap pion lawan
    if not is_valid(x2, y2) or board[x2][y2] != '-':
        return False
    dx, dy = x2 - x1, y2 - y1
    opponent = 'W' if player == 'B' else 'B'

    # Lompatan menangkap: maju diagonal 2 langkah
    # Harus ada pion lawan di tengah
    mx, my = (x1 + x2) // 2, (y1 + y2) // 2
    if not is_valid(mx, my):
        return False

    if (player == 'B' and dx == 2 and abs(dy) == 2) or \
       (player == 'W' and dx == -2 and abs(dy) == 2):
        return board[mx][my] == opponent
    return False

#Menghasilkan daftar semua langkah yang bisa dilakukan oleh pemain ('B' atau 'W'),
#baik gerakan biasa maupun menangkap lawan.
def get_possible_moves(board, player): 
    moves = []
    for x1 in range(4):
        for y1 in range(4):
            if board[x1][y1] == player:
                for dx in [-2, -1, 1, 2]:
                    for dy in [-2, -1, 1, 2]:
                        x2, y2 = x1 + dx, y1 + dy
                        if can_move(board, x1, y1, x2, y2, player):
                            moves.append(((x1, y1), (x2, y2), False)) #pergerakan biasa ditambahkan
                        elif can_capture(board, x1, y1, x2, y2, player):
                            moves.append(((x1, y1), (x2, y2), True)) #pergerakan menangkap ditambahkan
    return moves

def apply_move(board, move): #untuk membuat salinan papan yang baru baru
    (x1, y1), (x2, y2), is_capture = move
    new_board = [row[:] for row in board]
    piece = new_board[x1][y1]
    new_board[x1][y1] = '-'
    new_board[x2][y2] = piece #merubah isi petak setelah pergerakan bidak

    if is_capture:
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2
        new_board[mx][my] = '-' #merubah isi petak jika ada pion yang tertangkap
    return new_board

#men-generate semua langkah langkah
def build_game_tree(parent_node, board, player, depth=0, max_depth=3):
    if depth >= max_depth:
        return
    moves = get_possible_moves(board, player)
    for move in moves:
        (x1, y1), (x2, y2), is_capture = move
        piece = board[x1][y1]
        new_board = apply_move(board, move)
        move_desc = f"{piece}({x1},{y1})→({x2},{y2}){' (C)' if is_capture else ''}"
        child_node = TreeNode(move_desc, new_board, parent_node)
        build_game_tree(child_node, new_board, 'W' if player == 'B' else 'B', depth+1, max_depth)

if __name__ == "__main__":
    board = initial_board()
    print("Papan Awal Checker 4x4:\n")
    print_board(board)

    root = TreeNode("Root (Papan Awal)", board)
    build_game_tree(root, board, 'B', max_depth=5)
    
    print("\nGame Tree:")
    render_tree(root)