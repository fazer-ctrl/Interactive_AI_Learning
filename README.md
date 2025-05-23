# Interactive AI Learning

Interactive learning environment based on Artificial Intelligence: A Modern Approach (AIMA) textbook by Russell and Norvig.

## About

This repository contains implementations of AI algorithms from the AIMA textbook with interactive visualizations and hands-on learning components. The focus is on practical implementation and experimentation rather than just theoretical understanding.

## Projects

### Q-Learning
Complete reinforcement learning implementation with visualization of learning progress and policy evolution.

### Alpha Zero
Game-playing AI using Monte Carlo Tree Search and neural networks for self-play training.

### EDA
Exploratory Data Analysis tools with automated statistical analysis and visualization capabilities.

### Search Algorithms
Implementation of A*, Dijkstra, and other pathfinding algorithms with step-by-step visualization.

### Game AI
Minimax algorithm with alpha-beta pruning for game-playing agents.

### Neural Networks
From-scratch neural network implementations with training visualization and decision boundary plotting.

## Installation

```bash
git clone https://github.com/fazer-ctrl/Interactive_AI_Learning.git
cd Interactive_AI_Learning
pip install -r requirements.txt
```

## Usage

### Run individual projects:

```bash
cd projects/q_learning
python demo.py
```

```bash
cd projects/alpha_zero
python play_game.py
```

### Run Jupyter notebooks:

```bash
jupyter lab notebooks/
```

## Structure

```
projects/
├── q_learning/
├── alpha_zero/
├── eda/
├── search/
├── game_ai/
└── neural_nets/
notebooks/
utils/
tests/
docs/
```

## Requirements

- Python 3.8+
- Dependencies listed in requirements.txt

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit pull request

Focus on educational value and code clarity.

## License

MIT License

## References

- Russell, S. & Norvig, P. Artificial Intelligence: A Modern Approach
- Original AIMA Python repository: aimacode/aima-python
