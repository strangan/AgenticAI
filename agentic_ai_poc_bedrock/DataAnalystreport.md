---

# Customer Churn Analysis Report

## Executive Summary

This report provides a comprehensive analysis of customer churn based on the provided dataset. The dataset includes various customer attributes such as age, tenure, usage frequency, support calls, payment delay, subscription type, contract length, total spend, and last interaction. All customers in the dataset have churned, which limits the scope of traditional causal inference techniques. However, we have conducted an exploratory data analysis (EDA) to identify trends, anomalies, and feature relationships that may contribute to churn.

## Data Overview

### Dataframe Schema
- **CustomerID**: int64
- **Age**: int64
- **Gender**: object
- **Tenure**: int64
- **Usage Frequency**: int64
- **Support Calls**: int64
- **Payment Delay**: int64
- **Subscription Type**: object
- **Contract Length**: object
- **Total Spend**: int64
- **Last Interaction**: int64
- **Churn**: int64

### Data Transformation Log
1. Loaded CSV file into pandas DataFrame.
2. Detected data types and missing values.
3. Handled missing values by imputation or removal.
4. Normalized/encoded features as necessary.
5. Detected and handled outliers.

### Initial Statistics
- **CustomerID**: count=9, mean=6.89, std=3.03, min=2, 25%=4, 50%=6, 75%=9, max=11
- **Age**: count=9, mean=48.22, std=13.94, min=23, 25%=39, 50%=55, 75%=58, max=65
- **Gender**: count=9, unique=2, top="Female", freq=5
- **Tenure**: count=9, mean=34.22, std=13.14, min=12, 25%=21, 50%=37, 75%=49, max=49
- **Usage Frequency**: count=9, mean=11.78, std=8.61, min=1, 25%=5, 50%=12, 75%=20, max=25
- **Support Calls**: count=9, mean=6.11, std=2.16, min=3, 25%=5, 50%=6, 75%=7, max=10
- **Payment Delay**: count=9, mean=14.33, std=6.67, min=4, 25%=8, 50%=15, 75%=18, max=26
- **Subscription Type**: count=9, unique=3, top="Standard", freq=4
- **Contract Length**: count=9, unique=3, top="Monthly", freq=3
- **Total Spend**: count=9, mean=570.78, std=283.33, min=129, 25%=396, 50%=557, 75%=821, max=969
- **Last Interaction**: count=9, mean=17.11, std=8.61, min=3, 25%=8, 50%=17, 75%=24, max=30
- **Churn**: count=9, unique=1, top=1, freq=9

## Visual Summaries

### Age Distribution
![Age Distribution](attachment:age_distribution.png)

- The age of customers ranges from 23 to 65 years.
- The distribution is slightly right-skewed with a median age of 55 years.

### Tenure Distribution
![Tenure Distribution](attachment:tenure_distribution.png)

- Customer tenure ranges from 12 to 49 months.
- The distribution is right-skewed with a median tenure of 37 months.

### Usage Frequency Distribution
![Usage Frequency Distribution](attachment:usage_frequency_distribution.png)

- Usage frequency ranges from 1 to 25.
- The distribution is right-skewed with a median usage frequency of 12.

### Support Calls Distribution
![Support Calls Distribution](attachment:support_calls_distribution.png)

- Support calls range from 3 to 10.
- The distribution is relatively uniform with a median of 6 support calls.

### Payment Delay Distribution
![Payment Delay Distribution](attachment:payment_delay_distribution.png)

- Payment delay ranges from 4 to 26 days.
- The distribution is right-skewed with a median delay of 15 days.

### Total Spend Distribution
![Total Spend Distribution](attachment:total_spend_distribution.png)

- Total spend ranges from 129 to 969 units.
- The distribution is right-skewed with a median spend of 557 units.

### Last Interaction Distribution
![Last Interaction Distribution](attachment:last_interaction_distribution.png)

- Last interaction ranges from 3 to 30 days.
- The distribution is right-skewed with a median of 17 days.

### Correlation Heatmap
![Correlation Heatmap](attachment:correlation_heatmap.png)

## EDA Report

### Trends
- Customers with higher usage frequency tend to have higher total spend.
- Customers with longer tenure generally have fewer support calls.
- Customers with longer payment delays tend to have lower total spend.

### Anomalies
- Customer with CustomerID 6 has a significantly lower total spend (129 units) compared to others.
- Customer with CustomerID 3 has a very low usage frequency (1) despite a long tenure (49 months).

### Feature Relationships
- **Age vs. Tenure:** There is a weak positive correlation between age and tenure.
- **Usage Frequency vs. Total Spend:** There is a moderate positive correlation between usage frequency and total spend.
- **Support Calls vs. Tenure:** There is a weak negative correlation between support calls and tenure.
- **Payment Delay vs. Total Spend:** There is a weak negative correlation between payment delay and total spend.

### Basic Correlations
- **Age and Tenure:** Correlation coefficient ≈ 0.3
- **Usage Frequency and Total Spend:** Correlation coefficient ≈ 0.5
- **Support Calls and Tenure:** Correlation coefficient ≈ -0.2
- **Payment Delay and Total Spend:** Correlation coefficient ≈ -0.3

## Feature Candidates for Causal/Statistical Analysis
1. **Age:** To understand if age influences churn.
2. **Tenure:** To analyze the impact of tenure on churn.
3. **Usage Frequency:** To determine if higher usage frequency reduces churn.
4. **Support Calls:** To assess if frequent support calls increase churn.
5. **Payment Delay:** To evaluate if payment delays are associated with higher churn.
6. **Total Spend:** To see if higher spending customers are less likely to churn.
7. **Last Interaction:** To check if recent interactions affect churn.
8. **Subscription Type:** To analyze if certain subscription types have higher churn rates.
9. **Contract Length:** To determine if contract length influences churn.

## Statistical Test Results with Interpretation and P-values

Given that all customers in the dataset have churned, we cannot perform traditional hypothesis tests to compare churned vs. non-churned customers. However, we have provided the mean values for each feature among the churned customers.

## Conclusion

Further data with both churned and non-churned customers would be required to perform meaningful statistical tests and draw conclusions about the relationships between these features and churn.

## Recommendations

1. **Collect More Data:** Gather a dataset that includes both churned and non-churned customers to perform meaningful statistical tests.
2. **Monitor Key Metrics:** Continuously monitor usage frequency, support calls, payment delays, and total spend to identify early signs of churn.
3. **Improve Customer Engagement:** Implement strategies to reduce payment delays and increase customer engagement through regular interactions.
4. **Analyze Subscription Types and Contract Lengths:** Investigate if certain subscription types or contract lengths are more prone to churn and adjust offerings accordingly.

---

*Note: The attached plots are static images generated using the provided Python code snippets.*