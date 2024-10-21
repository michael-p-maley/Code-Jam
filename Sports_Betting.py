## Sports Betting Code Jam

import matplotlib.pyplot as plt
from scipy.stats import norm

# Function to calculate projected passing yards
def projected_player_yards(player_avg_yards, defense_allowed_yards):
    return (player_avg_yards + defense_allowed_yards) / 2

# Function to calculate the probability of hitting the line
def calculate_probability(projected_yards, line, std_dev=25):
    probability_over = 1 - norm.cdf(line, projected_yards, std_dev)
    return probability_over

# Get input from the user
player_avg_yards = float(input("Enter the player's average yards per game: "))
defense_allowed_yards = float(input("Enter the defense's average allowed yards per game: "))
line = float(input("Enter the player's yardage line: "))

# Calculate projected yards
projected_yards = projected_player_yards(player_avg_yards, defense_allowed_yards)

# Calculate probability of hitting the over on the line
std_dev = 25 
probability_over = calculate_probability(projected_yards, line, std_dev)

# Print the projected yards and probability
print(f"The projected yards for the player in this game is: {projected_yards}")
print(f"The probability of the player going over {line} yards is: {probability_over * 100:.2f}%")

# Data for the line graph
categories = ['Player Avg Yards', 'Defense Allowed Yards', 'Projected Yards', f'Line ({line} yards)']
values = [player_avg_yards, defense_allowed_yards, projected_yards, line]

# Plot the line graph
plt.figure(figsize=(8, 6))
plt.plot(categories, values, marker='o', linestyle='-', color='blue', linewidth=2, markersize=10)

# Add labels and title
plt.ylabel('Yards')
plt.title('Comparison of Player Avg, Defense Allowed, Projected Yards, and Line')

# Show the graph
plt.grid(True)
plt.show()
