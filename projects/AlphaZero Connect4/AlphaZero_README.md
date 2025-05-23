ConnectX AI with Modified AlphaZero Approach

## Overview
This project implements a modified version of the AlphaZero algorithm for the game of ConnectX (Connect Four). The implementation combines Monte Carlo Tree Search (MCTS) with deep neural networks, trained through self-play.

## Installation

### Dependencies
All required packages are listed in `requirements.txt`. Install them using:
```bash
pip install -r requirements.txt
Key Dependencies:

numpy: For numerical computations
torch: For neural network implementation
matplotlib: For visualization of training progress
kaggle-environments: For the ConnectX game environment
joblib: For parallel processing during training

Usage

Clone this repository
Install requirements
Run the Jupyter notebook to train the model
Use the submission generator to create a competition-ready agent

Training Process
The training pipeline includes:

Self-play data generation
Neural network training
Regular evaluation against baseline opponents
Progress visualization

Files

Connect4_AI.ipynb: Main notebook containing implementation and training
requirements.txt: List of required Python packages
submission.py: Generated submission file for competitions

Acknowledgments
Based on implementation by Gyozzza on Kaggle, with modifications and improvements by Group 4.