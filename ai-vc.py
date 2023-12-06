import matplotlib.pyplot as plt
import random
import heapq
import numpy as np


class WorldMap:
 
    def __init__(self, rows, cols, num_dirt_blocks, num_obs):
        self.rows = rows
        self.cols = cols
        self.num_dirt_blocks = num_dirt_blocks
        self.num_obs = num_obs
        self.world_map = [['clean' for _ in range(cols)] for _ in range(rows)]

        self.agent_positions = {}  # Dictionary to store agent positions

        # Place dirt blocks randomly on the map
        for _ in range(num_dirt_blocks):
            row = random.randint(0, rows - 1)
            col = random.randint(0, cols - 1)
            while self.world_map[row][col] == 'dirt' or self.world_map[row][col] == 'agent':
                row = random.randint(0, rows - 1)
                col = random.randint(0, cols - 1)
            self.world_map[row][col] = 'dirt'

        # Place obstacles randomly on the map (excluding corners)
        for _ in range(num_obs):
            row = random.randint(1, rows - 2)  # Avoid corners
            col = random.randint(1, cols - 2)  # Avoid corners
            while self.world_map[row][col] == 'dirt' or self.world_map[row][col] == 'agent' or self.world_map[row][col] == 'obs':
                row = random.randint(1, rows - 2)  # Avoid corners
                col = random.randint(1, cols - 2)  # Avoid corners
            self.world_map[row][col] = 'obs'

    def add_agent(self, agent_id):
        while True:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if self.world_map[row][col] == 'clean':
                self.world_map[row][col] = 'agent'
                self.agent_positions[agent_id] = (col,row)
                break


    def getAgentPos(self, agent_id):
        if agent_id in self.agent_positions:
            return self.agent_positions[agent_id]
        else:
            return None  # Agent not found

    def move_agent(self, agent_id, new_position):
        if agent_id in self.agent_positions:
            current_position = self.agent_positions[agent_id]
            if self.world_map[current_position[1]][current_position[0]] == 'agent':
                self.world_map[current_position[1]][current_position[0]] = 'clean'  # Clear the current cell
            self.world_map[new_position[1]][new_position[0]] = 'agent'  # Place the agent in the new cell
            self.agent_positions[agent_id] = new_position  # Update the agent's position
            print(new_position)


    def display_map(self):
        fig,ax = plt.subplots() # Clear the current plot
        for row in range(self.rows):
            for col in range(self.cols):
                if self.world_map[row][col] == 'dirt':
                    ax.plot(col + 0.5,  row + 0.5, 'ro', markersize=10)  # Display dirt as red dots
                elif self.world_map[row][col] == 'agent':
                    ax.plot(col + 0.5, row + 0.5, 'bo', markersize=10)  # Display agents as blue dots
                elif self.world_map[row][col] == 'obs':
                    ax.plot(col + 0.5, row + 0.5, 'ko', markersize=10)  # Display obstacles as black dots

        ax.set_xlim(0, self.cols)
        ax.set_ylim(0, self.rows)

        ax.set_xticks(range(self.cols))
        ax.set_yticks(range(self.rows))
        ax.grid()

    def is_valid_position(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
    

    # for random movement 
    def move_randomly(self,initialP):
        direction = random.choice(['up', 'down', 'left', 'right'])
        # initialP=self.getAgentPos(Agent_id)
        initialPos=list(initialP)
        new_position=initialPos
        print(initialPos,direction)
        if direction == 'up' and self.is_valid_position(new_position[1] , new_position[0]-1):
            initialPos[0] -= 1
            print(initialPos)
        elif direction == 'down' and self.is_valid_position(new_position[1] , new_position[0]+1):
            initialPos[0] += 1
            print(initialPos)
        elif direction == 'left' and self.is_valid_position(new_position[1] -1, new_position[0]):
            initialPos[1] -= 1
            print(initialPos)
        elif direction == 'right' and self.is_valid_position(new_position[1]+1 , new_position[0]):
            initialPos[1] += 1
            print(initialPos)
        self.move_agent('A',initialPos)

        return initialPos
    
world = WorldMap(5,5,10,3)
world.add_agent('A')
print(world.world_map)

world.display_map()
initialPosi=world.getAgentPos('A')
for _ in range(4):
    initialPosi =world.move_randomly(initialPosi)
    print(world.world_map)

    world.display_map()
    plt.show()