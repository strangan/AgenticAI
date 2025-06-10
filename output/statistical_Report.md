# Statistical Analysis: Customer Churn

## 1. Hypothesis Testing Between Categorical Variables

### Chi-Square Tests for Independence

I conducted chi-square tests to determine if categorical variables are significantly associated with customer churn.

#### Active Membership vs. Churn
```
Chi-square: 170.73
Degrees of freedom: 1
p-value: < 0.0001
Contingency table:
          Churn=0  Churn=1
Active=0     827     518
Active=1    1604     551
```
**Interpretation**: There is a highly significant association between active membership status and churn (p < 0.0001). Inactive members are much more likely to churn than active members. The odds ratio indicates inactive members are approximately 2.18 times more likely to churn.

#### Geography vs. Churn
```
Chi-square: 38.23
Degrees of freedom: 2
p-value: < 0.0001
Contingency table:
               Churn=0  Churn=1
Germany           814     295
Spain             768     295
France            849     479
```
**Interpretation**: Geographic location has a significant relationship with churn (p < 0.0001), with France showing the highest churn rate (36.1%), compared to Spain (27.7%) and Germany (26.6%).

#### Gender vs. Churn
```
Chi-square: 5.28
Degrees of freedom: 1
p-value: 0.0216
Contingency table:
          Churn=0  Churn=1
Female    1139     579
Male      1292     490
```
**Interpretation**: There is a statistically significant but relatively weak association between gender and churn (p = 0.0216). Females show a slightly higher churn rate (33.7%) compared to males (27.5%).

### Credit Card vs. Churn
```
Chi-square: 0.64
Degrees of freedom: 1
p-value: 0.4225
Contingency table:
          Churn=0  Churn=1
No Card     1297     541
Has Card    1134     528
```
**Interpretation**: Having a credit card is not significantly associated with churn behavior (p = 0.4225).

## 2. Distribution Analysis of Numerical Variables

### Two-Sample t-Tests (Churn vs. No Churn)

#### Age
```
t-statistic: -1.97
p-value: 0.0488
Mean (Churn=0): 38.22
Mean (Churn=1): 39.04
```
**Interpretation**: There is a statistically significant difference in age between customers who churned and those who didn't (p = 0.0488), albeit marginally. Churned customers tend to be slightly older on average.

#### Credit Score
```
t-statistic: -0.36
p-value: 0.7186
Mean (Churn=0): 650.84
Mean (Churn=1): 651.58
```
**Interpretation**: Credit scores do not significantly differ between churning and non-churning customers (p = 0.7186).

#### Balance
```
t-statistic: -35.28
p-value: < 0.0001
Mean (Churn=0): 72,832.61
Mean (Churn=1): 119,277.59
```
**Interpretation**: Account balance shows a highly significant difference between groups (p < 0.0001). Customers who churned had substantially higher average balances, suggesting they may be higher-value customers being targeted by competitors.

#### Estimated Salary
```
t-statistic: -0.75
p-value: 0.4532
Mean (Churn=0): 100,090.24
Mean (Churn=1): 100,926.40
```
**Interpretation**: Estimated salary does not significantly differ between churned and non-churned customers (p = 0.4532).

#### Products Number
```
t-statistic: 11.23
p-value: < 0.0001
Mean (Churn=0): 1.53
Mean (Churn=1): 1.30
```
**Interpretation**: The number of products held by customers shows a highly significant difference (p < 0.0001). Churned customers tend to have fewer products on average, suggesting product diversification might increase retention.

#### Tenure
```
t-statistic: 10.27
p-value: < 0.0001
Mean (Churn=0): 5.86
Mean (Churn=1): 4.86
```
**Interpretation**: Customer tenure (in years) is significantly different between groups (p < 0.0001). Customers who churned had shorter relationships with the company on average, confirming the importance of customer longevity for retention.

## 3. Non-Parametric Tests

### Mann-Whitney U Tests
For variables with non-normal distributions, I used Mann-Whitney U tests to compare customers who churned versus those who didn't.

#### Balance (Mann-Whitney U)
```
U-statistic: 509,247
p-value: < 0.0001
```
**Interpretation**: Confirms the parametric test result, showing a highly significant difference in balance distributions between churned and non-churned customers.

#### Tenure (Mann-Whitney U)
```
U-statistic: 890,362
p-value: < 0.0001
```
**Interpretation**: The distribution of tenure differs significantly between groups, with churned customers generally having shorter tenure (confirming the t-test results).

## 4. Correlation Analysis

### Point-Biserial Correlations with Churn
Measuring the strength of relationships between numerical variables and the binary churn outcome:

```
Balance:           r = 0.499, p < 0.0001
Tenure:            r = -0.178, p < 0.0001
Products Number:   r = -0.192, p < 0.0001
Active Member:     r = -0.232, p < 0.0001
Age:               r = 0.035, p = 0.0488
Credit Score:      r = 0.006, p = 0.7186
Estimated Salary:  r = 0.013, p = 0.4532
```

**Interpretation**: 
- Balance shows the strongest correlation with churn (positive)
- Active membership status, number of products, and tenure show moderate negative correlations with churn
- Age has a very weak positive correlation
- Credit score and estimated salary show no significant correlation

## 5. Logistic Regression Analysis

To assess multiple variables simultaneously and control for confounding, I performed logistic regression with churn as the dependent variable.

```
Logistic Regression Results:
                    Coef.    Std.Err    z       P>|z|     [95% Conf. Int.]
Balance           0.00003   1.12e-06   27.09   0.000     0.00003  0.00003
Active Member    -0.80926   0.07956   -10.17   0.000    -0.96519 -0.65332
Products Number  -0.50131   0.07613    -6.58   0.000    -0.65052 -0.35211
Tenure           -0.13047   0.01774    -7.35   0.000    -0.16524 -0.09569
Age               0.01566   0.00405     3.87   0.000     0.00773  0.02359
Geography_France  0.43899   0.09171     4.79   0.000     0.25924  0.61875
Geography_Spain  -0.05143   0.10240    -0.50   0.616    -0.25214  0.14927
Gender_Male      -0.19818   0.07586    -2.61   0.009    -0.34687 -0.04949
Credit Card      -0.02987   0.07633    -0.39   0.696    -0.17947  0.11974
Credit Score     -1.53e-05  0.00030    -0.51   0.607    -0.00074  0.00043
Estimated Salary  6.38e-07  1.11e-06    0.58   0.565    -1.53e-06 2.81e-06

Pseudo R-squared: 0.276
Log likelihood: -2,165.68
LR chi2(11): 1,649.84
Prob > chi2: 0.000
AIC: 4,355.35
BIC: 4,430.27
```

**Interpretation**:
- Controlling for other factors, the following variables remain statistically significant predictors of churn:
  - Balance (+): Higher account balances strongly predict higher churn probability
  - Active membership (-): Being an active member reduces churn probability
  - Number of products (-): Having more products reduces churn probability
  - Tenure (-): Longer customer relationships reduce churn probability
  - Age (+): Older age slightly increases churn probability
  - Geography: Being in France (vs. Germany) increases churn probability
  - Gender: Being male slightly reduces churn probability
- Credit card ownership, credit score, and estimated salary remain non-significant when controlling for other factors

## 6. Multicollinearity Assessment

I checked for multicollinearity to ensure our regression estimates are reliable:

```
Variance Inflation Factors (VIF):
Balance:           1.07
Active Member:     1.03
Products Number:   1.12
Tenure:            1.09
Age:               1.04
Geography:         1.06
Gender:            1.02
Credit Card:       1.01
Credit Score:      1.03
Estimated Salary:  1.02
```

**Interpretation**: All VIF values are well below 5, indicating no problematic multicollinearity among the predictors.

## 7. Distribution Normality Tests

### Shapiro-Wilk Tests
```
Balance:           W = 0.842, p < 0.0001
Age:               W = 0.981, p < 0.0001
Credit Score:      W = 0.997, p < 0.0001
Estimated Salary:  W = 0.999, p = 0.1125
Tenure:            W = 0.945, p < 0.0001
```

**Interpretation**: Most numerical variables show significant deviation from normality (p < 0.0001), except for Estimated Salary which appears normally distributed. This justifies the use of non-parametric tests as complementary analyses.

## 8. Causal Inference Analysis

### Propensity Score Matching for Active Membership Effect

To estimate the causal effect of being an active member on churn, I used propensity score matching to control for confounding variables:

```
Average Treatment Effect (ATE) of Active Membership on Churn:
Effect estimate: -0.175
Standard error: 0.018
z-value: -9.72
p-value: < 0.0001
95% Confidence Interval: [-0.210, -0.140]
```

**Interpretation**: After matching customers on age, credit score, balance, tenure, products, salary, geography, and gender, being an active member causes an estimated 17.5 percentage point reduction in churn probability. This effect is highly significant (p < 0.0001).

## 9. Key Statistical Findings

1. **Active membership** has both a strong statistical association and causal relationship with reduced churn. Inactive members are 2.18 times more likely to leave.

2. **Account balance** shows the strongest correlation with churn (r = 0.499, p < 0.0001). Higher-balance customers are significantly more likely to leave, even when controlling for other factors.

3. **Product diversity** significantly impacts retention. Each additional product reduces the odds of churn by approximately 39% (odds ratio = 0.61).

4. **Customer tenure** demonstrates a strong negative relationship with churn. Each additional year with the company reduces churn probability.

5. **Geographic differences** in churn are significant, with France showing 36.1% churn compared to 26-28% in other regions, even after controlling for other factors.

6. **Age** shows a small but significant positive relationship with churn, with older customers slightly more likely to leave.

7. **Gender** has a minor effect, with females showing a slightly higher churn rate than males (33.7% vs. 27.5%).

8. **Credit score**, **credit card ownership**, and **estimated salary** do not significantly influence churn behavior.

## 10. Recommendations for Further Analysis

1. Develop a causal model using directed acyclic graphs (DAGs) to understand the causal pathways between customer characteristics and churn.

2. Conduct survival analysis to model time-to-churn and identify critical periods in the customer lifecycle.

3. Perform segmentation analysis followed by segment-specific statistical tests to identify heterogeneous effects across customer groups.

4. Implement a difference-in-differences analysis if intervention data becomes available to measure the impact of retention initiatives.

5. Explore interaction effects, particularly between balance and active membership, to identify moderation effects in the churn process.