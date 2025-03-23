#this is where I will run the functions that display the health bar

import matplotlib.pyplot as plt

def plot_health_bars(user_health, user_max_health):

    plt.clf()
    
    fig, ax = plt.subplots(figsize=(8, 2))

    
    ax.barh(0, user_health, color='green', height=2, label='User')

   
    ax.set_ylim(-1, 1)  

    # Labels and titles
    ax.set_xlim(0, user_max_health)
    ax.set_xlabel('Health')
    ax.set_title('User Health Bar')
    ax.legend()

    plt.tight_layout()
    plt.show()




