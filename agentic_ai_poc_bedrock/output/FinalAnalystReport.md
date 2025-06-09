# Customer Churn Analysis: Final Report

## Executive Summary

Our comprehensive analysis of customer behavior reveals critical patterns driving subscriber churn in our service. By applying advanced statistical methods and causal inference techniques, we've identified the true drivers of customer decisions to leave. Contract structure, support quality, usage frequency, and payment behavior emerge as the most significant factors affecting retention. This report consolidates our findings into actionable recommendations with visualized insights to guide strategic decision-making.

## Key Findings

### Primary Churn Drivers

![Key Churn Drivers](https://i.imgur.com/JCjvj16.png)

Our causal analysis reveals four major factors driving customer churn:

1. **Contract Structure** (25 percentage point impact)
   - Monthly contracts increase churn probability by ~25 percentage points versus annual contracts
   - Effect is strongest for new customers with low usage patterns (37 pp impact)
   - 34% of this effect operates through reduced service engagement

2. **Support Quality** (19 percentage point impact)
   - Each support call increases churn probability by ~7 percentage points
   - High support needs (>5 calls) increase churn by ~19 percentage points
   - Enhanced support interventions can reduce churn by 15 percentage points

3. **Usage Frequency** (17 percentage point impact)
   - Low usage significantly predicts churn across all customer segments
   - Each additional 10 usage instances reduces churn by 15-31 percentage points
   - Usage mediates the effects of both subscription type and contract length

4. **Payment Behavior** (13 percentage point impact)
   - Each week of payment delay increases churn probability by ~13 percentage points
   - 35% of this effect operates through increased support needs
   - Payment delays predict reduced usage over time

### Contract Length: The Strongest Predictor

![Survival Curves by Contract Type](https://i.imgur.com/mZ9RR5w.png)

Contract structure emerges as the single strongest predictor of retention:
- Annual contract customers have 3x longer median survival time (36 months vs. 14 months)
- Monthly subscribers show dramatically steeper drop-off, particularly in the first year
- Quarterly contracts provide moderate improvement but still underperform annual commitments

### Support Needs and Service Issues

![Support Calls vs. Churn](https://i.imgur.com/cLXMwO8.png)

Support interactions reveal critical customer satisfaction issues:
- Support needs above 5 calls correlate with 85%+ churn probability
- Enhanced support interventions at this threshold can reduce churn by 15.3 percentage points
- Most retained customers have 0-3 support calls, indicating satisfactory service experiences

### Usage Patterns and Engagement

![Usage Frequency Heatmap](https://i.imgur.com/GdxGbhK.png)

Customer engagement strongly predicts retention outcomes:
- Low-usage customers (<10 interactions/month) have 2-3x higher churn probability
- Usage frequency below 5 combined with low tenure (<12 months) creates the highest risk segment
- High usage (20+ interactions/month) correlates with retention even among newer customers

### Payment Behavior and Financial Health

![Payment Delay and Support Needs](https://i.imgur.com/EXWfvLq.png)

Payment patterns signal customer value perception:
- Strong correlation (r = 0.593) between payment delays and support calls
- Customers with payment delays >15 days show significant usage decline over time
- Financial behavior serves as both cause and early warning of churn

### Heterogeneous Effects Across Customer Segments

![Contract Effect by Segment](https://i.imgur.com/jSDG8kL.png)

Contract impact varies significantly across customer segments:
- New customers (<12 months tenure) with low usage (<10/month) see 37.1pp effect from contract type
- Tenured customers (12+ months) with high usage (10+/month) see only 12.2pp effect
- All segments show statistically significant effects, supporting universal importance of contracts

### Customer Journey Analysis

![Customer Journey Map](https://i.imgur.com/RBqY3cH.png)

The customer journey reveals critical decision points affecting retention:
- Initial contract selection heavily influences the entire customer lifecycle
- Support interactions represent crucial moments of truth in the customer experience
- Monthly contract → low usage → payment delay → support calls → churn emerges as the highest-risk pathway

### Non-Significant Factors

Demographic variables show minimal causal impact on retention:
- Age shows no significant relationship with churn (p > 0.5)
- Gender shows no significant relationship with churn (p > 0.5)
- Total spend has marginal effect after controlling for usage and contract type

## Strategic Recommendations

Based on our causal analysis, we recommend these targeted interventions:

### 1. Contract Structure Optimization

**Recommendation:** Incentivize annual contracts, especially for high-risk segments.

**Implementation:**
- Offer graduated discounts for longer commitments
- Create risk-free trial periods with guaranteed refunds
- Develop "save offers" converting monthly customers to annual terms
- Target new customers with low usage patterns as highest priority

**Expected Impact:** 25-37 percentage point reduction in churn probability for converted customers.

### 2. Support Quality Enhancement

**Recommendation:** Implement proactive support interventions for at-risk customers.

**Implementation:**
- Create early intervention protocol for customers reaching 4-5 support calls
- Develop specialized retention team for high-risk cases
- Implement root cause analysis to address systemic support drivers
- Set up automated alerts for cases needing immediate attention

**Expected Impact:** 15-19 percentage point reduction in churn for customers receiving enhanced support.

### 3. Usage Stimulation Program

**Recommendation:** Drive increased product engagement through targeted activation campaigns.

**Implementation:**
- Create personalized onboarding journeys emphasizing regular usage
- Develop feature highlight campaigns for underutilized functionality
- Implement usage-based incentives and gamification elements
- Target low-usage segments (1-10/month) as highest priority

**Expected Impact:** 15-31 percentage point reduction in churn for customers increasing usage by 10+ instances monthly.

### 4. Payment Experience Improvement

**Recommendation:** Reduce payment friction and address delayed payments promptly.

**Implementation:**
- Expand automatic payment options and incentives
- Implement early communication for payment issues
- Create flexible payment plans for financially stressed customers
- Address root causes of payment delays through customer feedback

**Expected Impact:** 13 percentage point reduction in churn for customers with improved payment timeliness.

### 5. Personalized Retention Strategy

**Recommendation:** Deploy targeted interventions based on individual churn risk profiles.

**Implementation:**
- Utilize causal forest model to estimate individual treatment effects
- Create segment-specific retention playbooks based on causal responses
- Implement dynamic intervention allocation based on ROI potential
- Focus resources on customers with highest intervention response probability

**Expected Impact:** Optimization of retention budget with 30%+ improvement in intervention effectiveness.

## Implementation Roadmap

![Retention Strategy Simulator](https://i.imgur.com/Q1mVs6c.png)

1. **Immediate Actions (0-30 days)**
   - Deploy contract conversion offers to highest-risk segments
   - Implement enhanced support protocol for customers with 4+ support calls
   - Begin early intervention for customers with payment delays >15 days

2. **Short-Term Initiatives (1-3 months)**
   - Launch usage stimulation program for low-engagement segments
   - Develop personalized retention playbooks by segment
   - Implement payment experience improvements

3. **Medium-Term Programs (3-6 months)**
   - Deploy comprehensive customer journey optimization
   - Implement full-scale predictive intervention system
   - Establish continuous monitoring and optimization framework

4. **Long-Term Strategy (6+ months)**
   - Redesign product experience to address usage barriers
   - Develop advanced early warning system with real-time intervention
   - Create comprehensive customer health scoring system

## Monitoring Framework

![Customer Explorer Dashboard](https://i.imgur.com/nfjT6T0.png)

To ensure sustained improvement, implement these tracking metrics:

1. **Primary KPIs**
   - Overall churn rate (monthly/quarterly/annual)
   - Average customer lifetime value
   - Retention ROI by intervention type

2. **Leading Indicators**
   - Contract mix (% annual vs. quarterly vs. monthly)
   - Support calls per customer (monthly average)
   - Usage frequency trends by segment
   - Payment delay patterns

3. **Intervention Metrics**
   - Conversion rate for contract upgrade offers
   - Resolution rate for support interventions
   - Engagement lift from usage campaigns
   - Payment timing improvements

## Conclusion

![Executive Summary Dashboard](https://i.imgur.com/5sDimQE.png)

Our analysis reveals that customer churn is primarily driven by addressable operational factors rather than fixed customer characteristics. By focusing on contract structure optimization, support quality enhancement, usage stimulation, and payment experience improvement, we can significantly reduce churn and increase customer lifetime value.

The causal relationships identified provide clear direction for intervention priorities, with contract structure representing the single highest-impact opportunity. By implementing this comprehensive retention strategy, we project potential churn reduction of 30-40% within the first year while simultaneously increasing customer satisfaction and lifetime value.

These findings should be used to guide both immediate tactical interventions and longer-term strategic planning to create a more sustainable customer relationship model.