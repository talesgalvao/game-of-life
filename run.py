import os
import random
import time

clear = lambda: os.system('clear')

class GameOfLife:

    run = True
    qty_live = 0
    max_interarion = 10
    current_interation = 0
    gap_interaction = 0.10
    board_size = { 'x': 11, 'y': 11 }
    board = []

    def __init__(self):
        clear()

        for x in range(self.board_size['x']):
            self.board.append([])
            for y in range(self.board_size['y']):
                self.board[x].append(False)

        for x in range(self.board_size['x']):
            for y in range(self.board_size['y']):
                if random.randint(0, 4) > 3:
                    self.board[x][y] = True

        # current = {'l' : 0, 'r' : 10, 'd' : 'foward'}
        # for x in range(11):
        #     self.board[x][current['l']] = True
        #     self.board[x][current['r']] = True
        #     if current['l'] == 5:
        #         current['d'] == 'back'

        #     if current['d'] == 'foward' :
        #         current['l'] += 1
        #         current['r'] -= 1
        #     else:
        #         current['l'] -= 1
        #         current['r'] += 1

        #self.draw();exit()
        #self.debug_board()
        
    def debug_board(self):
        for i in self.board:
            print i
        exit()

    def run(self):
        while self.run:
            clear()
            self.proccess()

            self.current_interation += 1
            time.sleep(self.gap_interaction)

    def convert_cel(self, cel):
        return 'X' if cel == True else '-'

    def proccess(self):
        self.qty_live = 0
        changes = 0
        new_board = []

        alive_neighbors = self.verify_neighbors(1, 1)

        for x in range(self.board_size['x']):
            new_board.append([])
            for y in range(self.board_size['y']):
                alive_neighbors = self.verify_neighbors(x, y)
                if alive_neighbors < 2:
                    current_state = False
                elif alive_neighbors == 2 and self.board[x][y] == False:
                    current_state = False
                elif alive_neighbors == 2 and self.board[x][y] == True:
                    current_state = True
                elif alive_neighbors == 3:
                    current_state = True
                elif alive_neighbors >= 4:
                    current_state = False

                if self.board[x][y] != current_state:
                    changes += 1

                new_board[x].append(current_state)

                if current_state == 1:
                    self.qty_live += 1

        #print new_board
        # self.draw()
        self.board = new_board
        # self.draw()
        # exit()


        if changes == 0:
            self.draw()
            self.run = False
            print "Your system is stable"
        elif self.qty_live > 0:
            self.draw()
        elif self.qty_live == 0:
            self.draw()
            self.run = False
            print "ALL DIED"
        else:
            print "UNDEFINED ERROR"
            self.run = False

    def verify_neighbors(self, x, y):
        alive_neighbors = 0
        #print "alive:"+str(alive_neighbors)

        for range_x in range(x-1, x+2):
            for range_y in range(y-1, y+2):
                if (range_x >= 0 and range_y >= 0) and not (range_x == x and range_y == y ):
                    #print "["+str(range_x)+"]"+"["+str(range_y)+"]"
                    try:
                        if self.board[range_x][range_y] == True:
                            #print "["+str(range_y)+"]"+"["+str(range_y)+"]"
                            #print self.board[range_x][range_y]
                            alive_neighbors += 1
                    except IndexError:
                        pass

        #print "["+str(x)+"]"+"["+str(y)+"]"
        #print "alive:"+str(alive_neighbors)
        
        return alive_neighbors

    def draw(self):
        print "Interections:", self.current_interation
        for row_print in self.board:
            print "".join(map(self.convert_cel, row_print))

GameOfLife().run()