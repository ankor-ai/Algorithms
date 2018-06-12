# Multi-armed bandit Problem

## Description

This folder contains three basic algorithms to solve the multi-armed bandit Problem:

* Random selection
* Upper Confidence Bound (UCB)
* Thompson Sampling

## Understanding the multi-armed bandit problem
Don't you love problems with such cool names in machine learning ? The multi-armed bandit problem is one problem that can be solved with reinforcement learning. First of all, what is a bandit ?

![alt text](./images/one-armed-bandit.png?style=centerme)

As shown in the figure, a bandit is a slot machine. It is called specifically one-armed bandit because of the handle on the right that moves. In some places like casinos, you can still find these machines where you have to pull the handle. Nowadays, this process is likely electronic where you just press a button to initiate the game. Why it is called bandit ? Well, it is one of the quickest way on earth to loose your money in a casino. Some people even believe that companies that buil these machines put a bug into them to make people loose faster than what a simple probability computation reveals.

## How to solve this problem

### Random selection
![alt text](./images/random_selection.png)

### Upper Confidence Bound
![alt text](./images/UCB.png)
### Thompson Sampling

![alt text](./images/Thompson_Sampling.png)

## Running
The results can reproduced by running each script with Python 3:
* Random selection
``` shell
python3 Random_Selection.py
```

* Upper Confidence Bound (UCB)
``` shell
python3 UCB.py
```

* Thompson_Sampling.py
``` shell
python3 Thompson_Sampling.py
```




