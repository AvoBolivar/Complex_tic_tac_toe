def print_board():
    print(top[0], top[1], top[2])
    print(middle[0], middle[1], middle[2])
    print(bottom[0], bottom[1], bottom[2])
    print()


def other_board():
    for i in bd:
        print(i)


def picking_numeric(player, pieces):
    print(player, "you have: ", *pieces)
    print("Which numeric value would you like to use?")
    x = int(input(": "))
    if x in pieces:
        print("bet")
        pieces.remove(x)
    else:
        print("You do not have that piece")
        x = picking_numeric(player, pieces)
    return x, pieces


def insert(player, piece, row, x, column, bd, player_board):
    p = str(piece)
    if player == player_one:
        symbol = "x"
        bd[x-1][column-1] = 1
    else:
        symbol = "o"
        bd[x-1][column - 1] = 2

    row[column-1] = p+symbol
    player_board[x - 1][column - 1] = piece
    return row, bd, player_board


def check_winner(bd):
    winner = False
    n = bd[0][0]
    if n>0:
        for i in range(3):
            if n == bd[i-1][1] and n == bd[i-1][2]:
                winner = True

        for i in range(3):
            if n == bd[1][i-1] and n == bd[2][i-1]:
                winner = True

    if bd[0][0] == bd[1][1] and bd[0][0] == bd [2][2]:
        if bd[0][0] == 1 or bd[0][0] == 2:
            winner = True
            print("first diagnol")
    if bd[0][2] == bd[1][1] and bd[0][2] == bd [2][0]:
        if bd[0][2] == 1 or bd[0][0] == 2:
            winner = True
            print("second diagnol")

    return winner


def pick_location():
    print("Where would you like to play?")
    x = int(input("Enter row: "))
    y = int(input("Enter column: "))
    return x, y


one_pieces = [5, 4, 3, 2, 1]
two_pieces = [5, 4, 3, 2, 1]

top = ["_", "_", "_"]
middle = ["_", "_", "_"]
bottom = ["_", "_", "_"]
board = [top, middle, bottom]

t = [0, 0, 0]
m = [0, 0, 0]
b = [0, 0, 0]
bd = [t, m, b]

p_one_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
p_two_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

player_one = input("Player one insert name: ")
player_two = input("Player two insert name: ")
winner = False
player = player_two
p = two_pieces

while not winner:

    if player == player_one:
        one_pieces = p
        player = player_two
        other_p_board = p_two_board
        p = two_pieces
        player_board = p_one_board
    else:
        two_pieces = p
        player = player_one
        other_p_board = p_one_board
        p = one_pieces
        player_board = p_two_board

    n, p = picking_numeric(player, p)

    x, y = pick_location()
    location = False
    opposite = int(other_p_board[x-1][y-1])
    while not location:
        if board[x - 1][y - 1] == "_":
            print("its blank")
            board[x-1], bd, player_board = insert(player, n, board[x-1], x, y, bd, player_board)
            location = True
        elif int(n) > int(opposite):
            print("checked")
            board[x - 1], bd, player_board = insert(player, n, board[x - 1], x, y, bd, player_board)
            location = True
        else:
            print("This is not a valid location")
            print("please choose another location")
            x, y = pick_location()

    print_board()

    winner = check_winner(bd)

print("Winner: ", player)
