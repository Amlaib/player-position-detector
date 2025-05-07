import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import seaborn as sns
import csv

# Read data from CSV
x_positions = []
y_positions = []

with open('player_positions.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        x_positions.append(int(row['X']))
        y_positions.append(int(row['Y']))

# Plot heatmap
plt.figure(figsize=(10, 6))
sns.kdeplot(
    x=x_positions,
    y=y_positions,
    cmap="Reds",
    fill=True,
    bw_adjust=0.5
)

plt.title('Player Position Heatmap')
plt.xlabel('X Position (pixels)')
plt.ylabel('Y Position (pixels)')
plt.gca().invert_yaxis()
plt.grid(True)

plt.savefig('player_heatmap.png')
print("Heatmap saved as player_heatmap.png")