
A linearity in coefficients of (predictor) variables is the assumption of linear regression. Because it is X that is polynomial (squared or cubed), not the beta coefficient, the regression still qualifies as a linear model. 

A non-linear relationship between the predictor and response or target variable might exist while still preserving the linear model. 

How do you detect the relationship and conclude a linear models isn't the optimal one?

- Doing univariate and bivariate inspections of data before starting regression analyses. A simple scatter plot can reveal a curvilinear relationship.
- Inspection of residuals.  If you fit a linear model to (curved) data, a scatter plot of residuals and the predictor will have patches of positive residuals in the middle, patches of negative residuals at either end (or vice versa).  This is a good sign that a linear model is not appropriate, and a polynomial model may do better.

------


Scale changes of the variables only affect the ontercepts and not the slopes if there's no multiplicative term like interaction or polynomial. 





