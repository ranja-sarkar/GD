# Linear parameters in regression model

- Intercept (y-intercept)
- Slope (how much y differs on an average for each unit difference in x, there can be multiple x(s) and each one has its own slope)
- Residual variance

A linearity in coefficients of (predictor) variables is the assumption of linear regression. Because it is X that is polynomial (squared or cubed), not the beta coefficient, the regression still qualifies as a linear model. 

A linear model assumes that the effect of each feature/predictor on the dependent variable/target is independent of other predictors in the model. 

<img width="439" alt="ee" src="https://github.com/user-attachments/assets/f6929675-01a4-4649-96a5-dda37ca6b2da" />


A non-linear relationship between the predictor and response/target might exist while still preserving the linear model. 

How do you detect the relationships and conclude a linear models isn't the optimal one for your data?

- Doing univariate and bivariate inspections of data before starting regression analyses. A simple scatter plot can reveal a curvilinear relationship.
- Inspection of residuals.  If you fit a linear model to (curved) data, a scatter plot of residuals and the predictor will have patches of positive residuals in the middle, patches of negative residuals at either end (or vice versa).  This is a good sign that a linear model is not appropriate, and a polynomial model may do better.

<img width="200" alt="cc" src="https://github.com/user-attachments/assets/5ff78351-e466-4763-9a45-9060b20d7a4a" />

  
- By hypothesis that is, include a polynomial term in the equation

# Interactions in regression

- Interaction terms enables examining whether the relationship between the target and an independent variable changes depending on another independent variable.

  <img width="173" alt="cc" src="https://github.com/user-attachments/assets/1cf81cc9-b6b9-407e-a29b-3a360e8516d3" />


- Scale changes of the variables only affect the ontercepts and not the slopes only if there's no multiplicative term like interaction or polynomial.

- An interaction term is effectively a multiplication of two (or more) features that have a joint effect on the target.

  **Example:**

  <img width="155" alt="cc1" src="https://github.com/user-attachments/assets/ae569e5b-8274-48fa-aae8-38652663a226" />

  where, x1 is a continuous feature and x2 is a Boolean (0, 1) flag. Let's investigate the equation individually.

  For x2 = 1, we have

  <img width="83" alt="11" src="https://github.com/user-attachments/assets/87558bfa-ee7e-4889-ab34-ee505dd005d9" />

  For x2 = 0, we have

  
  <img width="79" alt="22" src="https://github.com/user-attachments/assets/20b27523-dbf0-45a7-ac01-5918afc24cd8" />


  We see that without an interaction term beta_1 is the unique effect of x1 on y. And with an interaction term, the effect of x1 is different for different values of x2.

   <img width="298" alt="33" src="https://github.com/user-attachments/assets/5c0799bf-ea4b-49a9-bad1-d73a7a88bba4" />

beta_0 is the intercept irrespective of the flag x2 has, beta_2 is the difference in the intercept between the two flags in x2, and beta_3 is the difference in slopes od x1 with the two values of x2. **The regression lines might or might not intersect.**

Note:

1. Higher-order interactions (like, of three features) are also possible.

2. One can create interaction terms for two numerical features.

    
   
