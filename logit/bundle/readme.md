
# Logistic Regression (LR)

![1](https://github.com/user-attachments/assets/291781c2-ac2c-4f0a-9900-325143938e48)

There is an outcome y such that y falls into one of two categories (say 0 or 1) or classes.
The resulting probability is compared to a threshold to predict a class for y based on X. The decision boundary (linear hyperplane) is defined by z = 0 in the 
k-dimensional feature space.

![2](https://github.com/user-attachments/assets/b4188a72-16c3-4a2e-962e-e4a538b304e0)


The non-linear transformation (sigmoid) might make us think logistic regression is a non-linear model. However, the linearity does not lie in the probability output but in how the model constructs its decision boundary (the log-odds that is) as a linear function.  The linearity is in the log-odds, not the probability itself. 

---

# Approaches to find the parameters or coefficients/weights in LR

1. MLE (maximum likelhood estimation)

MLE estimates the most likely distribution given the outcomes that is, data. 

MAP (maximum a posteriori) estimates the most probable posterior distribution which includes prior knowledge about the data and personal beliefs about the results. 

Both MLE and MAP are methods/tools to find the parameters of the model that best fits the information available to us.  

In MAP, the likelihood function gets weighted with some weight coming from the prior distribution. The prior is the only difference between MLE and MAP. When the prior is uniform (having same probability at all regions), MLE and MAP yield same estimates of parameters. 

2. Gradient Descent
   
----

**Logistic regression is a linear model because it models the log-odds as a linear combination of features. The sigmoid function maps the linear predictor to probabilities without affecting the linearity of the decision boundary. Despite its classification task and non-linear output, logistic regressiion earns its place in the family of generalized linear (regression) models.**

---
In linear regression, we model the expected value of a continuous outcome.

![1](https://github.com/user-attachments/assets/b6a727a5-0301-4e5c-9372-de3f3203368d)

In logistic regression, we model the log-odds.

![2](https://github.com/user-attachments/assets/a27bf2d8-7d07-4920-a70d-99d90412b82a)

---

The odds (ratio) is basically clarifying how likely the numerator is to happen relative to (denominator) not happening. Odds are calcuated as p/(1-p) which yields the ratio of the probability of happening to the probability of not happening.

If p = 0.75, it means the odds of happening are (0.75/0.25) that is 3 to 1. 

If p = 0.5, the odds of happening and not happening are equally likely. 

---

The loss function to optimize the algorithm is log-loss (or binary cross entropy).

![3](https://github.com/user-attachments/assets/2158ac9d-ac9c-43ad-946d-39e7db67ed4c)


-----


Using scikit-learn to develop a binary classifier (logistic regression) model and calibrating it:

1. https://scikit-learn.org/stable/modules/calibration.html
   
2. https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html

   



