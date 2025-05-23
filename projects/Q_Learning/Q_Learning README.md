# Deep Q-Learning for ConnectX Game

This project implements a Deep Q-Learning algorithm to play the ConnectX game, a variant of Connect Four, using reinforcement learning techniques. The code adapts insights from other deep reinforcement learning implementations, tailored specifically for ConnectX on the Kaggle platform.

## Citation
This README was written with assistance from OpenAI's ChatGPT, based on user instructions and information provided by:

1. Phung Hieu's Kaggle Notebook "ConnectX with Deep Q-Learning":
   [Kaggle Link](https://www.kaggle.com/code/phunghieu/connectx-with-deep-q-learning)
2. Benedikt's article "Deep Reinforcement Learning: Build a Deep Q-Network (DQN) to play CartPole with TensorFlow 2 and Gym":
   [Towards Data Science Link](https://towardsdatascience.com/deep-reinforcement-learning-build-a-deep-q-network-dqn-to-play-cartpole-with-tensorflow-2-and-gym-8e105744b998)

---

## Overview

This code uses a Deep Q-Network (DQN) approach, a reinforcement learning algorithm that combines Q-Learning with deep neural networks to approximate Q-values for action-state pairs. The algorithm enables the agent to learn optimal moves in the ConnectX game environment, which involves dropping tokens into a grid to create a line of four while preventing the opponent from doing the same.

### Key Components

1. **Environment Setup**:
   - The ConnectX environment is set up using the Kaggle API, where the agent interacts with the game grid and receives feedback in the form of rewards.

2. **Deep Q-Network**:
   - A neural network model approximates Q-values, trained with experience replay to enhance stability.
   - Actions are chosen based on an epsilon-greedy policy, where the agent occasionally explores random moves for a broader understanding of the game.

3. **Training Loop**:
   - The agent interacts with the environment, collecting experiences (state-action-reward-next state) stored in replay memory.
   - The DQN model is updated by sampling batches from this memory, allowing the agent to generalize from past experiences.

4. **Evaluation**:
   - After training, the agent is evaluated by playing multiple games in the ConnectX environment to measure its performance.

### Setup and Installation

1. **Install Dependencies**:
   - Use the `requirements.txt` file to install the necessary dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Execute the Notebook**:
   - Run the notebook step-by-step to set up the environment, initialize the model, and start training the agent.
   
3. **Tuning Parameters**:
   - Adjust hyperparameters such as learning rate, batch size, and epsilon decay in the code to optimize performance.

4. **Evaluate Performance**:
   - Use the evaluation section to test the trained agent's gameplay and analyze its strategies.

## Files

- `Q-ReinforcementLearningConnect4.ipynb`: The main notebook file containing all code for setting up, training, and evaluating the DQN agent.
- `requirements.txt`: Lists the dependencies needed to run the project.

## References

1. [Kaggle ConnectX Notebook by Phung Hieu](https://www.kaggle.com/code/phunghieu/connectx-with-deep-q-learning)
2. [Towards Data Science CartPole DQN Article](https://towardsdatascience.com/deep-reinforcement-learning-build-a-deep-q-network-dqn-to-play-cartpole-with-tensorflow-2-and-gym-8e105744b998)

---