def solve(puzzle):

    def print_field(field):
        for row in field:
            print(*row, sep=" ")

    def find_empty(field):
        emptyi, emptyj = -1, -1
        for i in range(9):
            for j in range(9):
                if field[i][j] == 0:
                    emptyi, emptyj = i, j
        return emptyi, emptyj

    def find_possible_num(field, emptyi, emptyj):
        canuse = [True] * 10
        for i in range(9):
            if field[emptyi][i] != 0:
                canuse[field[emptyi][i]] = False
            if field[i][emptyj] != 0:
                canuse[field[i][emptyj]] = False

            bi, bj = emptyi // 3 * 3 + 1, emptyj // 3 * 3 + 1

            for di in range(bi-1, bi+2):
                for dj in range(bj-1, bj+2):
                    canuse[field[di][dj]] = False
        return canuse

    def rec(field):
        emptyi, emptyj = find_empty(field)

        if emptyi == -1 and emptyj == -1:
            global answer
            answer = [" ".join([str(x) for x in row]) for row in field]
            print_field(field)
            return

        canuse = find_possible_num(field, emptyi, emptyj)

        for i in range(1, 10):
            if canuse[i]:
                field[emptyi][emptyj] = i
                rec(field)

        field[emptyi][emptyj] = 0

    rec(puzzle)


if __name__ == "__main__":
    puzzle = [[0, 0, 6, 1, 0, 0, 0, 0, 8],
              [0, 8, 0, 0, 9, 0, 0, 3, 0],
              [2, 0, 0, 0, 0, 5, 4, 0, 0],
              [4, 0, 0, 0, 0, 1, 8, 0, 0],
              [0, 3, 0, 0, 7, 0, 0, 4, 0],
              [0, 0, 7, 9, 0, 0, 0, 0, 3],
              [0, 0, 8, 4, 0, 0, 0, 0, 6],
              [0, 2, 0, 0, 5, 0, 0, 8, 0],
              [1, 0, 0, 0, 0, 2, 5, 0, 0]]
    solve(puzzle)