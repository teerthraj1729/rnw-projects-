import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class RetailAnalyzer:
    def __init__(self):
        self.data = None

    
    def _normalize_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        
        cols = (
            df.columns
            .astype(str)
            .str.strip()
            .str.lower()
            .str.replace(' ', '_', regex=False)
            .str.replace(r'[^\w_]', '', regex=True)
        )
        df.columns = cols
        return df

    def _find_col(self, candidates):
        
        for c in candidates:
            if c in self.data.columns:
                return c
        return None

    
    def load_data(self, file_path: str = None):
        
        if file_path is None:
            file_path = input("Enter path of retail_sales.csv: ").strip()

        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError("File not found!")

            if not file_path.lower().endswith(".csv"):
                raise ValueError("Invalid File Format! Please upload a CSV file.")

            self.data = pd.read_csv(file_path)

            
            self.data = self._normalize_columns(self.data)

            
            self.data.fillna(0, inplace=True)

            
            price_col = self._find_col(['price', 'unit_price', 'cost'])
            qty_col = self._find_col(['quantity_sold', 'quantity', 'qty', 'sold'])
            if 'total_sales' not in self.data.columns and price_col and qty_col:
                
                self.data[price_col] = pd.to_numeric(self.data[price_col], errors='coerce').fillna(0)
                self.data[qty_col] = pd.to_numeric(self.data[qty_col], errors='coerce').fillna(0)
                self.data['total_sales'] = self.data[price_col] * self.data[qty_col]

            print("Dataset loaded successfully!")
            print("Normalized columns:", self.data.columns.tolist())
            print(self.data.head())

        except FileNotFoundError as e:
            print(f"ERROR: {e}")

        except ValueError as e:
            print(f"ERROR: {e}")

        except Exception as e:
            print(f"Unexpected Error: {e}")

    
    def calculate_metrics(self):
        try:
            if self.data is None:
                raise Exception("Dataset not loaded!")

            
            total_col = self._find_col(['total_sales', 'total', 'sales'])
            if total_col is None:
                print("Required 'Total Sales' column missing and could not be derived.")
                print("Available numeric columns:", self.data.select_dtypes(include='number').columns.tolist())
                return

            
            product_col = self._find_col(['product_category', 'category', 'product', 'product_name'])

            total_sales = pd.to_numeric(self.data[total_col], errors='coerce').fillna(0).sum()
            avg_sales = pd.to_numeric(self.data[total_col], errors='coerce').fillna(0).mean()

            if product_col and self._find_col(['quantity_sold', 'quantity', 'qty', 'sold']):
                qty_col = self._find_col(['quantity_sold', 'quantity', 'qty', 'sold'])
                
                popular = (
                    self.data
                    .groupby(product_col)[qty_col]
                    .sum()
                    .idxmax()
                )
            else:
                popular = "N/A (product or quantity column missing)"

            print("Sales Metrics")
            print(f"Total Sales ({total_col}): ₹{total_sales}")
            print(f"Average Sales ({total_col}): ₹{avg_sales:.2f}")
            print(f"Most Sold Product/Category: {popular}")

        except KeyError:
            print("Required columns missing!")

        except Exception as e:
            print(f"ERROR: {e}")

    
    def filter_data(self):
        try:
            if self.data is None:
                raise Exception("Dataset not loaded!")

            print("Available columns:", self.data.columns.tolist())
            column_input = input("Enter column to filter by (type exact or close name): ").strip().lower()
            
            column = (
                column_input
                .strip()
                .lower()
                .replace(' ', '_')
            )

            
            if column in self.data.columns:
                col = column
            else:
                
                matches = [c for c in self.data.columns if column in c]
                col = matches[0] if matches else None

            if col is None:
                raise KeyError(f"Column does not exist! Tried to match '{column_input}'")

            value = input("Enter value to match (exact match). For partial match, enter %value%: ").strip()

            
            if value.startswith('%') and value.endswith('%'):
                val = value.strip('%')
                filtered = self.data[self.data[col].astype(str).str.contains(val, na=False, case=False)]
            else:
                
                filtered = self.data[self.data[col].astype(str) == value]

            print("Filtered Data (first 10 rows):")
            if filtered.empty:
                print("No rows match the filter.")
            else:
                print(filtered.head(10))

        except KeyError as e:
            print(f"ERROR: {e}")

        except Exception as e:
            print(f"ERROR: {e}")

    
    def display_summary(self):
        try:
            if self.data is None:
                raise Exception("Dataset not loaded!")

            print("Data Summary:")
            print(self.data.describe(include="all"))

        except Exception as e:
            print(f"ERROR: {e}")

    
    def visualize(self):
        try:
            if self.data is None:
                raise Exception("Dataset not loaded!")

            print("\nChoose Visualization Type:")
            print("1. Bar Chart (Total Sales by Category/Product)")
            print("2. Line Chart (Total Sales by Date)")
            print("3. Heatmap (Correlation between numeric columns)")

            choice = input("Enter choice (1/2/3): ").strip()

            if choice == "1":
                
                group_col = self._find_col(['product_category', 'category', 'product', 'product_name'])
                total_col = self._find_col(['total_sales', 'total', 'sales'])
                if group_col is None:
                    print(" No category/product column found for bar chart. Available columns:", self.data.columns.tolist())
                    return
                if total_col is None:
                    print("No 'total_sales' column found for bar chart. Available numeric columns:", self.data.select_dtypes(include='number').columns.tolist())
                    return

                category_sales = (
                    self.data
                    .groupby(group_col)[total_col]
                    .sum()
                    .sort_values(ascending=False)
                )
                category_sales.plot(kind="bar")
                plt.title("Total Sales by " + group_col)
                plt.ylabel(total_col)
                plt.xlabel(group_col)
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            elif choice == "2":
               
                date_col = self._find_col(['date', 'order_date', 'sale_date'])
                total_col = self._find_col(['total_sales', 'total', 'sales'])
                if date_col is None:
                    print("'Date' column not found! Available columns:", self.data.columns.tolist())
                    return
                if total_col is None:
                    print("'Total Sales' column not found! Available numeric columns:", self.data.select_dtypes(include='number').columns.tolist())
                    return

                
                self.data[date_col] = pd.to_datetime(self.data[date_col], errors='coerce')
                date_sales = (
                    self.data
                    .dropna(subset=[date_col])
                    .groupby(date_col)[total_col]
                    .sum()
                    .sort_index()
                )
                if date_sales.empty:
                    print("No valid date rows to plot.")
                    return

                date_sales.plot(kind="line", marker='o')
                plt.title("Total Sales Over Time")
                plt.ylabel(total_col)
                plt.xlabel(date_col)
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            elif choice == "3":
                
                numeric_data = self.data.select_dtypes(include=["number"])
                if numeric_data.empty:
                    print("No numeric columns available for heatmap.")
                    return
                plt.figure(figsize=(8, 6))
                sns.heatmap(numeric_data.corr(), annot=True)
                plt.title("Correlation Heatmap")
                plt.tight_layout()
                plt.show()

            else:
                print("Invalid choice!")

        except Exception as e:
            print(f"ERROR: {e}")



if __name__ == "__main__":
    analyzer = RetailAnalyzer()

    while True:
        print()
        print("Retail Sales Data Analyzer")
        print("1. Load Dataset")
        print("2. Calculate metrics")
        print("3. Filter data")
        print("4. Display summary")
        print("5. Visualize Data")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        match choice:
            case "1":
                analyzer.load_data()  
            case "2":
                analyzer.calculate_metrics()
            case "3":
                analyzer.filter_data()
            case "4":
                analyzer.display_summary()
            case "5":
                analyzer.visualize()
            case "6":
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice")
