# General Notes on ML

* following edx course
* might be useful for interviews

- train dataset: ilustration data of the task in hand.
- test dataset: 
- 

## Global scope on how to tackle a ML problem

- Explore the dataset to understand *how* the problem relates to this dataset.
    Ask and answer this questions:
    - What are the relevant variables/aspects of my problem?
    - How do these variables relate to my dataset? are they present? are they directly connected? are they correlated?
    - What is the jerarchy of these variables? which ones are more important/relevant.
- Map or mask your variables to the real numbers to get a *features vector*
- Set a baseline
- Compute the baseline


## Common types of ML
- Supervised learning: prediction based on examples of correct behavior
- Unsupervised learning: no explicit target, only data, goal to "model/discover"
- Semi-supervised learning: supplement limited annotations w/ unsupervised learning.
- Active learning: learn to query the examples actually needed for learning.
- Transfer learing: apply what you have learnt from A to B.
- Reinforcement learning: "learning to act, not just predict; goal to optimize the consequences of actions"

## Supervised learning

This paradigm of training consist on using "labeled data" to train a model.
The general procedure

Always mapping a **features vector** to label domain,
if this domain is made of categories,
then we refer to a Classification problem.
If the domain is made of real numbers,
then we talk about a Regression.


## Optimization

- loss function
- objective function: define as the *loss function* plus a *regularization* term
- margin boundaries: parallel boundaries to the decision boundary,
    controlled by an extra parameter that takes into account the distance btw the two boundaries.
    Now, if the decision bondary is the one that for a classifier $h(x)$ satisfies that $h(x)=0$ for every class, then the margin boundaries are define for each class $c_i$ like:
    $h(x)=c_i$, where $c_i$ is the mapping of the ith class.

## Regularization

