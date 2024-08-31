# Read text file Pacman_Rewards_lr_1e4.txt

import matplotlib.pyplot as plt

def extract_rewards(file_path):
    file = open(file_path, "r")
    data = file.read()
    lines = data.split('\n')
    rewards = []
    total_episodes = 0
    for line in lines:
        if len(line) > 1:
            rewards.append(float(line))
            total_episodes += 1
    return total_episodes, rewards



total_episodes_1, rewards_1 = extract_rewards("SensitivityAnalysis/LearningRate/Pacman_Rewards_lr_1e4.txt")
total_episodes_2, rewards_2 = extract_rewards("SensitivityAnalysis/LearningRate/Pacman_Rewards_lr_1e5.txt")
total_episodes_3, rewards_3 = extract_rewards("SensitivityAnalysis/LearningRate/Pacman_Rewards_lr_8e5.txt")




plt.figure(figsize=(10, 5))
plt.plot(rewards_1, label="Learning Rate 1e-4")
plt.plot(rewards_2, label="Learning Rate 1e-5")
plt.plot(rewards_3, label="Learning Rate 8e-5")
plt.xlabel("Episodes")
plt.ylabel("Rewards")
plt.title("Pacman Rewards Learning Rate sensitivity analysis")
plt.legend()
plt.show()
            