
Gradient descent literally means choosing a direction across a landscape and take whichever step gets us downhill, the step-size depending on the slope (gradient) of the hill.

**As an example, consider a professional journey which usually is gradient ascent. You start at a point in a typically rough terrain, your goal is to reach a 'good enough' or optimum point, you achieve it by taking small steps in the direction (upward) of the terrain's slope/gradient.**


<img width="235" alt="gd" src="https://github.com/user-attachments/assets/efd62049-6bc1-4d67-be80-c62d507441c6" />


In the context of machine learning, gradient descent is the algorithm for optimization while training a model. **Chapter 4** of my book discusses the gradient descent algorithm and its variants - vanilla gradient descent, same as **batch gradient descent**, **mini-batch gradient descent**, and **stochastic gradient descent (SGD)**. 

<img width="266" alt="gd" src="https://github.com/user-attachments/assets/90e01b26-0c05-4c8c-90e3-3c11e3ab73e9" />
<img width="830" alt="gd0" src="https://github.com/user-attachments/assets/c3963935-788d-4da3-91f0-6ff087183911" />


Apart from OLS, a linear regression model can be optimized using gradient descent method with a learning rate.  

<img width="409" alt="222" src="https://github.com/user-attachments/assets/bc15da37-102c-4bd8-abb4-6b74c29aa2d0" />
<img width="137" alt="333" src="https://github.com/user-attachments/assets/5d953809-fd0d-4057-a5ef-b9e10f593ad3" />

With too small a learning rate, the algorithm may reach the maximum permissible number of iterations before reaching the minimum cost (function in the y-axis), whereas it may not converge to the min or may diverge completely away from the min with a very high learning rate. 



<img width="442" alt="rs" src="https://github.com/user-attachments/assets/d40b8f98-9fff-473c-929c-d29691249c16" />



**Selecting the appropriate learning rate is crucial in achieving an optimally performing model.** Learning rate controls the **eﬀective capacity of the model** in a more complicated way than other hyperparameters, which is highest when the learning rate is correctly chosen for optimization.


<img width="605" alt="lr" src="https://github.com/user-attachments/assets/382743ba-3286-4f56-89a8-a1db7e38a38f" />

# Logistic Regression

Logistic regression is a linear model because it models the log-odds as a linear combination of features. The sigmoid function maps the linear predictor to probabilities without affecting the linearity of the decision boundary. 

📌 Despite its classification task and non-linear output, logistic regressiion earns its place in the family of generalized linear (regression) models.

In linear regression, we model the expected value.

<img width="379" height="36" alt="01" src="https://github.com/user-attachments/assets/bd9b9fa5-ac7b-4a9f-a192-658c8cd14117" />


In logistic regression, we model the log-odds. The odds (ratio) is basically clarifying the likeliness of (numerator) happenng relative to (denominator) not happening. Odds are calcuated as p/(1-p) which yields the ratio of the probability of happening to the probability of not happening. For example, if p = 0.5, the odds of happening and not happening are equally likely.



<img width="527" height="77" alt="02" src="https://github.com/user-attachments/assets/a82be645-cef4-4aa8-9710-794235f2088a" />

