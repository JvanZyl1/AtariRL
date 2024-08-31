Results from running on collab

Learning rate
DQN_params_Pacman = {
    "learning_rate": XXX,                  # learning rate
    "replay_buffer_size": 20000,            # replay buffer size
    "batch_size": 128,                      # batch size for training
    "gamma": 0.99,                          # discount factor
    "epsilon": 1.0,                         # exploration rate (Load-Run, Start-Run)
    "epsilon_decay": 0.999,                 # exploration rate decay
    "epsilon_min": 0.02,                    # minimum exploration rate
    "update_target_every": 500,             # update target network every 500 steps
    "alpha": 0.6,                           # alpha value for prioritization
    "beta": 0.4,                            # beta value for importance sampling
    "beta_increment_per_sampling": 0.001,   # increment for beta
    "device": device,                       # device to use (CPU or GPU)
    "icm_learning_rate" : 1e-4,
    "icm_update_every": 5,
    "eta" : 0.1
}

Epsilon_decay
DQN_params_Pacman = {
    "learning_rate": 1e-4,                  # learning rate
    "replay_buffer_size": 20000,            # replay buffer size
    "batch_size": 128,                      # batch size for training
    "gamma": 0.99,                          # discount factor
    "epsilon": 1.0,                         # exploration rate (Load-Run, Start-Run)
    "epsilon_decay": XXXXX,                 # exploration rate decay
    "epsilon_min": 0.02,                    # minimum exploration rate
    "update_target_every": 500,             # update target network every 500 steps
    "alpha": 0.6,                           # alpha value for prioritization
    "beta": 0.4,                            # beta value for importance sampling
    "beta_increment_per_sampling": 0.001,   # increment for beta
    "device": device,                       # device to use (CPU or GPU)
    "icm_learning_rate" : 1e-4,
    "icm_update_every": 5,
    "eta" : 0.1
}