
# Logistic Regression

![1](https://github.com/user-attachments/assets/291781c2-ac2c-4f0a-9900-325143938e48)

There is an outcome y such that y falls into one of two categories (say 0 or 1).
The resulting probability is compared to a threshold to predict a class for y, based on X. The decision boundary (linear hyperplane) is defined by z = 0 in the 
k-dimensional feature space.

![2](https://github.com/user-attachments/assets/b4188a72-16c3-4a2e-962e-e4a538b304e0)


The non-linear transformation (sigmoid) might make us think logistic regression is a non-linear model. However, the linearity does not lie in the probability output but in how the model constructs its decision boundary (the log-odds that is) as a linear function.  The linearity is in the log-odds, not the probability itself. 

<img width="422" alt="lr" src="https://github.com/user-attachments/assets/e63006db-b5e9-4fdb-942e-c8f93f49d503" />

---

**Logistic regression is a linear model because it models the log-odds as a linear combination of features. The sigmoid function maps the linear predictor to probabilities without affecting the linearity of the decision boundary. Despite its classification task and non=linear output, loigstic regressiion earns its place in the family of linear regression models.**

---

The odds ratio is basically clarifying how likely the numerator is - to happen relative to not happening. 

<img width="388" alt="77" src="https://github.com/user-attachments/assets/769a130f-fa90-498d-864b-c93fec5e3d66" />

The loss function typically to optimize algorithm for given data is log-loss (or cross entropy).

<img width="374" alt="22" src="https://github.com/user-attachments/assets/5973b25f-ce10-4833-9d7c-e764ac9d2e77" />



-----

There're 2 approaches to finding the coefficients in logistic regression:

i. Gradient Descent

ii. MLE (maximum likelhood estimation)

MLE estimates the most likely distribution given the outcomes. Both MLE and MAP (maximum a posteriori) are methods/tools to find the parameters of a distribution that best fits the information available to us. The prior is the only difference between MLE and MAP. When the prior is uniform (having same probability at all regions), MLE and MAP yield same estimates.

MAP estimates the most probable posterior distribution which includes prior knowledge about the data and personal beliefs about the results. In MAP, the likelihood function gets weighted with some weight coming from the prior distribution. 





<img width="380" alt="lr0" src="https://github.com/user-attachments/assets/dce8c5b0-01dd-4e53-81a9-9d1affc801fc" />



<img width="428" alt="lr1" src="https://github.com/user-attachments/assets/54c6c7bc-91b8-43fc-adb4-4122c1a72a05" />


