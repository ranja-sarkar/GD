
**Gradient descent** means choosing a direction across a landscape and take whichever step gets us downhill, the step-size depending on the slope/gradient of the hill.
As an example, consider a professional journey which usually is gradient **ascent**. You start at a point in a typically rough terrain, your goal is to reach a 'good enough' or optimum point, you achieve it by taking small steps in the direction **upward** of the terrain's slope.


<img width="235" alt="gd" src="https://github.com/user-attachments/assets/efd62049-6bc1-4d67-be80-c62d507441c6" />


[Gradient descent](https://github.com/ranja-sarkar/GD/blob/890a79722dbe8e4d26d57795c88b67f53cb020f6/causal/GD.ipynb) is an iterative optimization algorithm that estimates the set of coefficients/weights in regression equations/models, that is yields the minimum of a convex function. The first derivative is calculated at points on the surface to descend and this derivative gives the steepness of the curve.

**Chapter 4** of my [book](https://www.packtpub.com/en-in/product/a-handbook-of-mathematical-models-with-python-9781804617069) discusses the gradient descent algorithm and its variants - vanilla gradient descent (batch gradient descent), mini-batch gradient descent, and stochastic gradient descent (SGD). SGD is widely used to optimize [neural networks](https://ranja-sarkar.github.io/2026/02/12/neural-network.html). This algorithm has tunable parameters like all algorithms have which are discussed in the chapter.

<img width="830" alt="gd0" src="https://github.com/user-attachments/assets/c3963935-788d-4da3-91f0-6ff087183911" />


# Linear Regression

A linear regression model can be optimized using gradient descent [method](https://github.com/ranja-sarkar/GD/blob/dc7166c754c96bb6d3af625bce60f448c27be5b9/lr_gd.py). The algorithm parameter 'learning rate' controls the incremental steps of optimization. 

<img width="409" alt="222" src="https://github.com/user-attachments/assets/bc15da37-102c-4bd8-abb4-6b74c29aa2d0" />
<img width="137" alt="333" src="https://github.com/user-attachments/assets/5d953809-fd0d-4057-a5ef-b9e10f593ad3" />

With too small a step-size or learning rate, the algorithm may reach the maximum permissible number of iterations before reaching the minimum cost (loss function), whereas it may not converge to the minimum or may diverge completely away from it with a very high learning rate. 

<img width="244" height="196" alt="gd" src="https://github.com/user-attachments/assets/4b54d73f-34a9-4eba-a155-0b3ff6c5d7dd" />


Selecting appropriate learning rate is crucial in achieving an optimally performing model. Learning rate controls the eﬀective capacity of the model in a more complicated way than other hyperparameters of the algorithm. The model capacity is highest when the learning rate is correctly chosen for optimization.

📌 Linear regression is a neural network with [linear activation function](https://ranja-sarkar.github.io/2025/11/28/tests-&-measures.html).


# Logistic Regression

**Logistic regression is a linear model** because it models the log-odds as a linear combination of features. The sigmoid function maps the linear predictor to probabilities without affecting the linearity of the decision boundary. 

<img width="376" height="63" alt="011" src="https://github.com/user-attachments/assets/ac5f2f4f-a7b4-4726-9150-c40648d58435" />


There is an outcome y such that y falls into one of two categories (say 0 or 1) or classes. The resulting probability is compared to a threshold to predict a class for y based on X. The decision boundary (linear hyperplane) is defined by z = 0 in the k-dimensional feature space.

<img width="353" height="51" alt="022" src="https://github.com/user-attachments/assets/ae14f7b9-96bf-411d-b8b6-9138825ca055" />

The linearity does not lie in the probability output but in how the model constructs its decision boundary as a linear function. The linearity is in the log-odds, not the probability itself.

📌 Despite its classification task and non-linear output, logistic regressiion earns its place in the family of generalized linear (regression) models.

**In linear regression, we model the expected value.**

<img width="379" height="36" alt="01" src="https://github.com/user-attachments/assets/bd9b9fa5-ac7b-4a9f-a192-658c8cd14117" />


**In logistic regression, we model the log-odds.** 

<img width="527" height="77" alt="02" src="https://github.com/user-attachments/assets/a82be645-cef4-4aa8-9710-794235f2088a" />

The odds (ratio) clarifies the likeliness of (numerator) happenng relative to (denominator) not happening. Odds are calcuated as p/(1-p) which yields the ratio of the probability of happening to the probability of not happening. For example, if p = 0.5, the odds of happening and not happening are equally likely.

📌 Logistic regression is a neural network with the non-linear activation function, called the sigmoid.

<img width="355" height="143" alt="lr" src="https://github.com/user-attachments/assets/acde2888-f0cc-4c8d-96c2-ac8a8f1a8649" />

Switching from linear regression (continuous outcome y) to logistic regression (categorical outcome y) is basically switching from a linear function to nonlinear sigmoid function for the mathematical operation on the inputs to happen, the model still remaining linear and its output reflecting classification of the dataset.

---

Maximum Likelihood  Estimation (MLE) is another statistical method to find the parameters of such models that best fits the data or information available to us.  
MLE estimates the most likely distribution given the outcomes. Another method MAP (maximum a posteriori) estimates the most probable posterior distribution which includes prior knowledge about the data and personal beliefs about the outcome. In MAP, the likelihood function gets weighted with some weight coming from the prior distribution. 

The prior is the only difference between MLE and MAP. When the prior is uniform (having same probability at all regions), MLE and MAP yield same estimates of model parameters.

---

When fitting a logistic regression model, the goal is to find the parameters that optimize a function that defines how well the model is performing. Put simply, the goal is to make predictions as close to 1 when the outcome is 1 and as close to 0 when the outcome is 0. In machine learning, the function to be optimized is called the loss function or cost function. A suitable loss function in logistic regression is called the Log-Loss, or binary cross-entropy. 

<img width="356" height="46" alt="ll" src="https://github.com/user-attachments/assets/ca705e89-f211-4a12-b2b3-0248ac17e668" />

where n is the number of samples, indexed by i and p is the model prediction for the index i. Minimizing the Log-Loss is equivalent to maximizing the Log-Likelihood, since the Log-Loss is the negative of the Log-Likelihood.

---

The output of a logistic regression model is a probability, which based on a probability threshold is assigned a label for example, 0 or 1 for binary classification. So such models most of the times need to be [calibrated](https://scikit-learn.org/stable/modules/calibration.html) for reliable results. Calibration curves or plots, also referred to as reliability diagrams compare how well the probabilistic predictions of a binary classifier are calibrated.


![cc](https://github.com/user-attachments/assets/38cfca4d-ec62-4256-a951-d3e154c1feb1)


