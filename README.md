# AI Projects & Algorithms:

## Degrees
Find the shortest path and the "degree of seperations" between two actors using BFS and DFS

### Key Ideas:
- BFS: FIFO or queue frontier
- DFS: LIFO or stack frontier

## Tic-Tac-Toe
Use Minimax to make AI play the game optimally

### Key Ideas:
- Adveserial search: algorithm where the opponent has an opposing goal
- State: a configuration of an agent in its environment
- Actions: choices that can be made in a state
- Transition Model: state results based on a particular action
- State Space: set of all states possible from the initial state following a sequence of actions
- Goal Test: condition that determines whether a goal is reached
- Path Cost: a numerical cost associated with a given path

## Knights
Use model checking algorithm to solve the classic puzzle game: knights and knaves

### Key Ideas:
- Prepositional logic: knowledge base, entailment
- Inference rules: Modus Ponens, double negation elimination, implication elimination, biconditional elimination,
distributive property
- Resolution: conjunctive normal form (CNF)
- First order logic

## PageRank:
Use Markov Chain and iterative algorithms to calculate page ranks - the importance of pages when searching

### Key Ideas:
- Markov Chain: a sequence of random variables where the distribution of each variable follows the Markov assumption
- Markov assumption: a current state depends on only a finite number of previous states
- Transition model: specify the probability distributions of the next event based on the values of the current event

## Heredity:
Use Bayesian network and inference by enumeration to find the heredity of impairment genes

### Key Ideas:
- Bayesian network: a directed graph data structure that represents the dependencies of random variables where an
arrow from one variable (X) to another variable (Y) is the conditional probability of Y based on X. Y is the parent of X.
- Inference by enumeration: a process of finding the probability distribution of variable X given some observed evidence
e and some hiddren variables Y.
- Joint probability: the liklihood of multiple events all occuring

## Crossword
CSP using backtracking searching and heuristcs

### Optimization Concepts:
- Constraint Satisfaction Problem
- Backtracking Search
- Linear & nonlinear programming
- Hill climbing & simulated annealing

### Key Ideas:
- Arc consistency: when all the values in the variable's domain satisfy binary constraints
- Node consistency: when all the values in the variable's domain satisfy unary constraints

## Shopping
Use machine learning and kNN to predict whether online shopping customers will complete a purchase

## Nim
Use reinforcement learning (Q-learning) for AI to train itself in the game of nim

## Traffic: image classification
This is the project where I got to build a CNN for predicting German traffic signs and experiment with TensorFlow and OpenCV.

### Key Ideas: 
- multilayer neural network: artificial neural network with an input layer,
an output layer, and at least one hidden layer
- image convolution: applying a filter that adds each pixel value of an image
to its neighbours, weighted according to a kernel matrix
- pooling: reducing the size of an input by sampling from regions in the input
- max pooling: pooling by choosing the max value in each region
- dropout: temporaily removing units - selected at random - from a neural network
to prevent over-reliance on certain units

### Key Observations:
One of the key objectives of this project is tuning the hyperparameters of a convolutional neural network (CNN).

In general, it can be observed that increasing the number of convolutional and pooling 
layers also increases the accuracy of the model. This is achieved by applying the 
convolutional and pooling twice. The second time allows higher-level and more complex features to be extracted. 

Increasing the number of filters in the convolutional layer does not affect 
the overall accuracy of the model for a number of 10 epochs, even though the initial accuracies are low. Increasing the filter number or sizes increase the abstractions of the model. It can be reasoned that as the number of layers increases and as more higher-level features need to be extracted, increasing the filter number and sizes can increase the representational power of the layers. 

It can also be observed that increasing the number and sizes of hidden layers neither improve
nor worsen the accuracy of the model and the neural network. For other models however, this may affect the 
accuracy. On the other hand, while increasing the size of max pooling reduces the size of input, it comes at a significant drop of accuracy.

## Weather: random forest tutorial
Going to back environmental data, this time I'm learning to create an emsemble random forest classifier! Disclaimer: this code is based on the tutorial from medium: https://towardsdatascience.com/random-forest-in-python-24d0893d51c0. 
