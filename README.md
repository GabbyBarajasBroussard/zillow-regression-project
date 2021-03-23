# Predicting Churn at Telco
## About the project
### Goals
#### Predict the tax values of single unit properties that the tax district assessed using the property data from those whose last transaction was during the peak real estate demand months of May and August 2017. The deliverables for the project are acquire.py and prepare.py.


## Data Dictionary
| Terminology         | Definition                                                                                                                                                                                                                                                                                                                           |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                                                                                                                                                                                                                                                                     |
| Alpha               | Alpha is the likelihood that a true population parameter lays outside the confidence interval.                                                                                                                                                                                                                                       |
| Confidence Interval | The probability that a population parameter will fall between a set of values for a certain proportion of times.                                                                                                                                                                                                                     |
<br>

## Hypothesis Testing

    First Hypothesis 
    𝐻$0$ :  Homes have the same mean tax value in each county.
    𝐻𝑎 : Homes in Los Angeles have a higher mean tax value than in Ventura or Orange Counties.
    alpha ( 𝛼 ): 1 - confidence level (95% confidence level -> 𝛼=.05 )
    Test Used: 2 Tailed T-Tet
    Finding: The null hypothesis is reject meaning that homes in Los Angeles County have a higher mean value.


    Second Hypothesis
    𝐻0 : Number of bathrooms have no correlation with tax value. 
    𝐻𝑎 : Homes with more bathrooms are correlated with higher tax values.
    alpha ( 𝛼 ): 1 - confidence level (95% confidence level -> 𝛼=.05 )
    Test Used: Pearson's Correlation Coefficient
    Finding: Homes with more bathrooms are correlated with higher tax values.
## Data Science Pipeline Used
acquire.py
<ol>
<li>acquire data from csv gathered from sql. </li>
</ol><br>
prepare.py
<ol>
<li> address missing data </li>
<li> address outliers </li>
<li> split into train, validate, test</li>
</ol><br>
explore
<ol>
<li> plot correlation matrix of all variables </li>
<li> test each hypothesis </li> 
</ol><br>
feature engineering<br>
<ol>
<li> split and scale the data</ul>
<li> find top 3 features using KSelect Best and RFE</li> 
model
<ol>
<li> try different modeling algorithms: Lasso Lars, OLS, Polynomial Regression and Tweedie Regressor (GLM)
</li> 
<li> evaluate on train </li>
<li> select top models to evaluate on validate </li>
<li> select top model </li>
<li> run model on test to verify. </li>
 </ol><br>
conclusion
<ol>
<li> summarize findings </li>
<li> make recommendations </li>
<li> next steps </li>
<li> how to run with new data. </li> 
</ol><br><br>

## Conclusion

<ul>
<li>I reject the null hypothesis that homes have the same mean tax value in each county.
<li>I reject the null hypothesis that number of bathrooms have no correlation with tax value.
<li>Using Feature Engineering, the top 3 features are square_feet', 'bedroom_count', and 'bathroom_count'.
<li>The best performing model is the Tweedie Regressor using the top features.
<li>The median tax rate for Los Angeles County is 1.26, Ventura County is 1.12 and Orange County is 1.15.
<li>If more data and time were available, investigating number of stories, presence of hoa, and the combination of bedrooms and bathrooms as features for predicting tax value.
</ul>
## How to reproduce the results
#### You may download acquire.py and prepare.py. You will need your own env.py file with your SQL credentials in order to access the SQL server.
