


# Exploring interactions in a regression model

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





   

   
   
   
   
