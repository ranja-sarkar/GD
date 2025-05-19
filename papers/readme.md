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

- Scale changes of the variables only affect the ontercepts and not the slopes only if there's no multiplicative term like interaction or polynomial. 





