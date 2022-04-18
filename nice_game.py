#gra w kolko i krzyżyk
#user kontra komputer


NUM_SQUARES = 9
EMPTY = " "
remis = "remis"
O = 'O'
X = 'X'



def display_hello():
    """Wyswietl instrukcje gry """
    print('''          
                    Witaj ! oto gra w kółko i krzyżyk.Zapraszam Cie do rozgrywki pomiedzy mną komputerem, a
                    Tobą człowiekiem 
                    
                    
                    twoj ruch będzie wskazywany poprzez wybranie numeru pola na planszy, 
                    która wygląda tak:
                            
                            
                            0 | 1 | 2
                            --------- 
                            3 | 4 | 5 
                            ---------
                            6 | 7 | 8 
                            
                    Mam nadzieje, że jesteś gotów na porażke :) Zczynajmy ! ''')

def ask_yes_no(question):
    '''Zdaj pytanie na które mozna odpowiedziec tak lub nie '''
    response = None
    while response not in ('t','n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    '''Popros o cyfre w danym zakesie '''
    response = None
    while response not in range (low,high):
        response = int(input(question))
    return response


def first_move():
    '''Ustal do kogo należy pierwszy ruch '''
    go_first = ask_yes_no("\t\tczy chcesz miec prawo do pierwszego ruchu?  t/n ")
    if go_first == 't':
        print('\t\tPierwszy ruch należy do Ciebie graczu!')
        human = X
        computer = O
    else:
        print('\t\tOk, a więc zaczynam ja, Przygotuj sie graczu !')
        human = O
        computer = X
    return computer, human



def new_board():
    '''Utworz nowa plansze gry'''
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    '''Wyswietl plansze na ekranie'''
    print( f'''
                {board[0]} | {board[1]} | {board[2]}
                -----------
                {board[3]} | {board[4]} | {board[5]}
                -----------
                {board[6]} | {board[7]} | {board[8]}
''')



def legal_moves(board):
    '''Utworz liste prawidlowych ruchow '''
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    '''Ustal zwyciezce '''
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,7),
                   (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return remis

    return None


def human_move(board,human):
    '''Odcztytaj ruch czlowieka'''
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('Jaki będzie twoj ruch (0-8): ', 0, NUM_SQUARES)
        if move not in legal:
            print('\nTo pole jest, już zajęte cwaniaku, wybierz inne pole')
    print('\n Bardzo ładnie')
    return move


def computer_move(board, computer,human):
    '''Spowoduj wybranie ruchu przez komputer'''
    #tworze kopie roboczą, ponieważ funcja będzie manipulować listą
    board = board[:]

    # najlepsze pozycje do utworzenia wg kolejnosci
    BEST_MOVES =  (4, 9, 2, 6, 8, 1, 3, 5, 7)
    print("wybieram pole numer", end=" ")

    #sprawdzam czy dany ruch da zwyciestwo komputerowi
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #ten ruch zostal spraawdzony, wycofuje go, aby przyrownac kolejny
        board[move] = EMPTY

    #jesli czlowiek moze wygrac zablokuj ten ruch
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # ten ruch zostal sprawdzony, wycowfuje go, aby przyownac kolejny
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return(move)


def next_turn(turn):
    '''Zamien wykonawce ruchu'''
    if turn == X:
        return O
    else:
        return X


def the_winner_display (computer, human, winner):
    if winner == computer:
        the_winner = 'computer'
    elif winner == human:
        the_winner = 'human'
    return the_winner

def congrat_winner(the_winner, computer, human):
    '''Pogratuluj zwyciezcy'''
    if the_winner != remis:
        print(the_winner, 'Jesteś zwyciezcą!')
    else:
        print('Remis\n')

    if the_winner == computer:
        print('Tak jak sądzilem wygrany może być tylko jeden, kolejny raz nie możesz sie ze mną równac')
    elif the_winner == human:
        print('Jakims cudem udalo Ci sie wygrac! Ciesz sie to był raczej ostatni raz')
    elif the_winner == remis:
        print('Mialeś dużo szcześcia, albo ja gorszy dzień, udało Ci sie zremisować ')


def main():
    display_hello()
    computer, human = first_move()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer,human)


# rozpocznij gre
main()
input('\n\nAby zakończyć gre naciśnij klawisz Enter')