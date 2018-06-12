# Multi-armed bandit Problem

## Description

This folder contains three basic algorithms to solve the multi-armed bandit Problem:

* Random selection
* Upper Confidence Bound (UCB)
* Thompson Sampling

## Understanding the multi-armed bandit problem
Don't you love problems with such cool names in machine learning ? The multi-armed bandit problem is one problem that can be solved with reinforcement learning. First of all, what is a bandit ?

<p align="center">
  <img src="./images/one-armed-bandit.png">
</p>

As shown in the figure, a bandit is a slot machine. It is called specifically one-armed bandit because of the handle on the right that moves. In some places like casinos, you can still find these machines where you have to pull the handle. Nowadays, this process is likely electronic where you just press a button to initiate the game. Why it is called bandit ? Well, it is one of the quickest way on earth to loose your money in a casino. Some people even believe that companies that buil these machines put a bug into them to make people loose faster than what a simple probability computation reveals.

The multi-armed bandit problem is the challenge to *play with multiple one-armed bandit simultaneously*:

<p align="center">
  <img src="./images/multi-armed-bandit.png">
</p>

Interestingly, many real problems can be reduced to the multi-armed bandit problem. In fact, any problem in which a fixed limited set of resources must be allocated between competing (alternative) choices in a way that maximizes their expected gain boils down to the multi-armed bandit problem. In order to convince you why this is true, let's take a real problem of the ad selection on a web page.

### Case study: the ad selection on a web page

Image that we have N ads that we display to users each time they connect to a web page. We can only display one ad each time the user ask for the web page. We would like to maximize the probability that user click on the ad so that we can earn a fixed amount of dollars per click. as you can guess, the key question to answer is: which ad among the N ads we have should we display to maximize our profit ?

Where is the analogy with the multi-armed bandit problem ? Well, Let's consider:
* each ad as a bandit.
* displaying an ad is equivalent to play with one-armed bandit.
* the fact of earning a fixed amount of dollars if the user click on the ad equivalent to earn a fixed amount of dollars if we win a one-armed bandit game.

Then, solving the ad selection strategy on a web page is exactly equivalent to solving the multi-armed bandit game.

### The mathematical model of the multi-armed bandit problem

## How to solve this problem

### Random selection
<p align="center">
  <img src="./images/random_selection.png">
</p>

### Upper Confidence Bound

<p align="center">
  <img src="./images/UCB.png">
</p>

### Thompson Sampling

<p align="center">
  <img src="./images/Thompson_Sampling.png">
</p>

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




