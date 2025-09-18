# Capstone Project: Customer Insights Dashboard (Weeks 9–11)

##  Scenario
You are working as a junior business analyst in a digital retail company.  
Your manager has asked you to create a simple **Python-based analytics application** that helps the team understand **customer purchase behaviour**.  

The application should:
- Load customer data  
- Analyse metrics  
- Run automated tests  
- Handle errors gracefully  
- Persist results  

You should also include **unit tests** for key functions and reflect on the role of **AI coding assistants** in your development process.


## Core Requirements

### Week 9 – Testing and AI Coding
#### Unit Testing
- Write **unit tests** (with `pytest`) for at least **3 core functions**:
  - Calculate **total spend per customer**
  - Compute **churn rate**
  - Find the **most popular product**
- Use different assert methods (`assert`, `assertEqual`, `assertIn`, etc.).
- Demonstrate running tests locally and interpreting results.

#### AI Assistant Reflection
- Experiment with an AI coding assistant (e.g., GitHub Copilot, ChatGPT).  
- Document in comments or a short markdown note:
  - Which part of the code you asked the AI to help with.
  - How you reviewed/edited/refined the AI’s suggestions.
  - Any risks or ethical considerations.


### Week 10 – Application Development
#### Core Features
- Create a **User class** with attributes (`username`, `high_score`, `purchases`) and methods to update purchases and calculate totals.
- Create a **Product/Question class**:
  - **Analytics theme:** store `product_id`, `category`, and `price`.  
  - **Quiz theme:** store `question`, `options`, and `correct_answer`.  
- Load data from a **CSV or JSON file** (e.g., purchase history or quiz bank).
- Allow the user to:
  - View summary statistics (total sales, most popular product, average spend).
  - Save high scores or purchase summaries to a JSON file.
- Handle file errors gracefully (`FileNotFoundError`, `JSONDecodeError`).


### Week 11 – Wrap-Up and Reflection
#### Final Deliverables
- A **Python application** (structured with functions and classes).
- A **tests/** folder containing your pytest test cases.
- A **README.md** file that:
  - Explains how to run the program.
  - Summarises which features are included.
  - Reflects on your learning journey:
    - How you used Python concepts (lists, loops, dictionaries, classes, files).
    - How AI tools supported your coding.
    - What you would improve with more time.


##  Extra activities
- Add **data visualisation** with Matplotlib (e.g., bar chart of top 5 products).
- Include **input prompts** for interactive use.
- Store data in multiple formats (CSV + JSON).
- Create additional automated tests for **edge cases**.

---
