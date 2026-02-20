
Gradient descent literally means choosing a direction across a landscape and take whichever step gets us downhill, the step-size depending on the slope/gradient of the hill.
As an example, consider a professional journey which usually is gradient **ascent**. You start at a point in a typically rough terrain, your goal is to reach a 'good enough' or optimum point, you achieve it by taking small steps in the direction **upward** of the terrain's slope.


<img width="235" alt="gd" src="https://github.com/user-attachments/assets/efd62049-6bc1-4d67-be80-c62d507441c6" />


[Gradient descent](https://github.com/ranja-sarkar/GD/blob/890a79722dbe8e4d26d57795c88b67f53cb020f6/causal/GD.ipynb) is an iterative optimization algorithm that estimates the set of coefficients/weights in regression equations/models, that is yields the minimum of a convex function.

**Chapter 4** of my [book](https://www.packtpub.com/en-in/product/a-handbook-of-mathematical-models-with-python-9781804617069) discusses the gradient descent algorithm and its variants - vanilla gradient descent (batch gradient descent), mini-batch gradient descent, and stochastic gradient descent (SGD). SGD is widely used tooptimize neural networks. 

<img width="830" alt="gd0" src="https://github.com/user-attachments/assets/c3963935-788d-4da3-91f0-6ff087183911" />


# Linear Regression

A linear regression model can be optimized using gradient descent [method](https://github.com/ranja-sarkar/GD/blob/dc7166c754c96bb6d3af625bce60f448c27be5b9/lr_gd.py). The algorithm parameter 'learning rate' controls the incremental steps of optimization. 

<img width="409" alt="222" src="https://github.com/user-attachments/assets/bc15da37-102c-4bd8-abb4-6b74c29aa2d0" />
<img width="137" alt="333" src="https://github.com/user-attachments/assets/5d953809-fd0d-4057-a5ef-b9e10f593ad3" />

With too small a step-size or learning rate, the algorithm may reach the maximum permissible number of iterations before reaching the minimum cost (loss function), whereas it may not converge to the minimum or may diverge completely away from it with a very high learning rate. 

<img width="244" height="196" alt="gd" src="https://github.com/user-attachments/assets/4b54d73f-34a9-4eba-a155-0b3ff6c5d7dd" />


Selecting appropriate learning rate is crucial in achieving an optimally performing model. Learning rate controls the eﬀective capacity of the model in a more complicated way than other hyperparameters of the algorithm. The model capacity is highest when the learning rate is correctly chosen for optimization.



# Logistic Regression

Logistic regression is a linear model because it models the log-odds as a linear combination of features. The sigmoid function maps the linear predictor to probabilities without affecting the linearity of the decision boundary. 

<img width="376" height="63" alt="011" src="https://github.com/user-attachments/assets/ac5f2f4f-a7b4-4726-9150-c40648d58435" />


There is an outcome y such that y falls into one of two categories (say 0 or 1) or classes. The resulting probability is compared to a threshold to predict a class for y based on X. The decision boundary (linear hyperplane) is defined by z = 0 in the k-dimensional feature space.

<img width="353" height="51" alt="022" src="https://github.com/user-attachments/assets/ae14f7b9-96bf-411d-b8b6-9138825ca055" />

The linearity does not lie in the probability output but in how the model constructs its decision boundary as a linear function. The linearity is in the log-odds, not the probability itself.

📌 Despite its classification task and non-linear output, logistic regressiion earns its place in the family of generalized linear (regression) models.

In linear regression, we model the expected value.

<img width="379" height="36" alt="01" src="https://github.com/user-attachments/assets/bd9b9fa5-ac7b-4a9f-a192-658c8cd14117" />


In logistic regression, we model the log-odds. The odds (ratio) is basically clarifying the likeliness of (numerator) happenng relative to (denominator) not happening. Odds are calcuated as p/(1-p) which yields the ratio of the probability of happening to the probability of not happening. For example, if p = 0.5, the odds of happening and not happening are equally likely.



<img width="527" height="77" alt="02" src="https://github.com/user-attachments/assets/a82be645-cef4-4aa8-9710-794235f2088a" />

