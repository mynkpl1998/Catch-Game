# Catch-Game
This repository contains the implementation of Deep Q and Learning and Dual Network Deep Q Learning on a came of catch.
The agent wins each game in every episode (Accuracy : 100 %)

<img src="https://raw.githubusercontent.com/mynkpl1998/Catch-Game/master/Images/out-1.gif" alt="Smiley face" height="300" width="300">
<img src="https://raw.githubusercontent.com/mynkpl1998/Catch-Game/master/Images/out.gif" alt="Smiley face" height="400" width="600">

# Overview
Repository contains two folders
1. [Implementation of Deep Q Learning with Experience Replay](https://github.com/mynkpl1998/Catch-Game/tree/master/Deep%20Q%20Learning)
2. [Implementation of Dual Network Q learning](https://github.com/mynkpl1998/Catch-Game/tree/master/Dual%20Network%20Q%20Learning)

# Theory 
Deep Q learning is very good general reinforcement learning which can be applied multiple environment but the problem with Deep Q Learning is that it takes too long to converge if the environment is too complex. There exists many ways by which one can speed up the convergence of algorithm. **Experience Replay** is one of them which i have implemented, another way is to use a **Dual Network** instead of one in Q-learning algorithm. The logic behind the use of dual network is that it stablizes the learning process and speeds up in reaching the convergence.  

# To-Do
Due to lack of good gpu i didn't able to train the agent for Dual Network Learning.

# How to Train ?
```
cd Folder
python AI.py
```

# How to Play using saved model ?
```
cd Folder
python play_ai.py
```

# Graphs

<img src="https://raw.githubusercontent.com/mynkpl1998/Catch-Game/master/Deep%20Q%20Learning/data/combine_images.jpg" alt="Smiley face" height="600" width="800">
