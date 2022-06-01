import pygame
from queue import PriorityQueue




WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path finding Visualization")


#* defining global colors so we can use them everywhere 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


#* make each node in the grid. each node have properties and most importantly a color which defines it's state
class Spot: 
  def __init__(self, row, col, width, total_rows):
    self.row = row
    self.col = col 
    self.x = row * width
    self.y = col * width
    self.color = WHITE
    self.neighbors = [] #nodes will be stored as a graph. and each node must be aware of it's neighbors
    self.width = width
    self.total_rows = total_rows
    
  def get_pos(self):
    return self.row, self.col
  
  def is_closed(self):
    return self.color == RED 
  
  def is_open(self):
    return self.color == GREEN
  
  def is_barrier(self):
    return self.color == BLACK
  
  def is_start(self):
    return self.color == ORANGE

  def is_end(self):
    return self.color == TURQUOISE
  
  def reset(self):
    self.color = WHITE
    
  def make_start(self):
    self.color = ORANGE
    
  def make_closed(self):
    self.color = RED
    
  def make_open(self):
    self.color = GREEN
    
  def make_barrier(self):
    self.color = BLACK
    
  def make_end(self):
    self.color = TURQUOISE
    
  def make_path(self):
    self.color = PURPLE
    
  def draw(self, win):
    pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
  
  #* check in all directions to find the spots that aren't barriers 
  def update_neighbors(self, grid):
    self.neighbors = []
    #? not in last row, and the spot below is not a barrier
    if self.row < self.total_rows -1 and not grid[self.row +1][self.col].is_barrier(): 
      self.neighbors.append(grid[self.row +1][self.col]) #add the below spot to the neighbors 
    
    #? not in the first row, and the above spot is not a barrier
    if self.row > 0 and not grid[self.row -1][self.col].is_barrier(): 
      self.neighbors.append(grid[self.row -1][self.col]) #add the above spot to the neighbors
      
    #? not in the last col in the right, and the spot to the right is not a barrier
    # notice that total_rows = total_cols. so we didn't make a new constant for it 
    if self.col < self.total_rows -1 and not grid[self.row][self.col +1].is_barrier(): 
      self.neighbors.append(grid[self.row][self.col +1]) #add the Right spot to the neighbors
      
    #? not in the first col in the left, and the spot to the left is not a barrier
    if self.col > 0 and not grid[self.row][self.col -1].is_barrier():
      self.neighbors.append(grid[self.row][self.col -1]) #add the left spot to the neighbors
      
      
  def __lt__(self, other):
    return False 


#* The heuristic function. manhattan distance. !you can't move diagonally 
# p comes in a tubule form, (x,y)
def h(p1, p2):
  x1, y1 = p1
  x2, y2 = p2
  return abs(x1 - x2) + abs(y1 - y2)


#* draw the path as purple 
def reconstruct_path(came_from, current, draw):
  while current in came_from:
    current = came_from[current]
    current.make_path()
    draw()
  



#* The algorithm
def algorithm(draw, grid, start, end):
  count = 0
  open_set = PriorityQueue()
  open_set.put((0, count, start)) #add the start node
  came_from = {} #keep track of each path. to choose the best path in the end 
  
  #? we don't know the path cost to each of the neighbors. so lets assume it = infinity
  g_score = {spot: float("inf") for row in grid for spot in row}
  g_score[start] = 0
  
  #? we don't know the cost from each neighbor to the goal. so lets assume it = infinity 
  f_score = {spot: float("inf") for row in grid for spot in row}
  f_score[start] = h(start.get_pos(), end.get_pos()) #distance between start and end
  
  #?using a set to be able to know what's in the priority queue. cause we can't know what's in it unless we traverse it
  open_set_hash = {start} 
  
  #? event loop for the algorithm execution
  while not open_set.empty():
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        
    current = open_set.get()[2] #{f_score, count, node} =>[2] == node
    open_set_hash.remove(current) #sync it with the with the priority queue

    if current == end: #found the path -> we use the open_Set_hash. to know when to terminate the algorithm
      reconstruct_path(came_from, end, draw)
      end.make_end()
      return True 
    
    #? loop over each neighbor and find the one with the least previous path cost 
    for neighbor in current.neighbors: 
      temp_g_score = g_score[current] + 1 # +1 means that the actual cost to move from a node to the neighbor = 1 
    
      if temp_g_score < g_score[neighbor]:
        came_from[neighbor] = current #add it to came_from
        g_score[neighbor] = temp_g_score
        f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
        if neighbor not in open_set_hash : #add node to the queue and the set
          count +=1 
          open_set.put((f_score[neighbor], count, neighbor))
          open_set_hash.add(neighbor)
          neighbor.make_open()

    draw()
    if current != start: 
      current.make_closed()

  return False





#* we will need a 2d list that will make the grid. and contain all the nodes. 
def make_grid(rows, width):
  grid = []  #will be 2d grid. to make the whole window
  gap = width // rows   #get the width of each cube
  for i in range(rows):
    grid.append([])
    for j in range(rows):
      spot = Spot(i, j, gap, rows) #(row_pos, col_pos, spot_width, total_rows of the grid)
      grid[i].append(spot)
      
  return grid

    
#* draw the horizontal & vertical lines of the grid
def draw_grid(win, rows, width):
  gap = width // rows 
  for i in range(rows):
    pygame.draw.line(win, GREY, (0, i * gap), (width, i*gap)) #draw horizontal lines of the grid
    for j in range(rows):
      pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width)) #draw vertical lines of the grid



#* draw each spot as a cube with the color of the spot
def draw(win, grid, rows, width):
  win.fill(WHITE)  #redraw every frame in it's current/new state after each update on the states
 
  for row in grid:  #for each spot draw a cube with the color of the spot
    for spot in row: 
      spot.draw(win)
      
  draw_grid(win, rows, width) #draw the grid above the colored cubes of the spots
  pygame.display.update()
  

#* get the position where you click with the mouse on the grid
def get_clicked_pos(pos, rows, width):
  gap = width // rows 
  y, x = pos
  
  row = y // gap
  col = x // gap
  
  return row, col
  
  
#* main function containing the event loop
def main(win, width):
  ROWS = 50
  grid = make_grid(ROWS, width)
  start = None 
  end = None
  run = True
  
  
  
  while run: 
    draw(win, grid, ROWS, width)
    for event in pygame.event.get():   #keypress or timer || main event loop
      if event.type == pygame.QUIT:
        run = False
        
      
      #* left mouse key => put spots
      if pygame.mouse.get_pressed()[0]:  
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, ROWS, width) 
        spot = grid[row][col]  # get the spot where you clicked  
        if not start and spot != end: #?if you didn't specify a start before. make this clicked spot the start
          start = spot
          start.make_start()
        elif not end and spot != start:  #?if you didn't specify an end before. make this clicked spot the end
          end = spot
          end.make_end()
        elif spot != end and spot != start: #?if you specified the start and end before. make the spot a barrier
          spot.make_barrier()
          
      #* right mouse key => reset//delete spots to white
      elif pygame.mouse.get_pressed()[2]:   
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos, ROWS, width)
        spot = grid[row][col]  # get the spot where you clicked
        spot.reset()  #? rest ordinary spots 
        if spot == start:  #? reset start
          start = None
        elif spot == end:  #? reset end
          end = None
      
      #* start the algorithm if you press spacebar and already specified the start and end
      if event.type == pygame.KEYDOWN: #? check for spacebar key press to start the algorithm
          if event.key == pygame.K_SPACE and start and end : 
            for row in grid:
              for spot in row:
                spot.update_neighbors(grid) #for each spot in the grid find all the available neighbors
          
            algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
            
            
          if event.key == pygame.K_c : #? check for c keypress to reset the grid
            start = None
            end = None
            grid = make_grid(ROWS, width)
      
        
      
        
  pygame.quit()
  
  
main(WIN, WIDTH)
  
  
  
  
  
  
  
  
  
  
  
  
  












  
    
    



















