from omok_env import Omok
from mcts import MCTS, Node



import time




omok = Omok(size=10, goal_length=5)
omok.mark(2,3)
omok.mark(2,4)
omok.mark(2,5)


mcts = MCTS(omok)
t1 = time.time()
for i in range(10):
    selected_node = mcts.select()
    new_node = mcts.expand(selected_node)
    sim_result = mcts.simulate(new_node)
    mcts.backprop(new_node, sim_result)
t2 = time.time()

print t2-t1
mcts.print_tree_shape()
# selected_node.omok.show_state()
# selected_node.child_lst[0].omok.show_state()




