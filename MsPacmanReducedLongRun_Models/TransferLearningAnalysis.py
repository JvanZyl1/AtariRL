# Read text file Pacman_Rewards_lr_1e4.txt

import matplotlib.pyplot as plt

def extract_rewards(file_path):
    # Open the file in read mode
    file = open(file_path, "r")

    # Read the file
    data = file.read()

    # Split the data into lines
    lines = data.split('\n')

    # Initialize lists to store the rewards and episodes
    rewards = []

    # Iterate through the lines
    total_episodes = 0
    for line in lines:
        if len(line) > 1:
            # Only reward
            rewards.append(float(line))
            total_episodes += 1

    return total_episodes, rewards



total_episodes_1, rewards_1 = extract_rewards("MsPacmanReducedLongRun_Models/MsPacmanNotTransferLearning/Episode_440_Rewards.txt")
total_episodes_2, rewards_2 = extract_rewards("MsPacmanReducedLongRun_Models/MsPacmanTransferLearning/Episode_400_Rewards.txt")

# Collab crashed
total_episodes_2 = 370
rewards_2 = rewards_2[:total_episodes_2]

rewards_1 = rewards_1[:total_episodes_2]

# Apply moving average
window_size = 10
rewards_1_moving_av = [sum(rewards_1[i:i+window_size])/window_size for i in range(len(rewards_1) - window_size)]
rewards_2_moving_av = [sum(rewards_2[i:i+window_size])/window_size for i in range(len(rewards_2) - window_size)]

plt.figure(figsize=(10, 5))
plt.title("Ms Pacman reduced action space results.")
#plt.subplot(2, 1, 1)
#plt.plot(rewards_1,  linewidth =2,label="Not Transfer Learning")
#plt.plot(rewards_2, linewidth =2,label="Transfer Learning")
#plt.ylabel("Rewards")
#plt.subplot(2, 1, 2)
plt.plot(rewards_1_moving_av, linewidth =2, label="Not Transfer Learning")
plt.plot(rewards_2_moving_av,linewidth =2,label="Transfer Learning")
plt.xlabel("Episodes")
plt.ylabel("Rewards")
plt.legend()
plt.show()
            