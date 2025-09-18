from pathlib import Path
from src.io_utils import load_customers_json, load_products_csv, load_purchases_csv, save_summary_json
from src.analytics import total_spend_per_user, most_popular_product, churn_rate

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def run():
    customers = load_customers_json(str(DATA_DIR / "customers.json"))
    products = load_products_csv(str(DATA_DIR / "products.csv"))
    purchases = load_purchases_csv(str(DATA_DIR / "purchases.csv"))

    price_map = {pid: info["price"] for pid, info in products.items()}
    spend_by_user = total_spend_per_user(purchases, price_map)
    popular_pid, popular_qty = most_popular_product(purchases)
    churn = churn_rate(customers)

    print("=== Customer Insights Summary ===")
    print("Total spend by user (£):", spend_by_user)
    print(f"Most popular product: {popular_pid} (qty {popular_qty})")
    print(f"Churn rate: {churn}%")

    summary = {
        "spend_by_user": spend_by_user,
        "most_popular": {"product_id": popular_pid, "qty": popular_qty},
        "churn_rate_pct": churn
    }
    out_path = DATA_DIR / "summary.json"
    if save_summary_json(str(out_path), summary):
        print(f"Saved summary to {out_path}")

if __name__ == "__main__":
    run()
