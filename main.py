import pygame
import sys



BLACK = 0, 0, 0
WHITE = 255, 255, 255
CADET_BLUE = 95, 158, 160
GREEN = 153, 255, 204
PINK = 255, 193, 204


class Solver:
    
    def __init__ (self):
        
        pygame.init()
        pygame.font.init()
        
        pygame.display.set_caption("Sudoku Solver")
        img = pygame.image.load('icon.png')
        pygame.display.set_icon(img)
        

        self.font1 = pygame.font.SysFont("comicsans", 20)
        self.font2 = pygame.font.SysFont("comicsans", 50)

        self.screen = pygame.display.set_mode((650, 450))
        

        self.visual = False # set to true if visualize button clicked or V key pressed

        '''
        self.board = [
            [0, 0 ,0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        '''
        
        self.board = [
            [-8, 0 ,-1, 0, 0, -4, 0, 0, 0],
            [-2, 0, 0, 0, 0, 0, -7, 0, 0],
            [-3, -4, 0, -7, -6, 0, -5, 0, 0],
            [0, 0, -3, 0, 0, -5, -9, 0, -7], 
            [0, 0, 0, -6, -7, -8, 0, -3, -2], 
            [0, -2, -7, 0, 0, -1, 0, 0, 0],
            [0, -3, -2, -4, -9, -7, -8, -6, -5],
            [0, 0, 0, -1, -2, 0, 0, 0, 0],
            [-7, -6, -4, 0, -8, -3, 0, -2, 0]
        ]

        '''self.board = [
            [0, 1 ,6, 0, 0, 5, 3, 0, 0],
            [4, 0, 0, 0, 6, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 1],
            [6, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 3, 0, 8, 0], 
            [0, 9, 7, 0, 5, 0, 0, 0, 4],
            [0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 9, 0, 0, 4, 0, 0],
            [0, 5, 1, 0, 7, 0, 0, 0, 9]
        ]'''
        

        self.draw_grid(self.board)
        
        self.input_row, self.input_column = -1, -1

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # checks for button or grid clicks
                if event.type == pygame.MOUSEBUTTONDOWN:

                    self.test_button_collision(event)

                    self.input_row, self.input_column = self.test_grid_collision(event)
                    if (self.input_row, self.input_column) != (-1, -1):
                        self.draw_grid(self.board)
                        self.highlight_cell(self.input_row, self.input_column)
                
                if event.type == pygame.KEYDOWN:
                    # keys for solve, visualize, hide, and new respectively
                    if event.key == pygame.K_s:
                        self.click_solve()
                    elif event.key == pygame.K_v:
                        self.click_visualize()
                    elif event.key == pygame.K_h:
                        self.click_hide_solution()
                    elif event.key == pygame.K_n:
                        self.click_new()
                    
                    # checks for arrow keys
                    outside_grid = (self.input_row, self.input_column) == (-1, -1)

                    if event.key == pygame.K_LEFT: 
                        if outside_grid:
                            self.input_row, self.input_column = 0, 0
                        elif self.input_column > 0:
                            self.unhighlight_cell(self.input_row, self.input_column)           
                            self.input_column -= 1
                            
                        self.highlight_cell(self.input_row, self.input_column)
                        
                    if event.key == pygame.K_RIGHT:
                        if outside_grid:
                            self.input_row, self.input_column = 0, 0
                        elif self.input_column < 8:
                            self.unhighlight_cell(self.input_row, self.input_column)
                            self.input_column += 1
                            
                        self.highlight_cell(self.input_row, self.input_column)
                       
                            
                    if event.key == pygame.K_UP:
                        if outside_grid:
                            self.input_row, self.input_column = 0, 0
                        elif self.input_row > 0:
                            self.unhighlight_cell(self.input_row, self.input_column)
                            self.input_row -= 1
                         
                        self.highlight_cell(self.input_row, self.input_column)
                        

                    if event.key == pygame.K_DOWN:
                        if outside_grid:
                            self.input_row, self.input_column = 0, 0
                        elif self.input_row < 8:
                            self.unhighlight_cell(self.input_row, self.input_column)
                            self.input_row += 1

                        self.highlight_cell(self.input_row, self.input_column)
                        

                    # check for number inputs to grid
                    elif self.input_row != -1 and self.input_column != -1:
                        
                        input = ''
                        if event.key == pygame.K_0:
                            input = '0'
                        elif event.key == pygame.K_1:
                            input = '1'
                        elif event.key == pygame.K_2:
                            input = '2' 
                        elif event.key == pygame.K_3:
                            input = '3' 
                        elif event.key == pygame.K_4:
                            input = '4'
                        elif event.key == pygame.K_5:
                            input = '5' 
                        elif event.key == pygame.K_6:
                            input = '6' 
                        elif event.key == pygame.K_7:
                            input = '7' 
                        elif event.key == pygame.K_8: 
                            input = '8' 
                        elif event.key == pygame.K_9:
                            input = '9'
                        else:
                            continue
                        
                        # insert user inputted number into grid array
                        self.board[self.input_row][self.input_column] = -1 * int(input)
                        
                        self.draw_grid(self.board)
                        
            
            # update display
            pygame.display.flip() 
               


    def solve(self, bo, row, column):
        """
        returns True if sudoku is solved
        param bo: int[][]
        param row: int
        param column: int
        """

        if column == 9:
            if row == 8:
                return True # return True if reached the end of the board 
            
            # if reached end of row, go to beginning of next row
            column = 0
            row += 1

        # if user entered square is encountered, skip it because it is unchangeable
        if bo[row][column] != 0:
            return self.solve(bo, row, column+1)
        
        # recursively tests values 1-9 inclusive for current square on board, returns True if all subsequent squares return True

        for x in range(1, 10):
            if self.is_possible(bo, row, column, x):
                bo[row][column] = x
                
                # if visual is true, print number to screen after every change to board array
                if self.visual:
                    self.highlight_cell(row, column)
                    #bg = pygame.draw.rect(self.screen, BLACK, pygame.Rect(column * 50 + 4, row * 50 + 4, 44, 44))
                    self.draw_grid(bo)
                    #num = self.font1.render(str(bo[row][column]), True, WHITE, BLACK)
                    #self.screen.blit(num, ((column * 50) + 20, (row * 50) + 10))
                    #pygame.display.update([bg, num.get_rect()])
                    pygame.display.flip()

                if self.solve(bo, row, column+1):
                    return True
        
        bo[row][column] = 0 # if all 9 values fail, resets current square


        return False # return False if all 9 values fail, triggers backtracking 


    
    def draw_grid(self, bo):
        '''
        draws grid lines, inserts numbers from board array, and creates buttons
        param bo: int[][]
        '''
        # get rid of previous texts
        self.screen.fill(BLACK)

        # insert numbers to grid from board array
        for r in range(9):
            for c in range (9):
                if bo[r][c] != 0:

                    if bo[r][c] < 0:
                        num = self.font1.render(str(-1 * bo[r][c]), True, PINK, BLACK)
                        self.screen.blit(num, ((c * 50) + 20, (r * 50) + 10))
                    else: 
                        num = self.font1.render(str(bo[r][c]), True, WHITE, BLACK)
                        self.screen.blit(num, ((c * 50) + 20, (r * 50) + 10))
        
        # create buttons
        self.solve_button = self.create_button("Solve", 500, 50)
        self.visualize_button = self.create_button("Visualize", 500, 150)
        self.hide_button = self.create_button("Hide Solution", 500, 250)
        self.new_button = self.create_button("New", 500, 350)


        # draw grid lines
        self.draw_grid_lines()


    
    def test_button_collision(self, event):
        '''
        checks for button clicks
        param event: pygame.event
        '''

        if self.solve_button.collidepoint(event.pos):
            self.click_solve()
         
        if self.visualize_button.collidepoint(event.pos):
            self.click_visualize()

        if self.hide_button.collidepoint(event.pos):
            self.click_hide_solution()
        
        if self.new_button.collidepoint(event.pos):
            self.click_new()
        


    def test_grid_collision(self, event):
        '''
        checks for click on grid, returns position on board array
        param event: pygame.event
        '''
        x, y = event.pos
        row, col = -1, -1
        if x < 450 and y < 450:
            col, row = int(x/50), int(y/50)
        
        return row, col
    
    def highlight_cell(self, row, col):
        '''
        draws box around user selected cell 
        param row: int 
        param col: int 
        '''
        # horizontal lines of box
        pygame.draw.line(self.screen, GREEN, (col * 50, row * 50), (col * 50, (row + 1) * 50), 4)
        pygame.draw.line(self.screen, GREEN, ((col + 1) * 50, row * 50), ((col + 1) * 50, (row + 1) * 50), 4)

        # vertical lines of box
        pygame.draw.line(self.screen, GREEN, (col * 50, row * 50), ((col + 1) * 50, row * 50), 4)
        pygame.draw.line(self.screen, GREEN, (col * 50, (row + 1) * 50), ((col + 1) * 50, (row + 1) * 50), 4)

        pygame.display.flip()

    def unhighlight_cell(self, row, col):
        '''
        gets rid of box around specific cell
        param row: int 
        param col: int 
        '''
        pygame.draw.line(self.screen, BLACK, (col * 50, row * 50), (col * 50, (row + 1) * 50), 4)
        pygame.draw.line(self.screen, BLACK, ((col + 1) * 50, row * 50), ((col + 1) * 50, (row + 1) * 50), 4)

        # vertical lines of box
        pygame.draw.line(self.screen, BLACK, (col * 50, row * 50), ((col + 1) * 50, row * 50), 4)
        pygame.draw.line(self.screen, BLACK, (col * 50, (row + 1) * 50), ((col + 1) * 50, (row + 1) * 50), 4)

        self.draw_grid_lines()


    

    # **** HELPER FUNCTIONS ****

    def draw_grid_lines(self):

        for i in range(1, 9):
            if i % 3 == 0:
                thickness = 7
                color = CADET_BLUE
            else:
                thickness = 1
                color = WHITE

            pygame.draw.line(self.screen, color, (0, i * 50), (450, i * 50), thickness)
            pygame.draw.line(self.screen, color, (i * 50, 0), (i * 50, 450), thickness)


    def is_possible(self, bo, row, column, number):
        """
        checks if number is possible in specific board square
        param bo: int[][]
        param row: int
        param column: int
        param number: int
        """

        for i in range(9):
            # possible in row
            if bo[row][i] == number or bo[row][i] == -1 * number:
                return False
            # possible in column
            if bo[i][column] == number or bo[i][column] == -1 * number:
                return False

        # possible in 3x3 square
        startRow = int(row/3)*3 
        startCol = int(column/3)*3

        for i in range (startRow, startRow+3):
            for j in range(startCol, startCol+3):
                if bo[i][j] == number or bo[i][j] == -1 * number:
                    return False

        return True

    def create_button(self, text, xPos, yPos):
        '''
        Puts button text on screen with given location, returns rect for button
        param text: str 
        param xPos: int 
        param yPos: int 
        '''

        surface = self.font1.render(text, True, BLACK, CADET_BLUE)
        self.screen.blit(surface, (xPos, yPos))
        
        rect = surface.get_rect()
        
        rect.x, rect.y = xPos, yPos
        pygame.Rect.inflate_ip(rect, 7, 7)
        
        pygame.draw.rect(self.screen, CADET_BLUE, rect, 4, 10)
        return rect

    def click_solve(self):
        '''
        Tests if sudoku is valid, solves it if it is, otherwise prints "INVALID SUDOKU"
        '''
        if self.is_valid_sudoku() and self.solve(self.board, 0, 0):
            self.draw_grid(self.board)
        else:
            text = self.font2.render("WANAND IS MAD", True, WHITE, BLACK)
            self.screen.blit(text, (25, 250))
    
    def click_visualize(self):
        '''
        tests if sudoku is valid, solves it if it is, otherwise prints "INVALID SUDOKU," also sets visual boolean to True
        '''
        self.visual = True

        if not self.is_valid_sudoku() or not self.solve(self.board, 0, 0):
            text = self.font2.render("GALOOEH IS MAD", True, WHITE, BLACK)
            self.screen.blit(text, (25, 250))
    
    def click_hide_solution(self):
        '''
        changes only non-initial sudoku values to zero, resets visual boolean to false
        '''
        for row in range(9):
            for col in range(9):
                if self.board[row][col] > 0:
                    self.board[row][col] = 0

        self.draw_grid(self.board)

        self.visual = False

    def click_new(self):
        '''
        Changes all sudoku vals to 0, redraws grid and resets visual boolean to false
        '''
        for row in range(9):
            for col in range(9):
                self.board[row][col] = 0

        self.draw_grid(self.board)

        self.visual = False
    
    
    def is_valid_sudoku(self):
        '''
        Tests if given sudoku is a valid sudoku
        '''
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    continue
                
                num = -1 * self.board[r][c]
                self.board[r][c] = 0
                if not self.is_possible(self.board, r, c, num):
                    return False
                
                self.board[r][c] = -1 * num

        return True

   # ***** UNUSED FUNCTIONS *****
    def display_board(self, bo):
        """
        prints sudoku board in terminal
        param bo: int[][]
        """
        
        for i in range(len(bo)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -") # separate squares horizontally
            
            for j in range(len(bo[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end = "") # separate squares vertically
                
                if j == 8:
                    print(bo[i][j])
                else:
                    print(str(bo[i][j]) + " ", end = "")

                    

Sudoku = Solver()


