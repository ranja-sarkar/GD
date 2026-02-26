

The measurement of the impact a marketing effort or strategy generates on the business in the long-term when compared to no effort taken becomes complex 
since the effect might get diluted over time. Drawing causal inference is thus hard in the long-term. Allocating advertising budget and estimating its impact on business in the long-term needs modeling and optimization. 

# Measuring causal effect

The measurement is done with the difference between the effect generated in the consumers stimulated with marketing gimmick (test group) and those not stimulated (control group). The effect has binary outcomes - one when the consumer receives the stimulus (factual) and zero when he/she does not recieve the stimulus (counterfactual).

![con](https://github.com/user-attachments/assets/6f912344-3efd-4c6c-9e46-8aa7c9e6d864)


**The stimulus is a treatment.*

The test and control groups must be randomized for an unbiased measurement. Choosing the groups randomly ensures that all covariates before the stimulus are equal for the groups. This means there is no covariate that determines which group a consumer belongs to. This experiment is hence called randomized controlled trial (RCT).

For example, if past (buying) frequency were the only confounder, the solution would be simple since the test group would be compared with the control group that had the same past frequency. In reality, there are more than 1 possible covariates that explains the causal association of the stimulus with the outcome.

![00](https://github.com/user-attachments/assets/8964b521-1dba-443e-a0e2-4b64d1bd7333)


Unlike predictive ML models where there’s a target and predictions are validated against test data, there’s no ground truth or target in causal models. Validating the robustness of causal models is the bottleneck.

**We can never observe both potential outcomes but only the one that actually occurs in causal models.**

# References

1. https://developers.google.com/meridian/docs/causal-inference/about-mmm-causal-inference-methodology

2. https://github.com/py-why/dowhy

