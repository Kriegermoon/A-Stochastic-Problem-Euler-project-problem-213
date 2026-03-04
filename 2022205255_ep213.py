import time



begin = time.time()

import numpy as np # to taking a power of matrix we need this library

transition_matrix = [[0 for _ in range(900)] for _ in range(900)] # Set a  900 x 900 one step transition probability matrix

# We need to find the neighbors of a square so that defining the one step probabilities from the sqaure to neighbors
def find_neighbors(x, y): # control that where a grid is, and define the neighbors of squares

    neighbors = []

    if x > 0: # This means that there is a neighbor in the above
        neighbors.append((x-1, y))

    if x < 29: # This means that there is a neighbor in the below
        neighbors.append((x+1, y))

    if y > 0:  # This means that there is a neighbor in the left
        neighbors.append((x, y-1))

    if y < 29: # This means that there is a neighbor in the right
        neighbors.append((x, y+1))

    return neighbors

# start an iteration to reach every entry of the one step transition matrix
for i in range(900):

    x = i // 30 # This gives us the number of rows 
    y = i % 30 # and this gives us the number of columns in a spesific row
    # Hence (x,y) becomes a representation of a specific sqaure 

    neighbors = find_neighbors(x, y) # find neighbors of the square

    for neighbor in neighbors: # take a neighbor from neighbors so that attaining a probability the transition (x,y) to the neighbor

        j = neighbor[0] * 30 + neighbor[1] # find sqaure representation fo the neighbor

        transition_matrix[i][j] = 1/ len(neighbors) # attain probability, note that the number of neighbors is the number of possible legal moves

transition_matrix = np.array(transition_matrix) # to use numpy library we need to convert our 2D list to an array

power_50_transition_matrix = np.linalg.matrix_power(transition_matrix, 50) # Now we have the 50 step transititon matrix,
# which means that the matrix contains the information of what is the probability that being at (x1,y1) from (x,y) after 50 moves 

# create a list to preserve the probability of no flea in a sqaure for each square
prob_empt_grid = []

# There are 900 sqaures in the grid, and the 50 step transition matrix contains the probability of reaching ith sqaure from jth sqaure for all sqaures. 
# For example, we need to find the probability of no flea in first sqaure after 50 steps.
# Look at the 50 step transition matrix jth row 1st column for each j, and calculate (1-Pj1) for each j, where Pj1 denotes the probability strating from jth sqaure to 1st sqaure
# This gives us the the probability that a flea starting from jth sqaure does not reach the first sqaure
# Calculate this for all sqaure , and multiply all of them because they are independetn events. 
# So the results gives us the probability there is no flea in the first sqaure after 50 moves
# Do it for all sqaure, and sum

for end_sqaure in range(900):
    prob = 1
    for starting_sqaure in range(900):
        prob = prob * (1 - power_50_transition_matrix[starting_sqaure][end_sqaure]) 
    
    prob_empt_grid.append(prob)

expectation = round(np.sum(prob_empt_grid), 6)

print(expectation)

end = time.time()

print(f"Finished in {end - begin} seconds.")