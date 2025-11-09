# Causal Impact of Delivery Delays on Customer Satisfaction
### A Causal Inference & A/B Testing Project Using the Olist E-commerce Dataset  
Author: **Xuhui Liu** (UIUC Statistics PhD)

---

## 📌 Project Overview
This project estimates the **causal effect** of delivery delays on:
- Customer review scores  
- Repeat purchase behavior  
- High-sensitivity customer segments (uplift modeling)

Treatment definition:
- **T = 1** if actual delivery date > estimated delivery date  
- **T = 0** otherwise

This replicates real challenges faced by teams at **Uber, DoorDash, Instacart, Airbnb, and Booking.com**.

---

## ✅ Goals
- Estimate **ATE (average treatment effect)** of late delivery.
- Use **propensity score modeling** (Logistic Regression + Random Forest).
- Use **AIPW (doubly robust)** estimator.
- Estimate **heterogeneous treatment effects (HTE)** using:
  - Causal Forests
  - Uplift Models
- Provide **business recommendations** for reducing churn.

---

## ✅ Repository Structure

