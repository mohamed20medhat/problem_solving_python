from functions import *
# notice that when importing from an adjacent file. the file name shouldn't start with a number
# the name '8puzzle_functions" is not avilable cause it starts with a number 
from AiSearch import *


def human_solve(puzzle): 
    while(True):
        print_puzzle(puzzle)
        avilable_actions = possible_actions(puzzle) #? create later => it's output should be a list
        print('avilable actions: ' + ' , '.join(avilable_actions)) # convert a list into a string seperated by ' , '
        action = input("your action: ")

        while action not in avilable_actions :
            if action == 'exit' :
                print('thanks for playing')
                return
            print('you typed an unavilable action. please type one of the avilable actions')
            action = input("your action: ")

        puzzle = apply_action(puzzle, action) #? take the action and convert the puzzle into it's new form
        if check_puzzle(puzzle): #? check if the problem is solved after appling the actions 
            print_puzzle(puzzle); print("You win"); return 




# human_solve(shuffle(4))
# human_solve(check_shuffled(2))

# # bfs
# soultion, nodes_expanded = bfs(check_shuffled(10), possible_actions, apply_action, check_puzzle)
# print('Soluton: ', soultion)
# print('expaned_nodes: ', nodes_expanded)


# # dfs
# soultion, nodes_expanded = dfs(check_shuffled(5), possible_actions, apply_action, check_puzzle)
# print('Soluton: ', soultion)
# print('expaned_nodes: ', nodes_expanded)



# # ucs
s = ucs(check_shuffled(10), possible_actions, apply_action, check_puzzle, puzzle_cost, get_min)
print('Soluton: ', s['solution'])
print('cost: ', s['cost'])
print('expaned_nodes: ', s['expanded_nodes'])













