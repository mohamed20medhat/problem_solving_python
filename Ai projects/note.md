- the algorithm explained in !1:13 
- conclusion !1:25
- [A* Pathfinding Visualization Tutorial - Python A* Path Finding Tutorial](https://youtu.be/JtiK0DOeI4A)
- [Priority Queue | Data Structure | Python Tutorials](https://youtu.be/wRvOzgt2ygs)

# Problem explanation 
- we want to design a simple game or simulation using pygame. That looks like a grid that I can specify the start position and the end position. And it applies a* algorithm on it and shows the optimal path.


##### Window = grid
- We make a window and turn it into a grid that contains Nodes. Each node must store its position in the grid. (row, col), It's width. And it's state

##### State meaning 
- We can use colors to denote the different states. 
- Start node ⇾ orange 
- end node ⇾ turquoise
- barriers ⇾ black
- Possible paths ⇾ Red "path that I considered and calculated it's F score" "closed path"
- optimal path ⇾ purple 
- Open spots on the borders of the path ⇾ Green  



# Helper functions and their role 
- Each node should contain its available neighbors too. All the surrounding nodes that are not barriers, so we make a function that set this in the beginning of execution ⇾ ***update_neighbors***
- we will need a function that tell us How close are we to the goal. *Heuristic Function* ⇾ we will use Manhattan distance. (X1-X2) + (Y1-Y2) ⇾ ***h***
- After finding the optimal path. We will trace where it came from. And color it purple ⇾ ***reconstruct_path***
- we will need a function that makes a 2d list that will form the grid. And contain all the nodes, also creating the nodes ⇾ ***make_grid***
- we will need a function that draws the grid, draw the grid first then update it with the state of the nodes and their colors in each frame ⇾ ***draw***
- we will need a function that tells us where did the user click in the grid. Returns the rows and columns. So we can use these credentials to find the corresponding spot ⇾ ***get_clicked_position***




# Algorithm explanation 
- F = G + H == "the previous cost that I've taken + the approximated cost to the goal"
- G ⇾ Current shortest distance to get from the start node to THIS node *previous path*
- H ⇾ Heuristic function == estimate The distance between this node and the goal node, *how close are we to the goal* 


- Open Set ⇾ priority queue that keep track of the nodes and their cost. Its main advantage is that it stores the nodes in a priority manner. Not based on when you added them like a normal queue. And we will tie this priority to the least cost. So nodes with the least cost are used first before trying nodes with higher costs 
- priority queue = {(F, count, neighbors), ....}→this is where we store the neighbors of the current node 
- came from → a set that stores the path that we take to the goal
- count ⇾ the number of nodes that were expanded. And found their h, g score
- Priority queue is efferent for finding the node with the highest priority. But I can't traverse it. To know what's in it. That's why we will use a normal set and sync it with the queue. So, 
	- if we added a node once. We don't add it again 
	- also we can find if it contains the end directly. And terminate the algorithm
- we initiate the cost to all nodes = infinity. Then we will do the calculation 
- 


- At the beginning, we look at the neighbors of the start node. All of their initial values are infinity. Then we calculate the cost to reach the neighbors G. And the approximated cost to reach the goal from the neighbors H. Then we compare them. And choose the one with the least total F
- then we make the node that we choose the current node. And do the previous process again. Check its neighbors and calculate their total cost F. and choose the one with the least cost again. 
- Repeat this, till you reach the goal node. 
- As soon as the goal node exits the priority queue. We reconstruct the path and the algorithm terminates 
- 


# The main function 
- left mouse key click ⇾ put spots || start, end, barriers
- right mouse key click ⇾ reset spots || delete spots 
- space bar ⇾ start the algorithm
- c ⇾ reset the grid 
- pressing the x in the window will end the execution 




