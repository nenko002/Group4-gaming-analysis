import matplotlib.pyplot as plt

# Redefine values
platforms = ['Steam', 'PlayStation', 'Xbox']
avg_games = [239.85, 233.86, 272.63]
max_games = [32463, 13540, 9018]

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Average Games per Player
axs[0].bar(platforms, avg_games)
axs[0].set_title('Average Games per Player by Platform')
axs[0].set_ylabel('Average Number of Games')

# Max Games Owned by a Single Player
axs[1].bar(platforms, max_games)
axs[1].set_title('Maximum Games Owned by Top Player')
axs[1].set_ylabel('Number of Games')

plt.tight_layout()

# Save each figure separately
fig.savefig('avg_and_max_games.png')

# If you want to split them:
plt.figure(figsize=(7,5))
plt.bar(platforms, avg_games)
plt.title('Average Games per Player')
plt.ylabel('Average Number of Games')
plt.savefig('images/avg_games_per_player.png')  # save to images/

plt.figure(figsize=(7,5))
plt.bar(platforms, max_games)
plt.title('Maximum Games Owned by Top Player')
plt.ylabel('Number of Games')
plt.savefig('images/max_games_per_player.png')  # save to images/

plt.show()
