import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import csv

# Read data from CSV
frame_numbers = []
object_ids = []
x_positions = []
y_positions = []

with open('player_positions.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        frame_numbers.append(int(row['Frame']))
        object_ids.append(int(row['Object ID']))
        x_positions.append(int(row['X']))
        y_positions.append(int(row['Y']))

# Plot positions
plt.figure(figsize=(10, 6))

for obj_id in set(object_ids):
    xs = [x_positions[i] for i in range(len(object_ids)) if object_ids[i] == obj_id]
    ys = [y_positions[i] for i in range(len(object_ids)) if object_ids[i] == obj_id]
    plt.plot(xs, ys, marker='o', label=f'Object {obj_id}')

plt.title('Player Movements')
plt.xlabel('X Position (pixels)')
plt.ylabel('Y Position (pixels)')
plt.legend()
plt.grid(True)
plt.gca().invert_yaxis()  # Invert Y to match video coordinates
plt.savefig('player_movements.png')
print("Plot saved as player_movements.png")