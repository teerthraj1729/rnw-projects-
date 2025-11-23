Retail Sales Data Analyzer

A Python-based toolkit for analyzing retail sales data using NumPy, Pandas, Matplotlib, and Seaborn, implemented with clean Object-Oriented Programming (OOP) principles.



Develop a Retail Sales Analyzer that helps users:

* Load and clean retail sales datasets
* Generate key business metrics
* Filter data efficiently
* Visualize sales trends and correlations
* Derive insights like top-selling product categories, total revenue, and more



Features & Requirements

Class and Object Structure

 A single class RetailAnalyzer encapsulates:

  * Data loading
  * Cleaning & normalization
  * Sales computations
  * Filtering
  * Summary & visualization

 Data Loading & Cleaning

* Load CSV dataset with validation
* Normalize column names:

  * Lowercase
  * Underscore-based
  * Removes special characters
* Automatically fills missing values
* Automatically computes *total_sales* if price × quantity exists
* Detects & corrects:

  * price column
  * quantity column

Metrics Calculation

Calculates:

  * *Total sales*
  * *Average sales*
  * *Most sold product/category*
 Automatically identifies the correct columns using smart column search logic

 Data Filtering

* Filter rows based on:

  * Exact match
  * Partial match (%value%)
* Allows filtering on any column
* Shows first 10 matching rows
* Handles invalid or missing column names safely

---

data Summary (Pandas)

* Displays complete statistical summary using describe()
* Includes categorical and numerical columns

---

Data Visualization (Matplotlib & Seaborn)

User can choose between:

 1. *Bar Chart*

Total sales by category/product

 2. *Line Chart*

Sales trend over time

3. *Correlation Heatmap*

Shows relationship between sales, price, quantity, etc.



Object-Oriented Approach

* Class-based structure
* Private helper methods:

  * _normalize_columns()
  * _find_col()
* Clean separation of responsibilities
* Menu-driven interface in __main__
* Uses exception handling for safety and user-friendly errors

---

User Interface

A simple *menu-driven application*:


1. Load Dataset
2. Calculate Metrics
3. Filter Data
4. Display Summary
5. Visualize Data
6. Exit
