class Omok:
    def __init__(self, size, goal_length):
        self.size = size
        self.state = [['_']*size for i in range(size)]
        self.player = 'O'
        self.goal_length = goal_length

    def cur_player(self):
        return self.player

    def show_state(self):
        for row in self.state:
            print row
        print ''

    def get_state(self):
        return self.state

    def flip_player(self):
        if self.player == 'O':
            self.player = 'X'
        elif self.player == 'X':
            self.player = 'O'
        else:
            raise ValueError('Could Not Notice Player Name : ' + self.player)

    def mark(self, row_num, col_num):
        if self.player == 'O':
            self.state[row_num][col_num] = 'O'
            self.flip_player()
            #self.show_state()
        elif self.player == 'X':
            self.state[row_num][col_num] = 'X'
            self.flip_player()
            #self.show_state()
        else:
            raise ValueError('Could Not Notice Player Name : ' + player)

    def get_blanks(self):
        blanks = []
        for i in range(self.size):
            for j in range(self.size):
                if self.state[i][j] != 'O' and self.state[i][j] != 'X':
                    blanks.append((i,j))
        return blanks

    def is_end(self):
        def check_left_right(state, goal_length):
            width, height = len(state), len(state)

            for i in range(height):
                O_count, X_count = 0, 0
                for j in range(width):
                    if state[i][j] == 'O':
                        O_count += 1
                        X_count = 0
                    elif state[i][j] == 'X':
                        X_count += 1
                        O_count = 0
                    else:
                        O_count, X_count = 0, 0

                    if O_count == goal_length or X_count == goal_length:
                        return True
            return False

        def check_up_down(state, goal_length):
            width, height = len(state), len(state)

            for j in range(width):
                O_count, X_count = 0, 0
                for i in range(height):  
                    if state[i][j] == 'O':
                        O_count += 1
                        X_count = 0
                    elif state[i][j] == 'X':
                        X_count += 1
                        O_count = 0
                    else:
                        O_count, X_count = 0, 0

                    if O_count == goal_length or X_count == goal_length:
                        return True
            return False

        # Check "/" type (Right Upward)
        def check_diagonal_type1(state, goal_length):
            width, height = len(state), len(state)
            d_len = height + width - 1

            for i in range(d_len):
                O_count, X_count = 0, 0
                k = min(i, 2*width-i-2)
                for j in range(k+1):
                    if state[k-j][j] == 'O':
                        O_count += 1
                        X_count = 0
                    elif state[k-j][j] == 'X':
                        X_count += 1
                        O_count = 0
                    else:
                        O_count, X_count = 0, 0

                    if O_count == goal_length or X_count == goal_length:
                        return True
            return False

        # Check "\" type (Right Downward)
        def check_diagonal_type2(state, goal_length):
            width, height = len(state), len(state)
            d_len = height + width - 1

            for i in range(d_len):
                O_count, X_count = 0, 0
                k = min(i, 2*width-i-2)
                for j in range(k+1):
                    if state[k-j][width-j-1] == 'O':
                        O_count += 1
                        X_count = 0
                    elif state[k-j][width-j-1] == 'X':
                        X_count += 1
                        O_count = 0
                    else:
                        O_count, X_count = 0, 0

                    if O_count == goal_length or X_count == goal_length:
                        return True
            return False


        # if check_left_right(self.state, self.goal_length):
        #     print 'Left Right'
        # elif check_up_down(self.state, self.goal_length):
        #     print 'Up Down'
        # elif check_diagonal_type1(self.state, self.goal_length):
        #     print 'Diagonal Type1'
        # elif check_diagonal_type2(self.state, self.goal_length):
        #     print 'Diagonal Type2'

        result = check_left_right(self.state, self.goal_length) or check_up_down(self.state, self.goal_length) or \
                 check_diagonal_type1(self.state, self.goal_length) or check_diagonal_type2(self.state, self.goal_length)

        # if result or len(self.get_blanks()) == 0:
        #     if self.player=='X':
        #         print 'O wins'
        #     else:
        #         print 'X wins'
        #     print 'Game Ends'

        return result