from copy import deepcopy
import numpy as np
import random

class Node:
    def __init__(self, omok, parent = None):
        self.omok = omok
        self.visited_count = 0
        self.win_count = 0
        self.parent = parent
        self.child_lst = []

    def get_omok(self):
        return self.omok

    def add_child(self, node):
        self.child_lst.append(node)

    def get_child_lst(self):
        return self.child_lst

    def get_parent(self):
        return self.parent

    def is_leaf(self):
        return len(self.get_child_lst())==0


class MCTS:
    def __init__(self, omok):
        self.root = Node(omok)
        self.player = omok.cur_player()

    def expand(self, node):
        omok = deepcopy(node.get_omok())
        possible_actions = omok.get_blanks()
        x,y = random.choice(possible_actions)
        omok.mark(x,y)
        new_node = Node(omok, node)
        node.add_child(new_node)
        return new_node

    def select(self):
        cur_node = self.root
        while not cur_node.is_leaf():
            child_lst = cur_node.get_child_lst()
            max_score = 0
            max_idx = 0
            for i in range(len(child_lst)):
                cur_score = self.UCB1(child_lst[i])
                if cur_score > max_score:
                    max_score = cur_score
                    max_idx = i
            cur_node = child_lst[i]
        return cur_node

    def simulate(self, node):  # Random Simulation
        omok = deepcopy(node.get_omok())
        count = 0
        while not omok.is_end():
            print count,
            count += 1
            blanks = omok.get_blanks()
            x,y = random.choice(blanks)
            last_player = omok.cur_player()
            omok.mark(x,y)

        if self.player == last_player:
            return 1
        else:
            return 0

    def backprop(self, node, sim_result):

        cur_node = node

        while cur_node.get_parent() is not None:
            cur_node.visited_count += 1
            cur_node.win_count += sim_result
            cur_node = cur_node.parent


    def UCB1(self, node):
        xi = float(node.win_count)/float(node.visited_count)
        ni = node.visited_count
        return xi + np.sqrt(2.0/ni)

    def print_tree_shape(self):

        print self.root.visited_count
        for node in self.root.child_lst:
            print node.visited_count,