# Capstone Project: Customer Insights Dashboard (Weeks 9–11)

## Scenario
You are working as a junior business analyst in a digital retail company.  
Your manager has asked you to develop a **Python-based dashboard** that helps the team visualise and understand **customer purchase behaviour**.  

The dashboard should:
- Load and process **customer, product, and purchase data**  
- Compute **key business metrics** (spend, churn, popular products)  
- Display results using **visualisations**  
- Handle errors gracefully  
- Include **unit tests** for the analytical functions  
- Reflect on the role of **AI coding assistants** in your development process  


## Core Requirements

### Week 9 – Testing and AI Coding
#### Unit Testing
- Write unit tests (with `pytest`) for at least **3 core analytics functions**:
  - Total spend per customer
  - Churn rate
  - Most popular product
- Demonstrate running tests locally and interpreting results.

#### AI Assistant Reflection
- Experiment with an AI coding assistant (e.g., Copilot, ChatGPT).  
- Document:
  - Which part of the code you asked the AI to help with.  
  - How you reviewed/refined the AI’s suggestions.  
  - Risks/ethical considerations.  


### Week 10 – Dashboard Development
#### Core Features
- Build a **dashboard script** (`src/dashboard.py`) that:
  - Loads data from CSV/JSON  
  - Computes **summary metrics**  
  - Displays **visualisations** (Matplotlib):
    - Bar chart of top products  
    - Churn rate visualisation (pie or bar)  
    - Spend by customer (bar chart)  
- Include a **simple text menu** so the user can choose which chart to view.  
- Save **dashboard outputs** (charts as PNG and summary JSON) to the `outputs/` folder.  


### Week 11 – Wrap-Up and Reflection
#### Final Deliverables
- A **Python dashboard** (structured code + charts).  
- A **tests/** folder with pytest test cases.  
- A **README.md** that:
  - Explains how to run the dashboard.  
  - Optionally includes screenshots of charts.  
  - Reflects on your learning:
    - Use of Python (lists, loops, dictionaries, classes, files, visualisation).  
    - Role of AI assistants in your coding.  
    - Improvements you’d make with more time.  


## Stretch Goals (Optional)
- Add an **interactive dashboard** (e.g., Streamlit or Dash).  
- Allow filtering by **date range** or **customer segment**.  
- Save charts automatically to `.png` files.  
- Export metrics to **Excel/CSV** for reporting.  


##  How to Run

```bash
# (Optional) create and activate a virtual environment
pip install -r requirements.txt

# Run unit tests
pytest -q

# Run the dashboard (text menu)
python -m src.dashboard
```
