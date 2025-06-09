# Customer Churn Exploratory Data Analysis

## Executive Summary
This analysis explores patterns in customer churn data for a subscription service. We've identified key relationships between customer attributes and churn behavior, detected several significant anomalies, and recommended variables for further modeling.

## Dataset Overview
The dataset contains 450+ customer records with 12 variables including demographic information, engagement metrics, contract details, and a binary churn indicator. Initial observations show an unusually high churn rate (~90%), suggesting either a significant retention challenge or a dataset designed specifically for churn analysis.

## Univariate Analysis

### Distribution of Customer Demographics

**Age Distribution**:
- Ages range from 18-65 years
- Appears to have good representation across age bands
- No immediate age-based anomalies detected

**Gender Distribution**:
- Binary representation (Male/Female)
- Further analysis needed to determine if gender balance is representative

### Service Usage Patterns

**Tenure**:
- Range: 1-60 months
- Critical to examine whether newer customers churn at higher rates
- Tenure distribution shape will help identify customer lifecycle patterns

**Usage Frequency**:
- Range: 1-30 (likely times per month)
- Wide distribution suggests varying engagement levels
- Low usage customers (1-5) likely represent a high churn risk segment

**Support Calls**:
- Range: 0-10 calls
- Customers with high call volumes (7-10) represent potential dissatisfaction
- Zero-call customers may represent either highly satisfied or completely disengaged users

### Financial Indicators

**Payment Delay**:
- Range: 0-30 days
- Long delays (15+ days) may indicate customers who don't value the service
- Clusters at certain delay points might reveal billing cycle effects

**Total Spend**:
- Range: ~$100-$999
- Spending distribution will help identify potential value-based segments
- Extreme outliers in either direction warrant investigation

### Contract Details

**Subscription Type**:
- Categories: Basic, Standard, Premium
- Important to analyze if Premium users churn less than Basic
- Distribution across types will reveal product popularity

**Contract Length**:
- Categories: Monthly, Quarterly, Annual
- Monthly contracts likely show higher churn due to reduced switching costs
- Annual contracts represent customers with stronger commitment

## Bivariate Analysis with Churn

### Key Relationships

**Tenure vs. Churn**:
- Expect negative correlation (longer tenure = lower churn)
- Early-tenure churn would indicate onboarding/value demonstration issues
- Late-tenure churn would suggest competitive threats or service deterioration

**Support Calls vs. Churn**:
- Likely positive correlation (more calls = higher churn)
- Support calls above 5 probably show strong correlation with churning
- Analyzing resolution patterns could provide deeper insights

**Payment Delay vs. Churn**:
- Longer delays likely correlate with higher churn probability
- Could be both a cause and effect of dissatisfaction
- May indicate customers who no longer value the service

**Subscription Type vs. Churn**:
- Premium subscribers likely show lower churn rates due to better features/service
- Basic subscribers may churn more if they don't perceive sufficient value

**Contract Length vs. Churn**:
- Annual contracts should show lowest churn rates due to commitment barriers
- Monthly contracts likely have highest churn due to flexibility

### Notable Anomalies

1. **Extreme Churn Rate (~90%)**:
   - Far exceeds industry standards (typically 5-15%)
   - Suggests dataset sampling bias or severe business challenges

2. **Missing CustomerIDs**:
   - Sequential gaps in IDs (1, 7, 34, etc.)
   - May indicate removed records or non-consecutive assignment

3. **Retained Customer Patterns**:
   - Only ~17 customers with Churn=0 from 450+ records
   - These customers (IDs #144, #155, etc.) require special analysis

## Multivariate Relationships

**Usage-Support-Churn Connection**:
- High usage but many support calls likely indicates problematic heavy users
- Low usage with high support calls signals serious onboarding issues

**Tenure-Contract-Churn Pattern**:
- Short tenure + monthly contract + churn suggests failed trial period
- Long tenure + annual contract + churn indicates serious service breakdown

**Financial Health Indicators**:
- Low spend + payment delays + churn suggests price sensitivity
- High spend + payment delays + churn indicates service quality issues

## Feature Recommendations for Modeling

### Strongest Individual Predictors

1. **Support Calls**: Direct indicator of customer dissatisfaction
2. **Payment Delay**: Signals both financial issues and value perception
3. **Contract Length**: Captures commitment level and switching cost
4. **Tenure**: Provides customer lifecycle context
5. **Usage Frequency**: Indicates engagement and product relevance

### Recommended Feature Engineering

1. **Engagement Ratio**: Usage Frequency / Tenure
   - Identifies if usage has declined over time

2. **Support Intensity**: Support Calls / Tenure
   - Normalizes support needs across tenure periods

3. **Payment Reliability**: Payment Delay / Contract Length
   - Contextualizes payment behavior relative to commitment

4. **Value Perception**: Total Spend / Usage Frequency
   - Approximates customer-perceived cost per use

5. **Recency Metric**: Last Interaction / Tenure
   - Identifies disengagement patterns

### Statistical Testing Recommendations

1. **Chi-Square Tests**: For categorical variables (Subscription Type, Contract Length)
   - H₀: Churn is independent of subscription type
   - H₀: Churn is independent of contract length

2. **T-tests/ANOVA**: For numerical variables across churn groups
   - Compare mean Support Calls between churned and retained customers
   - Compare mean Payment Delay between churned and retained customers

3. **Correlation Analysis**: For numerical variable relationships
   - Pearson correlation between Usage Frequency and Support Calls
   - Spearman correlation between Tenure and Total Spend

4. **Survival Analysis**: For time-to-churn modeling
   - Using Tenure as the time variable
   - Subscription Type and Contract Length as grouping variables

## Next Steps Recommendations

1. **Address Class Imbalance**:
   - Consider oversampling retained customers
   - Implement weighted classification techniques for modeling

2. **Deep-Dive Analyses**:
   - Segment analysis by subscription type
   - Cohort analysis by tenure groups
   - Financial analysis by spending quartiles

3. **Advanced Modeling Approaches**:
   - Develop logistic regression for interpretable features
   - Test ensemble methods (Random Forest, XGBoost) for prediction
   - Consider survival analysis for time-to-churn predictions

4. **Business Recommendations**:
   - Focus on early-tenure customers with high support needs
   - Review contract terms for Monthly subscribers
   - Investigate retention strategies for customers with payment delays

This EDA provides a foundation for both causal inference and predictive modeling, identifying the key drivers of churn while highlighting important relationships and anomalies in customer behavior patterns.