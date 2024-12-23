# gradient descent

Gradient descent literally means choosing a direction across a landscape and take whichever step gets us downhill, the step-size depending on the slope (gradient) of the hill.

<img width="170" alt="2" src="https://github.com/user-attachments/assets/8a8928ab-99ad-4237-8b6b-1980905a55ac">


In the context of machine learning, gradient descent is the algorithm for optimization while training a model. Vanilla gradient descent, also called **batch gradient descent** has two variants namely, **mini-batch gradient descent** and **stochastic gradient descent (SGD)**. 

**Chapter 4** of my book discusses the gradient descent algorithm and the variants of it.

<img width="115" alt="0" src="https://github.com/user-attachments/assets/c86f23ab-7707-408b-bfc7-ef5cddabdc58">

Buy at Amazon: https://a.co/d/gw13Tv6


Three linear regression models optimized with the gradient descent method (see the py file in this repo) with different learning rates have been shown in the figures below. 

With too small a learning rate, the algorithm may reach the maximum permissible number of iterations before reaching the minimum cost (function in the y-axis), whereas it may not converge to the min or may diverge completely away from the min with a very high learning rate. 

<img width="195" alt="1" src="https://github.com/user-attachments/assets/55d7aea9-cf83-42df-8aed-0a85506e6f47">


**Selecting the appropriate learning rate is crucial in achieving an optimally performing model.**


<img width="316" alt="1" src="https://github.com/user-attachments/assets/453a37ea-469a-4373-8a79-ad2589a2e957">


<img width="320" alt="2" src="https://github.com/user-attachments/assets/5c2e2d4a-82b1-4fbf-bf7a-fd5cb6d40c1e">


<img width="308" alt="3" src="https://github.com/user-attachments/assets/69659f9d-42f7-47e1-88a7-b818b5ad93c6">


More about **linear regression** model optimized with ordinary least squares (OLS) method: https://ranjas.substack.com/p/linear-regression

Also, refer to my article on model hyperparameters - **learning rate**, **epoch**, and **batch** in the context of optimization of deep neural networks using the gradient descent algorithm:
https://open.substack.com/pub/ranjas/p/hyper-parameters-of-a-neural-network




