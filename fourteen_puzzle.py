import copy;

class Piece:                        #Class for each piece in board, has value and manhattan distance
    def __init__(self, value):
        self.value = int(value);
        self.man_dist = 0;

    def return_value(self):
        return self.value;

    def ret_man_dist(self):
        return self.man_dist;

    def assign_man_dist(self, value):
        self.man_dist=value;

    def __str__(self):
        return str(self.value);

    def __eq__(self, other):
        return self.value == other;

class Board:
    def __init__(self):               #Class for board, which contains 16 piece objects
        fd = open("board.txt");
        temp_board = fd.read().replace('\n', ' ').split(' ');
        temp_board[temp_board.index('0')] = '-1';
        temp_goal_board = temp_board[17:];
        temp_goal_board[temp_goal_board.index('0')] = '-1';
        changeFlag = 1;
        for num in temp_board:
            if (num == '0'):
                num = '-1';
            if (num == '0' and changeFlag == 1):
                num = '-1';
        for num in range(16):
            temp_board[num] = Piece(temp_board[num]);
        collumn = 0;
        self.path_cost = 0;
        row = 0;
        self.tot_man_dist = 0;
        self.board=[];
        self.board.append(temp_board[0:4]);
        self.board.append(temp_board[4:8]);
        self.board.append(temp_board[8:12]);
        self.board.append(temp_board[12:16]);
        for num in range(16):
            temp_goal_board[num] = Piece(temp_goal_board[num]);
        collumn = 0;
        row = 0;
        self.goal_board=[];
        self.goal_board.append(temp_goal_board[0:4]);
        self.goal_board.append(temp_goal_board[4:8]);           #separate goal board array
        self.goal_board.append(temp_goal_board[8:12]);
        self.goal_board.append(temp_goal_board[12:16]);
        fd.close();

    def edge_det(self, piece):                      #returns where in the board the piece is physically
        for row in self.board:
            try:
                curr_row = self.board.index(row);
                if (self.board[curr_row].index(piece) == 0 and curr_row == 0):
                    return "top left";
                elif (self.board[curr_row].index(piece) == 3 and curr_row == 0):
                    return "top right";
                elif ((self.board[curr_row].index(piece) == 1 or
                       self.board[curr_row].index(piece) == 2) and
                      curr_row == 0):
                    return "top edge";
                elif (self.board[curr_row].index(piece) == 0  and
                      (curr_row == 1 or curr_row == 2)):
                    return "left edge"
                elif (self.board[curr_row].index(piece) == 3 and
                      (curr_row == 1 or curr_row == 2)):
                    return "right edge"
                elif (self.board[curr_row].index(piece) == 0 and curr_row == 3):
                    return "bottom left"
                elif (self.board[curr_row].index(piece) == 3 and curr_row == 3):
                    return "bottom right"
                elif ((self.board[curr_row].index(piece) == 1 or
                       self.board[curr_row].index(piece) == 2) and
                      curr_row == 3):
                    return "bottom edge";
                else:
                    return 'center';
            except:
                pass

    def move(self, piece, dir):             #moves piece in the direction of dir, or returns -1 if illegal state
        for row in self.board:
            for curr_piece in row:
                if (curr_piece == piece):
                    curr_row = self.board.index(row);
                    pos = self.edge_det(self.board[curr_row][self.board[curr_row].index(piece)]);
                    if (pos == 'center'): #checks positions
                        if (dir == 'up'): #checks direction
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][self.board[curr_row].index(piece)]
                            self.board[curr_row][curr_col] = self.board[curr_row - 1][curr_col];
                            self.board[curr_row - 1][curr_col] = temp;
                            return 0;
                        elif (dir == 'down'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][curr_col];
                            self.board[curr_row][curr_col] = self.board[curr_row + 1][curr_col];
                            self.board[curr_row + 1][curr_col] = temp;
                            return 0;
                        elif (dir == 'left'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][self.board[curr_row].index(piece)];
                            self.board[curr_row][curr_col] = self.board[curr_row][curr_col - 1];
                            self.board[curr_row][curr_col - 1] = temp;
                            return 0;
                        elif (dir == 'right'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][curr_col];
                            self.board[curr_row][curr_col] = self.board[curr_row][curr_col + 1];
                            self.board[curr_row][curr_col + 1] = temp;
                            return 0;
                        else:
                            return -1;
                    if (pos == 'top left'):
                        if (dir == 'down'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][curr_col];
                            self.board[curr_row][curr_col] = self.board[curr_row + 1][curr_col];
                            self.board[curr_row + 1][curr_col] = temp;
                            return 0;
                        elif (dir == 'right'):
                            try:
                                curr_col = self.board[curr_row].index(piece);
                                temp = self.board[curr_row][curr_col];
                                self.board[curr_row][curr_col] = self.board[curr_row][curr_col + 1];
                                self.board[curr_row][curr_col + 1] = temp;
                                return 0;
                            except:
                                return -1;
                        else:
                            return -1;
                    elif (pos == 'top edge'):
                        if (dir == 'down'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][curr_col];
                            self.board[curr_row][curr_col] = self.board[curr_row + 1][curr_col];
                            self.board[curr_row + 1][curr_col] = temp;
                            return 0;
                        elif (dir == 'left'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][self.board[curr_row].index(piece)];
                            self.board[curr_row][curr_col] = self.board[curr_row][curr_col - 1];
                            self.board[curr_row][curr_col - 1] = temp;
                            return 0;
                        elif (dir == 'right'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][curr_col];
                            self.board[curr_row][curr_col] = self.board[curr_row][curr_col + 1];
                            self.board[curr_row][curr_col + 1] = temp;
                            return 0;
                        else:
                            return -1;
                    elif (pos == 'top right'):
                         if (dir == 'down'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][curr_col];
                            self.board[curr_row][curr_col] = self.board[curr_row + 1][curr_col];
                            self.board[curr_row + 1][curr_col] = temp;
                            return 0;
                         elif (dir == 'left'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][self.board[curr_row].index(piece)];
                            self.board[curr_row][curr_col] = self.board[curr_row][curr_col - 1];
                            self.board[curr_row][curr_col - 1] = temp;
                            return 0;
                         else:
                            return -1;
                    elif (pos == 'left edge'):
                        if (dir == 'down'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][curr_col];
                            self.board[curr_row][curr_col] = self.board[curr_row + 1][curr_col];
                            self.board[curr_row + 1][curr_col] = temp;
                            return 0;
                        elif (dir == 'up'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][self.board[curr_row].index(piece)]
                            self.board[curr_row][curr_col] = self.board[curr_row - 1][curr_col];
                            self.board[curr_row - 1][curr_col] = temp;
                            return 0;
                        elif (dir == 'right'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][curr_col];
                            self.board[curr_row][curr_col] = self.board[curr_row][curr_col + 1];
                            self.board[curr_row][curr_col + 1] = temp;
                            return 0;
                        else:
                            return -1;
                    elif (pos == 'right edge'):
                        if (dir == 'down'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][curr_col];
                            self.board[curr_row][curr_col] = self.board[curr_row + 1][curr_col];
                            self.board[curr_row + 1][curr_col] = temp;
                            return 0;
                        elif (dir == 'up'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][self.board[curr_row].index(piece)]
                            self.board[curr_row][curr_col] = self.board[curr_row - 1][curr_col];
                            self.board[curr_row - 1][curr_col] = temp;
                            return 0;
                        elif (dir == 'left'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][self.board[curr_row].index(piece)];
                            self.board[curr_row][curr_col] = self.board[curr_row][curr_col - 1];
                            self.board[curr_row][curr_col - 1] = temp;
                            return 0;
                        else:
                            return -1
                    elif (pos == 'bottom left'):
                        if (dir == 'up'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][self.board[curr_row].index(piece)]
                            self.board[curr_row][curr_col] = self.board[curr_row - 1][curr_col];
                            self.board[curr_row - 1][curr_col] = temp;
                            return 0;
                        elif (dir == 'right'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][curr_col];
                            self.board[curr_row][curr_col] = self.board[curr_row][curr_col + 1];
                            self.board[curr_row][curr_col + 1] = temp;
                            return 0;
                        else:
                            return -1;
                    elif (pos == 'bottom edge'):
                        if (dir == 'up'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][self.board[curr_row].index(piece)]
                            self.board[curr_row][curr_col] = self.board[curr_row - 1][curr_col];
                            self.board[curr_row - 1][curr_col] = temp;
                            return 0;
                        elif (dir == 'left'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][self.board[curr_row].index(piece)];
                            self.board[curr_row][curr_col] = self.board[curr_row][curr_col - 1];
                            self.board[curr_row][curr_col - 1] = temp;
                            return 0;
                        elif (dir == 'right'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][curr_col];
                            self.board[curr_row][curr_col] = self.board[curr_row][curr_col + 1];
                            self.board[curr_row][curr_col + 1] = temp;
                            return 0;
                        else:
                            return -1;
                    elif (pos == 'bottom right'):
                        if (dir == 'up'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][self.board[curr_row].index(piece)]
                            self.board[curr_row][curr_col] = self.board[curr_row - 1][curr_col];
                            self.board[curr_row - 1][curr_col] = temp;
                            return 0;
                        elif (dir == 'left'):
                            curr_col = self.board[curr_row].index(piece);
                            temp = self.board[curr_row][self.board[curr_row].index(piece)];
                            self.board[curr_row][curr_col] = self.board[curr_row][curr_col - 1];
                            self.board[curr_row][curr_col - 1] = temp;
                            return 0;
                        else:
                            return -1
    def __str__(self):
        temp_board = copy.deepcopy(self.board);  #for debugging
        for row in temp_board:
            for piece in row:
                if (piece.value == -1):
                    piece.value = 0;
        return str(self.board[0][0]) + ' ' + str(self.board[0][1])  + ' '  + \
               str(self.board[0][2])  + ' '  + str(self.board[0][3]) + \
               '\n' + str(self.board[1][0])  + ' '  + str(self.board[1][1])  + ' '  + \
               str(self.board[1][2])  + ' '  + str(self.board[1][3]) +\
               '\n' + str(self.board[2][0]) + ' ' + str(self.board[2][1])  + ' '  + \
               str(self.board[2][2])  + ' '  + str(self.board[2][3]) + \
               '\n' + str(self.board[3][0])  + ' '  + str(self.board[3][1])  + ' '  + \
               str(self.board[3][2])  + ' '  + str(self.board[3][3]);

    def __eq__(self, other):
        temp_board = copy.deepcopy(self.board); #boards are equal based on their corresponding pieces
        for row in temp_board:
            for piece in row:
                if (piece.value == -1): #changes -1s to 0s before checking match
                    piece.value = 0;
        temp_other = copy.deepcopy(other.board);
        for row in temp_other:
            for piece in row:
                if (piece.value == -1):
                    piece.value = 0;
        return (temp_board[0][0] == temp_other[0][0] and temp_board[0][1] == temp_other[0][1]\
                and temp_board[0][2] == temp_other[0][2] and temp_board[0][3] == temp_other[0][3]\
                and temp_board[1][0] == temp_other[1][0] and temp_board[1][1] == temp_other[1][1]\
                and temp_board[1][2] == temp_other[1][2] and temp_board[1][3] == temp_other[1][3]\
                and temp_board[2][0] == temp_other[2][0] and temp_board[2][1] == temp_other[2][1]\
                and temp_board[2][2] == temp_other[2][2] and temp_board[2][3] == temp_other[2][3]\
                and temp_board[3][0] == temp_other[3][0] and temp_board[3][1] == temp_other[3][1]\
                and temp_board[3][2] == temp_other[3][2] and temp_board[3][3] == temp_other[3][3]);

class Node:
    def __init__(self, board, path_cost): #node for tree
        self.board = board;
        self.f = 0; #f value for A*. initialized to zero
        self.f_str = ''; #f values of nodes before current one
        self.childs = [];
        self.level = 0;
        self.tot_man_dist = 0;
        self.parent = [];
        self.path_cost = path_cost;
        self.dir = 'nothing';
        self.path = ''

    def addChild(self, child):
        childs.append(child);

    def removeChild(self):
        try:
            childs.pop(0);
            return 0;
        except:
            return -1;

    def set_tot_man_dist(self): #calculates manhatan distance of node
        tot_man_dist = 0;
        temp = copy.deepcopy(self.board);
        for row in temp.board: #creates deepcopy to avoid changing data
            for piece in row:
                if (piece.value == -1):
                    piece.value = 0;
        for row in temp.goal_board:
            for piece in row:
                if (piece.value == -1):
                    piece.value = 0;
        for row in temp.board:
            for piece in row:
                if (piece.value > 0):
                    curr_row = temp.board.index(row);
                    curr_col = temp.board[curr_row].index(piece);
                    for goal_row in temp.goal_board:
                        try:
                            curr_goal_row = temp.goal_board.index(goal_row);
                            curr_goal_col = temp.goal_board[curr_goal_row].index(piece);
                            row_dif = abs(curr_goal_row - curr_row);
                            col_dif = abs(curr_goal_col - curr_col); #differences in rows/collumns used in calculation
                            tot_man_dist += row_dif + col_dif;
                            piece.man_dist = row_dif + col_dif;
                        except:
                            pass
        self.board.tot_man_dist = tot_man_dist;
        self.tot_man_dist = tot_man_dist;
        return self.tot_man_dist;

    def checkGoal(self): #checks if node is goal node
        temp = copy.deepcopy(self.board);
        for row in temp.board:
            for piece in row:
                if (piece.value == -1):
                    piece.value = 0;
        for row in temp.goal_board:
            for piece in row:
                if (piece.value == -1):
                    piece.value = 0;
        return ((temp.board[0][0].value == temp.goal_board[0][0].value) and\
                (temp.board[0][1].value == temp.goal_board[0][1].value) and\
                (temp.board[0][2].value == temp.goal_board[0][2].value) and\
                (temp.board[0][3].value == temp.goal_board[0][3].value) and\
                (temp.board[1][0].value == temp.goal_board[1][0].value) and\
                (temp.board[1][1].value == temp.goal_board[1][1].value) and\
                (temp.board[1][2].value == temp.goal_board[1][2].value) and\
                (temp.board[1][3].value == temp.goal_board[1][3].value) and\
                (temp.board[2][0].value == temp.goal_board[2][0].value) and\
                (temp.board[2][1].value == temp.goal_board[2][1].value) and\
                (temp.board[2][2].value == temp.goal_board[2][2].value) and\
                (temp.board[2][3].value == temp.goal_board[2][3].value) and\
                (temp.board[3][0].value == temp.goal_board[3][0].value) and\
                (temp.board[3][1].value == temp.goal_board[3][1].value) and\
                (temp.board[3][2].value == temp.goal_board[3][2].value) and\
                (temp.board[3][3].value == temp.goal_board[3][3].value));
    
    def __str__(self):
        return str(self.board);

    def __eq__(self, other):
        return self.board == other.board;


class Graph:
    def __init__(self, node, path): #graph for A* search
        self.root = node;
        self.lowest = node;
        self.curr_path = path;
        self.explored = [];
        self.frontier = [];
        self.goal_found = False; #true if goal is reached

    def createZeroTemp(self, node): #creates a version of board with -1 replaced with 0
        temp = copy.deepcopy(node);
        for row in temp.board.board:
            for piece in row:
                if (piece.value == -1):
                    piece.value = 0;
        for row in temp.board.goal_board:
            for piece in row:
                if (piece.value == -1):
                    piece.value = 0;
        return temp;

    def addExplored(self, node):
        self.explored.append(node);
        return

    def checkExplored(self, node): #checks if node is in explored
        for curr_node in self.explored:
            if curr_node == node:
                return True;
        return False;

    def addFrontier(self, node): #appends frontier
        self.frontier.append(node);
        return

    def checkFrontier(self, node):
        for curr_node in self.frontier:
            if curr_node == node:
                return True;
        return False;

    def update_f(self, node, pc): #sets manhattan distances, path cost, and calculates f
        node.set_tot_man_dist();
        node.path_cost = pc + 1;
        node.f = node.path_cost + node.tot_man_dist;
        node.f_str += str(node.f) + ' ';
        return node;

    def expand(self, node): #expands node
        temp = copy.deepcopy(node);
        for curr_node in self.frontier:
            if curr_node == node:
                self.frontier.remove(curr_node); #removes node being checked from frontier
        self.addExplored(copy.deepcopy(temp)); #adds node to explored
        curr_board0 = copy.deepcopy(temp);
        if (curr_board0.board.move(-1, 'up') != -1): #checks if move is legal
            if (self.checkExplored(curr_board0) == False and self.checkFrontier(curr_board0) == False): #checks if state is in explored or frontier 
                curr_board0 = self.update_f(curr_board0, temp.path_cost);
                curr_board0.path += 'U1 ';
                curr_board0.parent.append(copy.deepcopy(temp));
                node.childs.append(copy.deepcopy(curr_board0.board));
                self.addFrontier(curr_board0); #adds node to frontier if legal and not in explored/frontier
                if (curr_board0.checkGoal()):
                    self.goal_found = True;
                    return
        curr_board1 = copy.deepcopy(temp);
        if (curr_board1.board.move(-1, 'right') != -1):
            if (self.checkExplored(curr_board1) == False and self.checkFrontier(curr_board1) == False):
                curr_board1 = self.update_f(curr_board1, temp.path_cost);
                curr_board1.path += 'R1 ';
                curr_board1.parent.append(copy.deepcopy(temp));
                node.childs.append(curr_board1.board);
                self.addFrontier(curr_board1);
                if (curr_board1.checkGoal()):
                    self.goal_found = True;
                    return
            curr_board1.set_tot_man_dist();
        curr_board2 = copy.deepcopy(temp);
        if (curr_board2.board.move(-1, 'left') != -1):
            if (self.checkExplored(curr_board2) == False and self.checkFrontier(curr_board2) == False):
                curr_board2 = self.update_f(curr_board2, temp.path_cost);
                curr_board2.path += 'L1 ';
                curr_board2.parent.append(copy.deepcopy(temp));
                node.childs.append(copy.deepcopy(curr_board2.board));
                self.addFrontier(curr_board2);
                if (curr_board2.checkGoal()):
                    self.goal_found = True;
                    return
        curr_board3 = copy.deepcopy(temp);
        if (curr_board3.board.move(-1, 'down') != -1):
            if (self.checkExplored(curr_board3) == False and self.checkFrontier(curr_board3) == False):
                curr_board3 = self.update_f(curr_board3, temp.path_cost);
                curr_board3.path += 'D1 ';
                node.childs.append(curr_board3.board);
                curr_board3.parent.append(copy.deepcopy(temp));
                self.addFrontier(curr_board3);
                if (curr_board3.checkGoal()):
                    self.goal_found = True;
                    return
        curr_board4 = copy.deepcopy(temp);
        if (curr_board4.board.move(0, 'up') != -1):
            if (self.checkExplored(curr_board4) == False and self.checkFrontier(curr_board4) == False):
                curr_board4 = self.update_f(curr_board4, temp.path_cost);
                curr_board4.path += 'U2 ';
                node.childs.append(copy.deepcopy(curr_board4.board));
                curr_board4.parent.append(copy.deepcopy(temp));
                self.addFrontier(curr_board4);
                if (curr_board4.checkGoal()):
                    self.goal_found = True;
                    return
        curr_board5 = copy.deepcopy(temp);
        if (curr_board5.board.move(0, 'right') != -1):
            if (self.checkExplored(curr_board5) == False and self.checkFrontier(curr_board5) == False):
                curr_board5 = self.update_f(curr_board5, temp.path_cost);
                curr_board5.path += 'R2 ';
                node.childs.append(curr_board5.board);
                curr_board5.parent.append(copy.deepcopy(temp));
                self.addFrontier(curr_board5);
                if (curr_board5.checkGoal()):
                    self.goal_found = True;
                    return
        curr_board6 = copy.deepcopy(temp);
        if (curr_board6.board.move(0, 'left') != -1):
            if (self.checkExplored(curr_board6) == False and self.checkFrontier(curr_board6) == False):
                curr_board6 = self.update_f(curr_board6, temp.path_cost);
                curr_board6.path += 'L2 ';
                node.childs.append(copy.deepcopy(curr_board6.board));
                curr_board6.parent.append(copy.deepcopy(temp));
                self.addFrontier(curr_board6);
                if (curr_board6.checkGoal()):
                    self.goal_found = True;
                    return
        curr_board7 = copy.deepcopy(temp);
        if (curr_board7.board.move(0, 'down') != -1):
            if (self.checkExplored(curr_board7) == False and self.checkFrontier(curr_board7) == False):
                curr_board7 = self.update_f(curr_board7, temp.path_cost);
                curr_board0.path += 'D2 ';
                node.childs.append(curr_board7.board);
                curr_board7.parent.append(copy.deepcopy(temp));
                self.addFrontier(curr_board7);
                if (curr_board7.checkGoal()):
                    self.goal_found = True;
                    return
        self.lowest = self.frontier[0];
        for curr_node in self.frontier: 
            if curr_node.f <= self.lowest.f: #updates node to be selected with lowest f value
                self.lowest = curr_node;
            
    def search(self): 
        self.update_f(self.root, -1);
        self.addFrontier(self.root);
        while (self.goal_found == False): #expands while goal node is not found
                self.expand(self.lowest);
        fd = open("board.txt", 'a');
        fd.write('\n\n' + str(self.lowest.path_cost) + '\n');
        fd.write(str(len(self.explored) + len(self.frontier)) + '\n');
        fd.write(self.lowest.path + '\n' + self.lowest.f_str);
        fd.close();

    def __str__(self):
        ans = 'Root:\n' + strong(self.root.board) + '\nLevel 1:\n';
        for node in self.frontier:
            ans += str(node.board) + ' Man Dist: ' + str(node.tot_man_dist) \
                   + ' path: ' + str(node.path_cost) + '\n\n';
        return ans;
            
                            
def main():
    board = Board();
    node = Node(board, 0);
    graph = Graph(node, 0);
    graph.search();
    return board;

main();
