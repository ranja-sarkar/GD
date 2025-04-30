
# Binary classification by Logistic Regression

There is an outcome y such that y falls into one of two categories (say 0 or 1).
The resulting probability is compared to a threshold to predict a class for y, based on X.

<img width="305" alt="11" src="https://github.com/user-attachments/assets/12aab6df-8e98-43cf-b369-af154af8c350" />

The non-linear transformation might make us think logistic regression is a non-linear model. However, the linearity does not lie in the probability output but in how the model constructs its decision boundary (the log-odds that is). 

<img width="422" alt="lr" src="https://github.com/user-attachments/assets/e63006db-b5e9-4fdb-942e-c8f93f49d503" />

The odds ratio is basically clarifying how likely the numerator is - to happen relative to not happening. 

<img width="388" alt="77" src="https://github.com/user-attachments/assets/769a130f-fa90-498d-864b-c93fec5e3d66" />

The loss function typically to optimize algorithm for given data is log-loss (or cross entropy).

<img width="374" alt="22" src="https://github.com/user-attachments/assets/5973b25f-ce10-4833-9d7c-e764ac9d2e77" />


Examples:


<img width="287" alt="33" src="https://github.com/user-attachments/assets/ac04f47f-531f-4695-b557-247dd544fad7" />
<img width="496" alt="44" src="https://github.com/user-attachments/assets/8e72c2ee-4ed8-4d2e-b1c8-d21951f6a57d" />


<img width="285" alt="55" src="https://github.com/user-attachments/assets/da779a7a-467e-4ebb-8606-3f77cd91d1d4" />
<img width="484" alt="66" src="https://github.com/user-attachments/assets/fff3f372-9c0d-4404-86fb-23cbff17804c" />



-----

There're 2 approaches to finding the coefficients in logistic regression:

i. Gradient Descent

ii. MLE (maximum likelhood estimation)

MLE estimates the most likely distribution given the outcomes. Both MLE and MAP (maximum a posteriori) are methods/tools to find the parameters of a distribution that best fits the information available to us. The prior is the only difference between MLE and MAP. When the prior is uniform (having same probability at all regions), MLE and MAP yield same estimates.

MAP estimates the most probable posterior distribution which includes prior knowledge about the data and personal beliefs about the results. In MAP, the likelihood function gets weighted with some weight coming from the prior distribution. 

[In the Bayesian framework, we start with a belief (prior). We strengthen/weaken the prior with each evidence/datapoint that is, we update the belief to a degree. The updated belief is posterior.]


------

# Comparison to Linear Regression

Decision boundary (linear hyperplane) is defined by: 

<img width="380" alt="lr0" src="https://github.com/user-attachments/assets/dce8c5b0-01dd-4e53-81a9-9d1affc801fc" />

The sigmoid function arises naturally from modeling the log-odds as a linear function. The linearity is in the log-odds, not the probability itself. 

<img width="428" alt="lr1" src="https://github.com/user-attachments/assets/54c6c7bc-91b8-43fc-adb4-4122c1a72a05" />


