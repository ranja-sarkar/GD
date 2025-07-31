# Introduction

Predictive maintenance techniques are utilized to assess the condition of operational equipments, allowing for maintenance to be scheduled as needed. This method offers potential cost savings compared to preventive maintenance.

# Problem statement

Development of a supervised machine learning model to predict the likelihood of device malfunction from aggregated IoT data of daily frequency. 


# Data
The data provided is 6.4 MB, clean one with no missing data. The dataset has 12 variables, one of which is datetime. The target variable is 'malfunction'.

# Solution Approach

A logistic regression model for binary classification is being built to predict if one (or more) of the devices would fail or not the next day. Decision threshold have been tuned (imbalanced dataset) for a comparison of the FPs and FNs in each case.


