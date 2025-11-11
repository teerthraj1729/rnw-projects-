import numpy as np
from typing import Optional, Union, Tuple

class DataAnalytics:

    def __init__(self):
        self.array: Optional[np.ndarray] = None
        self.second_array: Optional[np.ndarray] = None

    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = input("Enter your choice: ").strip()

        try:
            match choice:
                case "1":
                    elements = input("Enter elements separated by space: ").strip()
                    self.array = np.array([float(x) for x in elements.split()])
                    print(f"\nArray created successfully:\n{self.array}")

                case "2":
                    rows = int(input("Enter the number of rows: "))
                    cols = int(input("Enter the number of columns: "))
                    total = rows * cols
                    elements = input(f"Enter {total} elements for the array separated by space: ").strip()
                    values = [float(x) for x in elements.split()]
                    if len(values) != total:
                        print(f"Error: Expected {total} elements, got {len(values)}")
                        return
                    self.array = np.array(values).reshape(rows, cols)
                    print(f"\nArray created successfully:\n{self.array}")

                case "3":
                    depth = int(input("Enter the depth: "))
                    rows = int(input("Enter the number of rows: "))
                    cols = int(input("Enter the number of columns: "))
                    total = depth * rows * cols
                    elements = input(f"Enter {total} elements for the array separated by space: ").strip()
                    values = [float(x) for x in elements.split()]
                    if len(values) != total:
                        print(f"Error: Expected {total} elements, got {len(values)}")
                        return
                    self.array = np.array(values).reshape(depth, rows, cols)
                    print(f"\nArray created successfully:\n{self.array}")

                case _:
                    print("Invalid choice!")
        except Exception as e:
            print(f"Error creating array: {e}")

    def indexing_slicing_menu(self):
        if self.array is None:
            print("No array created yet! Please create an array first.")
            return

        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = input("Enter your choice: ").strip()

            match choice:
                case "1":
                    self._indexing_operation()
                case "2":
                    self._slicing_operation()
                case "3":
                    break
                case _:
                    print("Invalid choice!")

    def _indexing_operation(self):
        print(f"\nCurrent Array:\n{self.array}")
        try:
            if self.array.ndim == 1:
                index = int(input("Enter the index: "))
                print(f"Element at index {index}: {self.array[index]}")
            elif self.array.ndim == 2:
                row = int(input("Enter the row index: "))
                col = int(input("Enter the column index: "))
                print(f"Element at [{row}, {col}]: {self.array[row, col]}")
            elif self.array.ndim == 3:
                depth = int(input("Enter the depth index: "))
                row = int(input("Enter the row index: "))
                col = int(input("Enter the column index: "))
                print(f"Element at [{depth}, {row}, {col}]: {self.array[depth, row, col]}")
        except Exception as e:
            print(f"Error: {e}")

    def _slicing_operation(self):
        print(f"\nCurrent Array:\n{self.array}")
        try:
            if self.array.ndim == 1:
                start = input("Enter start index (or press Enter for default): ").strip()
                end = input("Enter end index (or press Enter for default): ").strip()
                start = int(start) if start else None
                end = int(end) if end else None
                sliced = self.array[start:end]
                print(f"\nSliced Array:\n{sliced}")

            elif self.array.ndim >= 2:
                row_range = input("Enter the row range (start:end): ").strip()
                col_range = input("Enter the column range (start:end): ").strip()

                if ':' in row_range:
                    row_parts = row_range.split(':')
                    row_start = int(row_parts[0]) if row_parts[0] else None
                    row_end = int(row_parts[1]) if row_parts[1] else None
                else:
                    row_start = row_end = int(row_range) if row_range else None

                if ':' in col_range:
                    col_parts = col_range.split(':')
                    col_start = int(col_parts[0]) if col_parts[0] else None
                    col_end = int(col_parts[1]) if col_parts[1] else None
                else:
                    col_start = col_end = int(col_range) if col_range else None

                sliced = self.array[row_start:row_end, col_start:col_end]
                print(f"\nSliced Array:\n{sliced}")
        except Exception as e:
            print(f"Error: {e}")

    def combine_split_menu(self):
        if self.array is None:
            print("No array created yet! Please create an array first.")
            return

        while True:
            print("\nChoose an option:")
            print("1. Combine Arrays")
            print("2. Split Array")
            print("3. Go Back")

            choice = input("Enter your choice: ").strip()

            match choice:
                case "1":
                    self._combine_arrays()
                case "2":
                    self._split_array()
                case "3":
                    break
                case _:
                    print("Invalid choice!")

    def _combine_arrays(self):
        print(f"\nOriginal Array:\n{self.array}")
        try:
            total_elements = self.array.size
            elements = input(f"Enter the elements of another array to combine ({total_elements} elements separated by space): ").strip()
            values = [float(x) for x in elements.split()]

            if len(values) != total_elements:
                print(f"Error: Expected {total_elements} elements, got {len(values)}")
                return

            second_arr = np.array(values).reshape(self.array.shape)
            print(f"\nSecond Array:\n{second_arr}")

            combined = np.vstack([self.array, second_arr])
            print(f"\nCombined Array (Vertical Stack):\n{combined}")

        except Exception as e:
            print(f"Error: {e}")

    def _split_array(self):
        print(f"\nCurrent Array:\n{self.array}")
        try:
            num_splits = int(input("Enter the number of parts to split: "))

            if self.array.ndim == 1:
                splits = np.array_split(self.array, num_splits)
            else:
                axis = int(input("Enter the axis to split (0 for rows, 1 for columns): "))
                splits = np.array_split(self.array, num_splits, axis=axis)

            print(f"\nSplit Arrays:")
            for i, split in enumerate(splits):
                print(f"Part {i+1}:\n{split}\n")
        except Exception as e:
            print(f"Error: {e}")

    def mathematical_operations_menu(self):
        if self.array is None:
            print("No array created yet! Please create an array first.")
            return

        while True:
            print("\nChoose a mathematical operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Go Back")

            choice = input("Enter your choice: ").strip()

            match choice:
                case "1" | "2" | "3" | "4":
                    self._element_wise_operation(choice)
                case "5":
                    break
                case _:
                    print("Invalid choice!")

    def _element_wise_operation(self, operation: str):
        print(f"\nOriginal Array:\n{self.array}")
        try:
            total_elements = self.array.size
            elements = input(f"Enter the same-size array elements ({total_elements} elements separated by space): ").strip()
            values = [float(x) for x in elements.split()]

            if len(values) != total_elements:
                print(f"Error: Expected {total_elements} elements, got {len(values)}")
                return

            second_arr = np.array(values).reshape(self.array.shape)
            print(f"\nSecond Array:\n{second_arr}")

            match operation:
                case "1":
                    result = self.array + second_arr
                    print(f"\nResult of Addition:\n{result}")
                case "2":
                    result = self.array - second_arr
                    print(f"\nResult of Subtraction:\n{result}")
                case "3":
                    result = self.array * second_arr
                    print(f"\nResult of Multiplication:\n{result}")
                case "4":
                    result = self.array / second_arr
                    print(f"\nResult of Division:\n{result}")
        except Exception as e:
            print(f"Error: {e}")

    def search_sort_filter_menu(self):
        if self.array is None:
            print("No array created yet! Please create an array first.")
            return

        while True:
            print("\nChoose an option:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")
            print("4. Go Back")

            choice = input("Enter your choice: ").strip()

            match choice:
                case "1":
                    self._search_value()
                case "2":
                    self._sort_array()
                case "3":
                    self._filter_array()
                case "4":
                    break
                case _:
                    print("Invalid choice!")

    def _search_value(self):
        print(f"\nOriginal Array:\n{self.array}")
        try:
            value = float(input("Enter the value to search: "))
            indices = np.where(self.array == value)

            if len(indices[0]) > 0:
                print(f"\nValue {value} found at indices: {list(zip(*indices))}")
            else:
                print(f"\nValue {value} not found in the array.")
        except Exception as e:
            print(f"Error: {e}")

    def _sort_array(self):
        print(f"\nOriginal Array:\n{self.array}")

        print("\nChoose sorting order:")
        print("1. Ascending")
        print("2. Descending")

        choice = input("Enter your choice: ").strip()

        try:
            if self.array.ndim == 1:
                match choice:
                    case "1":
                        sorted_arr = np.sort(self.array)
                        print(f"\nSorted Array (Ascending):\n{sorted_arr}")
                    case "2":
                        sorted_arr = np.sort(self.array)[::-1]
                        print(f"\nSorted Array (Descending):\n{sorted_arr}")
                    case _:
                        print("Invalid choice!")
            else:
                axis = input("Enter axis to sort (0 for rows, 1 for columns): ").strip()
                axis = int(axis) if axis else None

                match choice:
                    case "1":
                        sorted_arr = np.sort(self.array, axis=axis)
                        print(f"\nSorted Array (Ascending):\n{sorted_arr}")
                    case "2":
                        sorted_arr = np.sort(self.array, axis=axis)
                        if axis == 0:
                            sorted_arr = sorted_arr[::-1]
                        elif axis == 1:
                            sorted_arr = sorted_arr[:, ::-1]
                        print(f"\nSorted Array (Descending):\n{sorted_arr}")

                if self.array.ndim == 2 and axis is not None:
                    print("(Sorting applied row-wise.)" if axis == 0 else "(Sorting applied column-wise.)" if axis == 1 else "")
        except Exception as e:
            print(f"Error: {e}")

    def _filter_array(self):
        print(f"\nOriginal Array:\n{self.array}")

        print("\nChoose a filter condition:")
        print("1. Greater than a value")
        print("2. Less than a value")
        print("3. Equal to a value")
        print("4. Between two values")

        choice = input("Enter your choice: ").strip()

        try:
            match choice:
                case "1":
                    value = float(input("Enter the value: "))
                    filtered = self.array[self.array > value]
                    print(f"\nFiltered Array (> {value}):\n{filtered}")
                case "2":
                    value = float(input("Enter the value: "))
                    filtered = self.array[self.array < value]
                    print(f"\nFiltered Array (< {value}):\n{filtered}")
                case "3":
                    value = float(input("Enter the value: "))
                    filtered = self.array[self.array == value]
                    print(f"\nFiltered Array (= {value}):\n{filtered}")
                case "4":
                    lower = float(input("Enter the lower bound: "))
                    upper = float(input("Enter the upper bound: "))
                    filtered = self.array[(self.array >= lower) & (self.array <= upper)]
                    print(f"\nFiltered Array (between {lower} and {upper}):\n{filtered}")
                case _:
                    print("Invalid choice!")
        except Exception as e:
            print(f"Error: {e}")

    def aggregates_statistics_menu(self):
        if self.array is None:
            print("No array created yet! Please create an array first.")
            return

        while True:
            print("\nChoose an aggregate/statistical operation:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Go Back")

            choice = input("Enter your choice: ").strip()

            try:
                print(f"\nOriginal Array:\n{self.array}")

                match choice:
                    case "1":
                        result = np.sum(self.array)
                        print(f"\nSum of Array: {result}")
                    case "2":
                        result = np.mean(self.array)
                        print(f"\nMean of Array: {result}")
                    case "3":
                        result = np.median(self.array)
                        print(f"\nMedian of Array: {result}")
                    case "4":
                        result = np.std(self.array)
                        print(f"\nStandard Deviation of Array: {result}")
                    case "5":
                        result = np.var(self.array)
                        print(f"\nVariance of Array: {result}")
                    case "6":
                        break
                    case _:
                        print("Invalid choice!")
            except Exception as e:
                print(f"Error: {e}")

    def run(self):
        print("Welcome to the NumPy Analyzer!")
        print("=" * 40)

        while True:
            print("\nChoose an option:")
            print("1. Create a Numpy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            match choice:
                case "1":
                    self.create_array()
                case "2":
                    self.mathematical_operations_menu()
                case "3":
                    self.combine_split_menu()
                case "4":
                    self.search_sort_filter_menu()
                case "5":
                    self.aggregates_statistics_menu()
                case "6":
                    print("\nThank you for using the NumPy Analyzer! Goodbye!")
                    break
                case _:
                    print("Invalid choice! Please try again.")


if __name__ == "__main__":
    analyzer = DataAnalytics()
    analyzer.run()
