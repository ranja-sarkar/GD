# Gradient Descent

Gradient descent literally means choosing a direction across a landscape and take whichever step gets us downhill, the step-size depending on the slope (gradient) of the hill.


<img width="235" alt="gd" src="https://github.com/user-attachments/assets/efd62049-6bc1-4d67-be80-c62d507441c6" />


In the context of machine learning, gradient descent is the algorithm for optimization while training a model. Vanilla gradient descent, also called **batch gradient descent** has two variants namely, **mini-batch gradient descent** and **stochastic gradient descent (SGD)**. 

<img width="266" alt="gd" src="https://github.com/user-attachments/assets/90e01b26-0c05-4c8c-90e3-3c11e3ab73e9" />
<img width="830" alt="gd0" src="https://github.com/user-attachments/assets/c3963935-788d-4da3-91f0-6ff087183911" />



**Chapter 4** of my book discusses the gradient descent algorithm and the variants of it.

<img width="115" alt="0" src="https://github.com/user-attachments/assets/c86f23ab-7707-408b-bfc7-ef5cddabdc58">

Buy at Amazon: https://a.co/d/gw13Tv6


Apart from OLS, a linear regression model can be fitted by use of the gradient descent method with a learning rate.  

<img width="409" alt="222" src="https://github.com/user-attachments/assets/bc15da37-102c-4bd8-abb4-6b74c29aa2d0" />
<img width="137" alt="333" src="https://github.com/user-attachments/assets/5d953809-fd0d-4057-a5ef-b9e10f593ad3" />

With too small a learning rate, the algorithm may reach the maximum permissible number of iterations before reaching the minimum cost (function in the y-axis), whereas it may not converge to the min or may diverge completely away from the min with a very high learning rate. 



<img width="442" alt="rs" src="https://github.com/user-attachments/assets/d40b8f98-9fff-473c-929c-d29691249c16" />



**Selecting the appropriate learning rate is crucial in achieving an optimally performing model.** Learning rate controls the eﬀective capacity of the model in a more complicated way than other hyperparameters—the eﬀective capacity of the model is highest when the learning rate is correct for the optimization problem.


<img width="605" alt="lr" src="https://github.com/user-attachments/assets/382743ba-3286-4f56-89a8-a1db7e38a38f" />




Refer to my article on model hyperparameters - **learning rate**, **epoch**, and **batch** in the context of optimization of deep neural networks using the gradient descent algorithm:
https://open.substack.com/pub/ranjas/p/hyper-parameters-of-a-neural-network




