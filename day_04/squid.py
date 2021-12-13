from copy import deepcopy
import numpy as np
testing = False
input = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19
3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

class Board: 
    def __init__(self, board): 
        self.board = []
        for line in board.split("\n"): 
            self.board.append([int(elem) for elem in line.strip().split()])

        self.board  = np.asarray(self.board)        
        self.occupied = np.full(self.board.shape , False,  dtype=bool)
        self.solved = False 
    def draw_num(self, num: int):
        ind = np.where(self.board == num) 
        if len(ind[0]) != 0: 
            self.occupied[ind] = True
        
        self.check()

    def check(self): 
        for row in self.occupied: 
            if all(row): 
                self.solved = True
        for col in self.occupied.T: 
            if all(col): 
                self.solved = True
    def calculate_result(self, num): 
        sum = 0

        for i in range(len(self.board)): 
            for j in range(len(self.board[0])): 
                if self.occupied[i][j] == False: 
                    sum += self.board[i][j]
        return sum * num

    def __repr__(self,): 
        for i in range(len(self.board)): 
            print(f"{self.board[i]}\t{self.occupied[i]}")
    
    def __str__(self): 
        res = []
        res.append("-"*75)
        for i in range(len(self.board)): 
            res.append(f'{self.board[i]}\t{self.occupied[i]}')


        return "\n".join(res)
    
    def __eq__(self, other):
        if type(other) != type(self): 
            return False 

        for i in range(len(self.board)): 
            for j in range(len(self.board[0])): 
                if self.board[i][j] != other.board[i][j]: 
                    return False 

        return True


def read_data():

    with open("input.txt") as f: 
        input = f.read().strip()
    input = input.split("\n\n")

    nums = [int(elem) for elem in input[0].strip().split(",")] 

    boards = []
    
    for board in input[1: ]: 
        boards.append(Board(board))
    
    return nums, boards


def pt_1(): 

    nums, boards = read_data()
    winning_board = None 
    winning_num = None
    last_solved = False
    for num in nums: 
        for board in boards: 
            board.draw_num(num)

            if board.solved == True and winning_board == None: 
                winning_board = deepcopy(board) 
                winning_num = num 
                break 
    return winning_board.calculate_result(winning_num)

def pt_2(): 

    nums, boards = read_data()
    winning_board = None
    winning_num = None
    last_solved = False
    for num in nums: 
        for i in range(len(boards)-1, -1, -1): 
            boards[i].draw_num(num)

            if boards[i].solved ==True and len(boards) > 1:
                del boards[i]

            elif boards[i].solved == True and len(boards) == 1: 
                winning_board = deepcopy(boards[i])
                winning_num = num 
                last_solved = True
                break 

        if last_solved: 
            break 
    return winning_board.calculate_result(winning_num)


if __name__ == "__main__": 
    print(f'Part 1: {pt_1()}') 
    print(f'Part 2: {pt_2()}') 
