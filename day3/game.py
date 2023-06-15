theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
# 打印棋盘
printBoard(theBoard)

turn = 'x'
for i in range(9):
    printBoard(theBoard)
    print("True for " + turn + ". Move on which space?")
    move = input()
    theBoard[move] = turn
    if turn == "x":
        turn = 'o'
    else:
        turn = 'x'


