def crossword_puzzle(crossword, words):

    def print_board(board):
        for row in board:
            print(''.join(row))

    def get_poss_locs(board, word):
        length = len(word)
        for i in range(10):
            for j in range(10 - length + 1):
                if all([board[i][j + k] in ['-', word[k]] for k in range(length)]):
                    yield (i, j, 0)
        for i in range(10 - length + 1):
            for j in range(10):
                if all([board[i + k][j] in ['-', word[k]] for k in range(length)]):
                    yield (i, j, 1)

    def revert(board, word, loc):
        length = len(word)
        i, j, axis = loc
        if axis == 0:
            for k in range(length):
                board[i][j + k] = '-'
        else:
            for k in range(length):
                board[i + k][j] = '-'

    def move(board, word, loc):
        length = len(word)
        i, j, axis = loc
        if axis == 0:
            for k in range(length):
                board[i][j + k] = word[k]
        else:
            for k in range(length):
                board[i + k][j] = word[k]

    def solve(board, words):
        if not words:
            print_board(board)
            global answer
            answer = ["".join(x) for x in board]
            return

        word = words.pop()
        for loc in get_poss_locs(board, word):
            move(board, word, loc)
            solve(board, words)
            revert(board, word, loc)
        words.append(word)

    board = [[x for x in row] for row in crossword]
    solve(board, words)


if __name__ == '__main__':
    crossword = [
        "+-++++++++",
        "+-++++++++",
        "+-------++",
        "+-++++++++",
        "+-++++++++",
        "+------+++",
        "+-+++-++++",
        "+++++-++++",
        "+++++-++++",
        "++++++++++"
    ]
    words = ["AGRA", "NORWAY", "ENGLAND", "GWALIOR"]
    crossword_puzzle(crossword, words)
