import random

class FarmMap:
    """This class is ALREADY DONE - just copy and use it!"""
    
    def __init__(self, num_wheat=10):
        self.size = 9
        self.map = self._create_map()
        self.total_wheat = num_wheat
        self._place_wheat(num_wheat)
    
    def _create_map(self):
        """Creates a 9x9 grid filled with 0"""
        return [[0 for _ in range(self.size)] for _ in range(self.size)]
    
    def _place_wheat(self, num_wheat):
        """Randomly places wheat on the map"""
        placed = 0
        while placed < num_wheat:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.map[y][x] == 0:  # Empty cell
                self.map[y][x] = 1  # Place wheat
                placed += 1
    
    def get_cell(self, x, y):
        """Returns what's at position (x, y): 0=empty, 1=wheat"""
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.map[y][x]
        return -1  # Out of bounds
    
    def remove_wheat(self, x, y):
        """Removes wheat from position (x, y)"""
        if self.map[y][x] == 1:
            self.map[y][x] = 0
            return True
        return False
    
    def count_remaining_wheat(self):
        """Counts how many wheat are left on map"""
        count = 0
        for row in self.map:
            count += sum(row)
        return count
    
    def display(self, robot_x, robot_y):
        """Displays the map with robot position"""
        print("\n    ", end="")
        for i in range(self.size):
            print(f"{i:3}", end=" ")
        print()
        
        for y in range(self.size):
            print(f"{y} ", end="")
            for x in range(self.size):
                if x == robot_x and y == robot_y:
                    print("[ R ]", end="")
                elif self.map[y][x] == 1:
                    print("[ W ]", end="")
                else:
                    print("[ . ]", end="")
            print()
        print()

# TASK 1
# 1.1 CREATE ROBOT FUNCTION
def is_valid_position(x, y):
    if 0 <= x < 9 and 0 <= y < 9:
        return True
    return False

print(f"True = {is_valid_position(5, 5)}")
print(f"False = {is_valid_position(9, 5)}")
print(f"False = {is_valid_position(-1, 5)}")

# 1.2 CALCULATE DISTANCE
def calculate_distance(x1, y1, x2, y2):
    manhattan_distance = abs(x2 - x1) + abs(y2 - y1)
    return manhattan_distance

distance = calculate_distance(0, 0, 3, 4)
print(f"Distance = {distance}")

# 1.3 FIND NEAREST WHEAT
def find_nearest_wheat(farm_map, robot_x, robot_y):
    min_distance = 999
    nearest_wheat = None

    for y in range(9):
        for x in range(9):
            if farm_map.get_cell(x, y) == 1:
                distance = calculate_distance(robot_x, robot_y, x, y)
                if distance < min_distance:
                    min_distance = distance
                    nearest_wheat = (x, y)

    return nearest_wheat
farm = FarmMap(num_wheat=5)
nearest = find_nearest_wheat(farm, 0, 0)
print(f"Nearest wheat is at: {nearest}")


# TASK 2 
# 2.1 Create Robot Class

class Robot:
    def __init__(self, new_x=0, new_y=0):
        self.x = new_x
        self.y = new_y
        self.energy = 100
        self.wheat_collected = 0
    
    def get_position(self):
        return (self.x, self.y)
        
    def move(self, direction):
        new_x = self.x
        new_y = self.y
        if direction == "UP":
            new_y = self.y - 1
        elif direction == "DOWN":
            new_y = self.y + 1
        elif direction == "LEFT":
            new_x = self.x - 1
        elif direction == "RIGHT":
            new_x = self.x + 1
        if is_valid_position(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.energy -= 1
            return True
        return False

    def harvest(self, farm_map):
        if farm_map.get_cell(self.x, self.y) == 1:
            farm_map.remove_wheat(self.x, self.y)
            self.wheat_collected += 1
            return True
        return False

    def get_status(self):
        return {
            "robot at": (self.x, self.y),
            "energy": self.energy,
            "wheat_collected": self.wheat_collected
        }

farm = FarmMap(num_wheat=5)
robot = Robot()
print("========================")
print(robot.get_status())
print(f"robot position: {robot.get_position()}")

robot.move("RIGHT")
print(f"robot position: {robot.get_position()}")
print(f"robot energy: {robot.energy}")

robot.move("DOWN")
robot.move("DOWN")
print(f"robot position: {robot.get_position()}")

result = robot.harvest(farm)
print(f"Harvested: {result}")
print(robot.get_status())

# TASK 3
# 3.1: Move Robot to Target

print("========================")
def move_robot_to(robot, target_x, target_y):
    while robot.x < target_x:
        robot.move("RIGHT")
        print(f"Moving RIGHT... now at {robot.get_position()}")
        farm.display(robot.x, robot.y)
        print(robot.get_status())

    while robot.x > target_x:
        robot.move("LEFT")
        print(f"Moving LEFT... now at {robot.get_position()}")
        farm.display(robot.x, robot.y)
        print(robot.get_status())

    while robot.y < target_y:
        robot.move("DOWN")
        print(f"Moving DOWN... now at {robot.get_position()}")
        farm.display(robot.x, robot.y)
        print(robot.get_status())

    while robot.y > target_y:
        robot.move("UP")
        print(f"Moving UP... now at {robot.get_position()}")
        farm.display(robot.x, robot.y)
        print(robot.get_status())

    print("Robot has reached the target!")
    print(f"Final position: {robot.get_position()}")
    print(f"Final energy: {robot.energy}")

robot = Robot()
farm = FarmMap(num_wheat=5)

move_robot_to(robot, 3, 4)

def patrol_and_harvest(robot, farm_map):
    while farm_map.count_remaining_wheat() > 0 and robot.energy > 0:
        nearest_wheat = find_nearest_wheat(farm_map, robot.x, robot.y)
        if nearest_wheat is None:
            print("No more wheat found!")
            break
        
        target_x, target_y = nearest_wheat
        move_robot_to(robot, target_x, target_y)
        
        if robot.harvest(farm_map):
            print(f"Harvested wheat at {robot.get_position()}!")
        else:
            print(f"No wheat to harvest at {robot.get_position()}!")
        
        print(robot.get_status())
        farm_map.display(robot.x, robot.y)
    
    print("Patrol and harvest complete.")
    print(f"Total wheat collected: {robot.wheat_collected}")
    print(f"Remaining energy: {robot.energy}")

robot = Robot()
farm = FarmMap(num_wheat=10)

print("initial farm state:")
farm.display(robot.x, robot.y)
print(robot.get_status())

patrol_and_harvest(robot, farm)

print("final farm state:")
farm.display(robot.x, robot.y)
print(robot.get_status())
print(f"Wheat remaining on farm: {farm.count_remaining_wheat()}")
