import pandas as pd

def create_treatment(df):
    """Adds delivery delay variables used for causal inference."""
    
    # Convert timestamps
    df["order_estimated_delivery_date"] = pd.to_datetime(df["order_estimated_delivery_date"])
    df["order_delivered_customer_date"] = pd.to_datetime(df["order_delivered_customer_date"])
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

    # Treatment indicator
    df["late_delivery"] = (
        df["order_delivered_customer_date"] > df["order_estimated_delivery_date"]
    ).astype(int)

    # Delivery time features
    df["actual_delivery_days"] = (
        df["order_delivered_customer_date"] - df["order_purchase_timestamp"]
    ).dt.days

    df["estimated_delivery_days"] = (
        df["order_estimated_delivery_date"] - df["order_purchase_timestamp"]
    ).dt.days

    return df
