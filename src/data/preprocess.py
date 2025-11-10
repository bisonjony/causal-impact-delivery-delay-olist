import pandas as pd

import pandas as pd

def merge_olist_tables(df_dict):
    """
    Merge key Olist tables into a complete order-item level dataset
    with customer, seller, product, payment, and review information.
    """

    orders = df_dict["orders"]
    items = df_dict["order_items"]
    payments = df_dict["order_payments"]
    reviews = df_dict["order_reviews"]
    products = df_dict["products"]
    customers = df_dict["customers"]
    sellers = df_dict["sellers"]

    # 1. Merge orders with order_items (1-to-many)
    df = orders.merge(items, on="order_id", how="left")

    # 2. Merge aggregated payments (sum over multiple payment attempts)
    payment_agg = payments.groupby("order_id").agg({
        "payment_value": "sum",
        "payment_type": "first"
    }).reset_index()

    df = df.merge(payment_agg, on="order_id", how="left")

    # 3. Merge reviews (one per order)
    df = df.merge(
        reviews[["order_id", "review_score"]],
        on="order_id", how="left"
    )

    # 4. Merge product information
    df = df.merge(
        products[[
            "product_id",
            "product_category_name",
            "product_weight_g",
            "product_length_cm",
            "product_height_cm",
            "product_width_cm"
        ]],
        on="product_id",
        how="left"
    )

    # 5. Merge customer geo info
    df = df.merge(
        customers[[
            "customer_id",
            "customer_city",
            "customer_state"
        ]],
        on="customer_id",
        how="left"
    )

    # 6. Merge seller geo info
    df = df.merge(
        sellers[[
            "seller_id",
            "seller_city",
            "seller_state"
        ]],
        on="seller_id",
        how="left"
    )

    print("Merged dataset shape:", df.shape)
    return df
