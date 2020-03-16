# RL intro
* `Learn` to make a `good` `seqences of decisions`
  * not just one decision
  * it is hard to define goodness in some scenario (deplayed consequence)
  * How to learn
* 99% of the applications are still supervised learning
  * RL is in `Robotics`, `Game (trading)`, `Self-driving` and `Chatbot`
* Sometimes we dont get all states (e.g., trading, poker game, ...)
* Need to get reward in the end of day, Not easy to tell which step is good

# Architecture
![rl_arch](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Reinforcement_learning_diagram.svg/800px-Reinforcement_learning_diagram.svg.png)

# Model
A model has a very specific meaning: it refers to the different dynamic states of an environment and how these states lead to a reward.
* `Model-based RL` entails constructing such a model.
* `Model-free RL`, conversely, forgoes this environmental information and only concerns itself with determining what action to take given a specific state. 

# Policy based
* `Policy` is a mapping from past experience (perceived states of the environment) to action (to be taken when in those states)
* It is can be represented as a table

# Value based
* No policy (e.g., `Q-learning`)

## Value function
* It is future rewards from being in a state and/or action when following a particular policy
![value_fun](https://user-images.githubusercontent.com/8428372/74616561-e4312d00-516b-11ea-9809-a543a4ba78ce.png)

# Markov Decision Process (MDP)


## Markov chains
* It has probabilities of the next states, no reward, no action

![Markov1](https://user-images.githubusercontent.com/8428372/74341692-78596800-4deb-11ea-8e4c-f9e47f01f8e9.png)

* It can be represented by finite state machines, or a table format

![Markov2](https://user-images.githubusercontent.com/8428372/74341678-7394b400-4deb-11ea-8be5-a3662b5f37f5.png)

## Markov reward process
* Markov reward process = Markov chains + reward
* No action

### `Horizon`
* Number of time steps in each episode
* Can be infinite, Otherwise called finite Markov reward process

### `Return`
* Discounted sum of rewards (`γ` is discount factor) from time step t to horizon

![return](https://user-images.githubusercontent.com/8428372/74606766-6b53b600-5116-11ea-831f-eabd51156a88.png)

### value function of Markov reward process
![MRP_value_func](https://user-images.githubusercontent.com/8428372/74616663-923cd700-516c-11ea-89de-27357ebe7af2.png)

## Markov Decision Process (MDP)
* Markov Decision Process = Markov reward process + action

![MDP](https://user-images.githubusercontent.com/8428372/74616811-50606080-516d-11ea-8441-c1643fbbbf8e.png)

* P (dynamics/transitions) with 2 actions (left and right)
![p_in_mdp_with_2_a](https://user-images.githubusercontent.com/8428372/74616895-be0c8c80-516d-11ea-8087-1f9280894aae.png)

### Policy in MDP
* Policy (`π(a|s)`) specifies what action to take in each state

# Model free policy evalution
* Sometimes we don't have `P` (dynamics/transitions) and `Reward` (e.g., playing Go)
* Algorithms:
  * Dynamic programming: when we know how the world works
  * Monte Carlo policy evaluation
  * Temporal Difference (TD)
  
# How to evalute policy?

# MDP vs Q-learning
* Markov Decision Process(MDP) is a model for Q-learning to be applied to
* The goal of Q-learning is to learn a `policy`, which tells an agent what action to take under what circumstances
  * For any finite Markov decision process (FMDP), Q-learning finds a policy that is optimal in the sense that it maximizes the expected value of the total reward over any and all successive steps, starting from the current state.

# Q-learning
* The goal of Q-learning
![qlearning_table](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Q-Learning_Matrix_Initialized_and_After_Training.png/800px-Q-Learning_Matrix_Initialized_and_After_Training.png)

* The process of the algorithm
![qlearning_process](https://user-images.githubusercontent.com/8428372/76696665-3022b380-66d1-11ea-8bf1-a8c92c761e0f.png)

* The equation of Q-learning updating
![update_qvalue](https://user-images.githubusercontent.com/8428372/76696667-31ec7700-66d1-11ea-8d2a-6ec1cea8a8d7.png)

## exploration
* exploration and exploitation trade-off 
* epsilon greedy strategy: 
  * In the beginning, the epsilon rates will be higher. The robot will explore the environment and randomly choose actions. 
  * As the robot explores the environment, the epsilon rate decreases and the robot starts to exploit the environment.

## Approximations
* Use NN to predict the Q value

# RL vs Deep RL
## Q-learning vs Deep Q-learning
In reinforcement learning, an agent tries to come up with the best action given a state.  

Through reinforcement learning's trial and error, it accumulates knowledge through these `(state, action)` pairs, as in, it can tell if there would be positive or negative reward given a `(state, action)` pair.

Like this:  
```
state | action | reward Q(state, action)   
----------------------------------------  
  ... |   ...  |   ...  
```

The problem is the (state, action) space can be very big, even a slightly different state is still a distinct state (e.g., Atari Games)

## Approximating the Q value with a Neural Network
* Use NN to predict the Q value, based on the input (state, action).
  * `Q` names the function that returns the reward and can stand for the "quality" of an action taken in a given state

## Summary 
Deep RL uses a Deep Neural Network to approximate Q(state, action). 
Non-Deep RL defines Q(state, action) using a tabular function.

## Ref
https://stackoverflow.com/questions/46260775/what-is-a-policy-in-reinforcement-learning  





# Today  
https://jlptstudy.net/N5/
