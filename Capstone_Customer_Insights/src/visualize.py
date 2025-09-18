"""Visualization stubs for the Capstone project.

Usage
-----
- Ensure you have run `python -m src.main` at least once so `data/summary.json` exists.
- Then run this file directly or import its functions from another script.

Rules
-----
- Use matplotlib (no seaborn).
- One chart per figure.
- Do not set specific colors unless asked.
"""
import json
from pathlib import Path
import matplotlib.pyplot as plt

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def plot_top_products_from_purchases(purchases_path: Path, top_n: int = 3) -> None:
    """Compute top-N products by quantity from purchases.csv and plot a bar chart."""
    import csv
    counts = {}
    with open(purchases_path, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            pid = row["product_id"]
            qty = int(row["quantity"])
            counts[pid] = counts.get(pid, 0) + qty
    # Sort and take top-N
    items = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    labels = [k for k, _ in items]
    values = [v for _, v in items]

    plt.figure()
    plt.bar(labels, values)
    plt.title(f"Top {top_n} Products by Quantity")
    plt.xlabel("Product ID")
    plt.ylabel("Total Quantity")
    for i, v in enumerate(values):
        plt.text(i, v + 0.2, str(v), ha="center")
    plt.tight_layout()
    plt.show()

def plot_spend_by_user_from_summary(summary_path: Path) -> None:
    """Plot spend by user (£) from data/summary.json produced by src.main."""
    with open(summary_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    spend = data.get("spend_by_user", {})
    users = list(spend.keys())
    totals = [spend[u] for u in users]

    plt.figure()
    plt.bar(users, totals)
    plt.title("Total Spend by User (£)")
    plt.xlabel("User")
    plt.ylabel("Spend (£)")
    for i, v in enumerate(totals):
        plt.text(i, v + 0.2, f"{v:.2f}", ha="center")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example manual run:
    #   python -m src.visualize
    purchases_csv = DATA_DIR / "purchases.csv"
    summary_json = DATA_DIR / "summary.json"
    if purchases_csv.exists():
        plot_top_products_from_purchases(purchases_csv, top_n=3)
    if summary_json.exists():
        plot_spend_by_user_from_summary(summary_json)
    else:
        print("Run `python -m src.main` first to generate data/summary.json.")
