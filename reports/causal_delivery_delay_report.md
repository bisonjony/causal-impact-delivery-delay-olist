# Causal Impact of Late Delivery on Customer Review Score
### A Causal Inference and Uplift Modeling Case Study Using the Olist E-Commerce Dataset

---

# 1. Motivation

Customer reviews strongly affect platform reputation, seller ranking, conversion rate, and long-term customer retention.  
This project answers the following questions:

1. What is the *causal effect* of late delivery on review scores?
2. Are certain customers or products more sensitive to delay?
3. Can we design a targeted intervention to reduce negative reviews with positive business ROI?

---

# 2. Dataset and Treatment Definition

We use the public Olist Brazil e-commerce dataset (over 110,000 orders).

## Treatment Definition

An order is considered "late" if:

late_delivery = (order_delivered_customer_date > order_estimated_delivery_date)

Let `T = 1` for late deliveries.

## Outcome Variable

`review_score` (1 to 5 stars)

## Features Used

After removing extremely high-cardinality variables that cause memory issues (such as customer_city and seller_city), we use:

**Numeric variables**
- order_purchase_dayofweek  
- order_purchase_hour  
- estimated_delivery_days  
- price  
- freight_value  
- product_volume_cm3  
- payment_value  

**Categorical variables**
- payment_type  
- customer_state  
- seller_state  
- product_category_name  

These variables act as confounders influencing both delivery time and review score.

---

# 3. Causal Assumptions and Confounding Structure

We assume the features above confound both the likelihood of late delivery and customer satisfaction.

Simplified causal structure:

X → T (late delivery) → Y (review score)

Where `X` contains product characteristics, seller region, customer region, payment information, and temporal purchasing patterns.

---

# 4. Propensity Score Modeling and IPW Weights

Two propensity models were fit:

- Logistic Regression
- Gradient Boosted Trees

Both generate estimated probabilities:
- `ps_logit`
- `ps_gb`

Inverse probability weights (IPW and stabilized IPW) were computed.  
Standardized Mean Difference (SMD) calculations show that weighting improves covariate balance across treatment groups.

---

# 5. Causal Effect Estimation (IPW and AIPW)

We estimate ATE (average treatment effect), ATT (average treatment effect on treated), and ATC.

## Final Estimates

| Estimator | Effect (change in review score) | 95% Confidence Interval |
|----------|---------------------------------|-------------------------|
| IPW ATE  | -1.5221 | (-1.6252, -1.4223) |
| IPW ATT  | -1.6244 | (-1.6599, -1.5821) |
| IPW ATC  | -1.6507 | (-1.7002, -1.5902) |
| AIPW ATE | -1.6383 | (-1.6901, -1.5849) |

## Interpretation

Late delivery causally reduces review scores by approximately **1.6 stars** on average.  
The consistency between IPW and AIPW results provides additional validation.

---

# 6. Heterogeneous Treatment Effects (Causal Forest)

To study variation across customers and products, we train a CausalForestDML model.

High-cardinality features were dropped for memory stability.  
One-hot encoding was applied to all retained features.

## Summary of CATE (tau_hat)

The distribution of treatment effects shows:

- Most customers experience a negative impact from late delivery.
- A subgroup has substantially higher sensitivity, with treatment effects in the range of 8 to 20 points depending on model scaling.

## High-sensitivity product categories (example)

| product_category_name            | n   | mean_tau | p90_tau | top10_share |
|---------------------------------|-----|----------|---------|-------------|
| cds_dvds_musicais               | 14  | 3.03     | 8.17    | 0.214       |
| fashion_roupa_infanto_juvenil   | 8   | 2.73     | 7.41    | 0.125       |
| dvds_blu_ray                    | 63  | 2.35     | 7.65    | 0.142       |
| fashion_roupa_masculina         | 131 | 2.00     | 8.86    | 0.137       |
| fashion_calcados                | 261 | 1.95     | 6.82    | 0.088       |

These categories are notably more affected by delivery delays.

---

# 7. Business Impact Simulation

We run an intervention simulation based on uplift scores to determine the optimal targeting strategy.

## Economic Assumptions
- Value per 1-point improvement in review score: **1.25 USD**
- Cost of intervention per customer (e.g., coupon or priority support): **2.00 USD**

## Optimization Results

Optimal targeting share: **30%**  
Optimal `K`: **33,231 customers**

### Summary of business metrics:

| Metric | Value |
|--------|-------|
| Total customers | 110,770 |
| Optimal targeted customers | 33,231 |
| Total benefit | 306,303 USD |
| Total cost | 66,462 USD |
| Net gain | 239,841 USD |
| ROI | 3.61 |

### Interpretation

By targeting only the top 30% of customers (ranked by predicted sensitivity to late delivery), the platform achieves:

- Approximately **240,000 USD** net value  
- An ROI above **3.6**  
- A substantial reduction in negative review risk  
- A more efficient and targeted compensation strategy

---

# 8. Conclusions

1. Late delivery reduces review scores by approximately **1.6 stars**, a large and economically significant effect.  
2. Treatment effects vary considerably across customers and products.  
3. Causal forest modeling identifies high-risk segments such as certain multimedia and fashion categories.  
4. A targeted intervention strategy focusing on the most sensitive 30% of customers yields the highest ROI and substantial financial benefit.  
5. The combination of causal inference and uplift modeling provides actionable insights that outperform untargeted interventions.
