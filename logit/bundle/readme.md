

**1. MLE (maximum likelhood estimation)**

MLE estimates the most likely distribution given the outcomes that is, data. 

MAP (maximum a posteriori) estimates the most probable posterior distribution which includes prior knowledge about the data and personal beliefs about the results. 

Both MLE and MAP are statistical methods to find the parameters of the model that best fits the information available to us.  

In MAP, the likelihood function gets weighted with some weight coming from the prior distribution. The prior is the only difference between MLE and MAP. When the prior is uniform (having same probability at all regions), MLE and MAP yield same estimates of parameters. 

----


The loss function to optimize the algorithm is log-loss (or binary cross entropy).

![3](https://github.com/user-attachments/assets/2158ac9d-ac9c-43ad-946d-39e7db67ed4c)


-----


Using scikit-learn to develop a binary classifier (logistic regression) model and calibrating it:

1. https://scikit-learn.org/stable/modules/calibration.html
   
2. https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html

   



