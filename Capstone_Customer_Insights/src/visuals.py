import matplotlib.pyplot as plt

def plot_top_products(product_counts, top_n=5):
    """Plot a bar chart of the top N products by quantity."""
    top_items = sorted(product_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    labels, values = zip(*top_items)
    plt.bar(labels, values, color="skyblue")
    plt.title(f"Top {top_n} Products by Quantity")
    plt.xlabel("Product ID")
    plt.ylabel("Quantity")
    plt.show()
