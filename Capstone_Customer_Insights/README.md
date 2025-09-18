# Capstone Project — Customer Insights Dashboard (Weeks 9–11)

**Audience:** MSc Business Analytics  
**Goal:** Build a small Python analytics app that loads purchase data, computes metrics, 
saves results, and includes automated tests. Reflect on responsible use of AI coding tools.

## Project Structure
```
Capstone_Customer_Insights/
├─ data/
│  ├─ customers.json
│  ├─ products.csv
│  └─ purchases.csv
├─ src/
│  ├─ models.py
│  ├─ analytics.py
│  ├─ io_utils.py
│  └─ main.py
├─ tests/
│  └─ test_analytics.py
└─ README.md
```
## Quick Start
1. (Optional) Create a virtual environment (recommended).
2. Install dev dependency for testing:
   ```bash
   pip install pytest
   ```
3. Run the app:
   ```bash
   python -m src.main
   ```
4. Run the tests:
   ```bash
   pytest -q
   ```

## Deliverables
- Working Python app (menu-based or simple script) that prints key metrics.
- Automated tests in `tests/` (pytest).
- A short reflection in `AI_NOTES.md` on how you used AI coding tools.


## New files added
- `requirements.txt` — install with `pip install -r requirements.txt`
- `src/visualize.py` — Matplotlib stubs:
  - `plot_top_products_from_purchases(purchases_path, top_n=3)`
  - `plot_spend_by_user_from_summary(summary_path)`
Run `python -m src.visualize` after generating `data/summary.json` (via `python -m src.main`).
