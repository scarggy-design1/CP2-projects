#this is where I will run the functions that display the health bar

import matplotlib.pyplot as plt

def plot_health_bars(user_health, monster_health, user_max_health, monster_max_health):
    plt.clf()  # Clear the current figure to avoid overlapping plots
    
    # Only use ax (the axes) for the plotting
    ax = plt.subplots(figsize=(8, 2))[1]

    # Plot the health bars
    ax.barh(0, user_health, color='green', height=0.2, label='User')
    ax.barh(0, monster_health, color='red', height=0.2, left=user_max_health, label='Monster')

    # Labels and titles
    ax.set_xlim(0, max(user_max_health, monster_max_health))  # Adjust the axis limits
    ax.set_xlabel('Health')
    ax.set_title('Battle Health Bar')
    ax.legend()

    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)  # Pause to update the plot
    plt.show()