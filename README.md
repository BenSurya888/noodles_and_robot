# 🍜 Instant Noodle Maker & 🤖 Farm Robot Simulation

## 📖 Description
This project contains **two Python simulations**:

1. **Instant Noodle Maker (`noodle.py`)** → simulates an automatic instant noodle cooking machine.
2. **Farm Robot (`robot.py`)** → simulates a robot that harvests wheat in a 9x9 grid farm.

Both are designed for learning **Object-Oriented Programming (OOP)**, simulation logic, and simple automation systems in Python.

---

## 🍜 Instant Noodle Maker Simulation

### ⚙️ Features
- Automatic water filling up to bucket capacity.
- Heating and maintaining water temperature.
- Automatic dispensing of ketchup, sausage, and seasoning powder.
- Cooking noodle simulation with realistic time delay.
- Automatic bucket cleaning.
- Machine status reporting.

### 🧩 Class Structure
- **`WaterSystem`** → Controls water level and temperature.
- **`Dispenser`** → Handles ingredient dispensing and stock tracking.
- **`NoodleMachine`** → Combines all subsystems into a working noodle maker.

### 🚀 How to Run
```bash
python noodle.py
```

### 💡 Learning Concepts
- Object-Oriented Programming (Classes, Methods, Objects)
- Loops and conditional statements
- Time simulation using `time.sleep`
- Sequential automation logic (like robotics)

---

## 🤖 Farm Robot Simulation

### ⚙️ Features
- 9x9 farm grid with randomly placed wheat.
- Robot movement and harvesting system.
- Two modes:
  - **Manual mode** → Control the robot using keyboard input.
  - **Automatic mode** → Robot finds and harvests the nearest wheat.
- Energy-based system for robot actions.
- Real-time map display in terminal.

### 🧩 Class Structure
- **`FarmMap`** → Handles the map generation and wheat placement.
- **`Robot`** → Manages position, energy, and wheat collection.
- **Helper Functions**:
  - `find_nearest_wheat()` → Finds the nearest wheat using Manhattan distance.
  - `move_robot_to()` → Moves robot toward a target coordinate.
  - `patrol_and_harvest()` → Automatic harvesting loop.
  - `run_robot_with_keyboard()` → Manual control using keyboard input.

### 🚀 How to Run
```bash
python robot.py
```

Then choose a mode:
```
1. Run robot with manual control
2. Run robot automatic patrol and harvest
```

### 🎮 Manual Controls
| Key | Action |
|-----|---------|
| **W** | Move Up |
| **A** | Move Left |
| **S** | Move Down |
| **D** | Move Right |
| **F** | Harvest Wheat |
| **Q** | Quit Game |

### 💡 Learning Concepts
- Object-Oriented Programming (Classes and Methods)
- Pathfinding using Manhattan distance
- Loops and state-based logic
- Interactive command-line simulation

### 🧰 Dependencies
```bash
pip install keyboard
```

---

## 👨‍💻 Author
Developed by [BenSurya888](https://github.com/BenSurya888)
