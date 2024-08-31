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



total_episodes_1, rewards_1 = extract_rewards("SensitivityAnalysis/EpsilonDecay/Pacman_Rewards_epsilondecay_0999.txt")
total_episodes_2, rewards_2 = extract_rewards("SensitivityAnalysis/EpsilonDecay/Pacman_Rewards_epsilondecay_09995.txt")
total_episodes_3, rewards_3 = extract_rewards("SensitivityAnalysis/EpsilonDecay/Pacman_Rewards_epsilondecay_099.txt")




plt.figure(figsize=(10, 5))
plt.plot(rewards_1, label="Epsilon Decay 0.999")
plt.plot(rewards_2, label="Epsilon Decay 0.9995")
plt.plot(rewards_3, label="Epsilon Decay 0.99")
plt.xlabel("Episodes")
plt.ylabel("Rewards")
plt.title("Pacman Rewards Epsilon decay sensitivity analysis")
plt.legend()
plt.show()
            