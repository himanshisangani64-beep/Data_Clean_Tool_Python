# 🧹 Automated Data Cleaning & EDA Tool

### *Python-Based Data Cleaning, Data Quality Analysis & Dataset Preprocessing Utility*

> *"Clean data is the foundation of reliable analysis and machine learning."*

---

## 📋 Table of Contents

* [📌 Overview](#-overview)
* [🎯 Problem Statement](#-problem-statement)
* [✨ Key Features](#-key-features)
* [🏗️ Project Structure](#️-project-structure)
* [🗃️ Tool Architecture](#️-tool-architecture)
* [🔄 Project Workflow](#-project-workflow)
* [📥 Part A — Data Loading & Inspection](#-part-a--data-loading--inspection)
* [🧹 Part B — Data Cleaning](#-part-b--data-cleaning)
* [📊 Part C — Data Quality Analysis](#-part-c--data-quality-analysis)
* [💾 Part D — Clean Data Export](#-part-d--clean-data-export)
* [🛠️ Tech Stack](#️-tech-stack)
* [📚 Python & Data Concepts Practiced](#-python--data-concepts-practiced)
* [📈 Results & Project Output](#-results--project-output)
* [🔍 Data Quality & Design Notes](#-data-quality--design-notes)
* [🏆 Advantages](#-advantages)
* [🎯 Why I Built This Project](#-why-i-built-this-project)
* [🔮 Future Improvements](#-future-improvements)
* [▶️ How to Run](#️-how-to-run)
* [👤 Author](#-author)
* [🙏 Acknowledgements](#-acknowledgements)

---

# 📌 Overview

The **Automated Data Cleaning & EDA Tool** is a Python-based utility designed to perform common **data cleaning, data inspection and data-quality analysis** tasks using **Pandas and NumPy**.

In practical Data Analysis and Machine Learning projects, raw datasets may contain:

* Missing values
* Duplicate records
* Incorrect data types
* Invalid numeric values
* Incorrect date formats
* Unclean categorical values
* Unnecessary columns
* Different file formats

Before performing Exploratory Data Analysis or using data for Machine Learning, these issues often need to be identified and handled.

This project provides reusable Python functions that help perform these common operations in a structured workflow.

The tool currently supports:

* CSV files
* Excel files
* JSON files

It can:

* Load datasets
* Inspect dataset structure
* Display data types
* Detect missing values
* Handle numeric missing values
* Handle categorical missing values
* Detect duplicate records
* Remove duplicate records
* Convert data types
* Remove unnecessary columns
* Inspect column values
* Generate a basic data-quality report
* Save cleaned data in CSV, Excel and JSON formats

The project was developed as a practical Python project to strengthen my understanding of **Python, Pandas, NumPy, Data Cleaning, Data Quality and Data Preprocessing**.

---

# 🎯 Problem Statement

> **Objective:** Build a reusable Python-based data-cleaning utility that can load datasets, identify common data-quality problems, perform basic cleaning operations and save the cleaned dataset in multiple file formats.

Raw datasets are often not immediately suitable for analysis or Machine Learning.

A typical problem can be represented as:

```text
Raw Dataset
     │
     ▼
Missing Values
     │
     ▼
Duplicate Records
     │
     ▼
Incorrect Data Types
     │
     ▼
Unclean / Invalid Values
     │
     ▼
Unnecessary Columns
     │
     ▼
Data Quality Problems
     │
     ▼
Clean Dataset
     │
     ├──────────────► Data Analysis
     │
     └──────────────► Machine Learning
```

Manually repeating these operations for every dataset can result in repetitive code and inconsistent workflows.

Therefore, this project was created to combine commonly used cleaning operations into reusable Python functions.

---

## 📊 Major Functional Areas

| **Feature**               | **Type**     | **Description**                                |
| ------------------------- | ------------ | ---------------------------------------------- |
| Data Loading              | Input        | Loads CSV, XLSX and JSON datasets              |
| Dataset Summary           | Inspection   | Displays rows, columns and dataset structure   |
| Data Information          | Inspection   | Displays DataFrame information and data types  |
| Statistical Summary       | Analysis     | Generates descriptive statistics               |
| Numeric Conversion        | Cleaning     | Converts selected columns into numeric format  |
| Date Conversion           | Cleaning     | Converts selected columns into datetime format |
| Category Conversion       | Cleaning     | Converts columns into categorical data type    |
| Missing Value Detection   | Data Quality | Identifies missing values column-wise          |
| Numeric Missing Handling  | Cleaning     | Fills numeric missing values using mean        |
| Category Missing Handling | Cleaning     | Fills categorical missing values               |
| Missing Row Removal       | Cleaning     | Removes rows containing missing values         |
| Duplicate Detection       | Data Quality | Counts duplicate records                       |
| Column Duplicate Check    | Data Quality | Checks duplicate values in a specific column   |
| Duplicate Removal         | Cleaning     | Removes duplicate rows                         |
| Column Removal            | Cleaning     | Removes selected unnecessary columns           |
| Value Inspection          | Analysis     | Displays frequency of values                   |
| Data Quality Report       | Reporting    | Generates column-level quality information     |
| Clean Data Export         | Output       | Saves cleaned data as CSV, XLSX or JSON        |

The overall goal is to demonstrate how Python can be used to create a **reusable data-preprocessing utility** rather than performing every operation separately.

---

# ✨ Key Features

| **Feature**                      | **Description**                                   |
| -------------------------------- | ------------------------------------------------- |
| 🐍 **Python Utility**            | Built using reusable Python functions             |
| 🐼 **Pandas**                    | Used for DataFrame operations and data cleaning   |
| 🔢 **NumPy**                     | Used for numerical and categorical value handling |
| 📂 **CSV Support**               | Loads and saves CSV datasets                      |
| 📊 **Excel Support**             | Loads and saves XLSX datasets                     |
| 🗂️ **JSON Support**             | Loads and saves JSON datasets                     |
| 🔍 **Data Inspection**           | Checks dataset structure and information          |
| 🔢 **Data Type Conversion**      | Converts numeric, date and categorical columns    |
| 🕳️ **Missing Value Detection**  | Identifies missing values                         |
| 🧮 **Numeric Imputation**        | Handles numeric missing values using mean         |
| 🏷️ **Categorical Handling**     | Handles missing categorical values                |
| ♻️ **Duplicate Detection**       | Detects duplicate records                         |
| 🗑️ **Duplicate Removal**        | Removes duplicate rows                            |
| 🧹 **Column Removal**            | Removes unnecessary columns                       |
| 📊 **Data Quality Report**       | Generates an automated quality summary            |
| 💾 **Multiple Output Formats**   | Saves cleaned data in CSV, XLSX and JSON          |
| 📈 **EDA Preparation**           | Prepares data for further analysis                |
| 🤖 **ML Preparation Foundation** | Provides basic preprocessing before ML workflows  |

---

# 🏗️ Project Structure

```text
📦 Automated-Data-Cleaning-EDA-Tool/
│
├── 📄 Data_Source.py
│   ├── Data_Load()
│   ├── Data_save()
│   ├── Show_Data_Type()
│   ├── Change_Data_Type_into_Number()
│   ├── Change_Data_Type_into_Date()
│   ├── Change_Data_Type_into_Category()
│   ├── Missing_Value_Show()
│   ├── Numberic_Value_Handel()
│   ├── Category_Value_Handel()
│   ├── Remove_Missing_Value()
│   ├── Show_Duplicated_Value()
│   ├── Show_Duplicated_Coumn()
│   ├── Remove_Dupicated_Value()
│   ├── Drop_Any_Column()
│   ├── Show_Data_Info()
│   ├── Summery_Data()
│   ├── Dataset_Short_Summery()
│   ├── Data_In_Value()
│   ├── Category_Object_Value()
│   └── Data_Quality_Report()
│
├── 📓 Data_Cleaning_Tool.ipynb
│   └── Complete project workflow and practical execution
│
├── 📂 Massi_Data/
│   ├── Data_Cleaning_Practice_Dataset.csv
│   ├── Data_Cleaning_Practice_Dataset.xlsx
│   └── Data_Cleaning_Practice_Dataset.json
│
├── 📂 Clean_Data/
│   ├── clean_data.csv
│   ├── clean_data.xlsx
│   └── clean_data.json
│
├── 📂 Data_Clean_Report_Image/
│   └── Project output / report screenshots
│
└── 📄 README.md
    └── Project Documentation
```

---

# 🗃️ Tool Architecture

The project is divided into two major Python components:

### `Data_Source.py`

This file contains reusable functions responsible for:

```text
Data Loading
     ↓
Data Inspection
     ↓
Data Type Conversion
     ↓
Missing Value Handling
     ↓
Duplicate Handling
     ↓
Column Operations
     ↓
Value Inspection
     ↓
Data Quality Reporting
     ↓
Data Export
```

### `Data_Cleaning_Tool.ipynb`

The Jupyter Notebook demonstrates how the functions from `Data_Source.py` are used in an actual data-cleaning workflow.

The notebook includes:

* Library import
* Module reload
* Dataset loading
* Dataset inspection
* Data type conversion
* Missing value handling
* Duplicate analysis
* Column removal
* Data quality analysis
* Clean dataset export

---

# 🔄 Project Workflow

```text
                         🚀 Project Start
                               │
                               ▼
                    📂 Select Input Dataset
                               │
                               ▼
                    📥 Load Dataset
                 CSV / XLSX / JSON
                               │
                               ▼
                    🔍 Inspect Dataset
                               │
                ┌──────────────┼──────────────┐
                ▼              ▼              ▼
           Data Types     Missing Values   Duplicates
                │              │              │
                ▼              ▼              ▼
             Convert         Handle          Remove
                │              │              │
                └──────────────┼──────────────┘
                               ▼
                     🧹 Clean Dataset
                               │
                               ▼
                    📊 Quality Analysis
                               │
                               ▼
                     📋 Quality Report
                               │
                               ▼
                    💾 Save Clean Data
                       /      |      \
                     CSV     XLSX    JSON
                               │
                               ▼
                  📈 Further Data Analysis
                               │
                               ▼
                     🤖 ML Preprocessing
```

---

# 📥 Part A — Data Loading & Inspection

## 1. Import Libraries

The project uses:

```python
import pandas as pd
import numpy as np
```

### Pandas

Pandas is used for:

* DataFrame operations
* File loading
* Missing-value analysis
* Data type conversion
* Duplicate handling
* Statistical analysis
* Data export

### NumPy

NumPy is used for numerical operations and categorical missing-value handling.

---

# 📂 2. Data Loading

The `Data_Load()` function supports three file formats.

```python
df = Data_Load(
    "Massi_Data/Data_Cleaning_Practice_Dataset.xlsx"
)
```

Supported formats:

```text
CSV
 │
 ├── .csv
 │
Excel
 │
 ├── .xlsx
 │
JSON
 │
 └── .json
```

Internally, the function uses:

```python
pd.read_csv()
pd.read_excel()
pd.read_json()
```

---

# 📋 3. Dataset Summary

The `Dataset_Short_Summery()` function provides basic dataset information.

```python
Dataset_Short_Summery(df)
```

It displays:

* Dataset shape
* Column names
* Total rows
* Total columns

---

# 🔍 4. Dataset Information

The project uses:

```python
Show_Data_Info(df)
```

This provides information such as:

* Column names
* Non-null values
* Data types
* Memory usage

Internally, it uses:

```python
data.info()
```

---

# 📊 5. Statistical Summary

The project uses:

```python
Summery_Data(df)
```

Internally:

```python
data.describe()
```

This provides descriptive statistics for numerical columns, including:

* Count
* Mean
* Standard deviation
* Minimum
* Quartiles
* Maximum

---

# 🔢 6. Data Type Inspection

The current data types can be viewed using:

```python
Show_Data_Type(df)
```

This helps identify columns that may require conversion before analysis.

---

# 🧹 Part B — Data Cleaning

## 🔢 1. Numeric Data Type Conversion

The tool provides:

```python
Change_Data_Type_into_Number(
    df,
    "Age"
)
```

It uses:

```python
pd.to_numeric(
    data[col],
    errors="coerce"
)
```

Using `errors="coerce"` converts invalid numeric values into missing values (`NaN`), allowing them to be handled during the cleaning stage.

---

# 📅 2. Date Conversion

Date columns can be converted using:

```python
Change_Data_Type_into_Date(
    df,
    "Order_Date"
)
```

Internally:

```python
pd.to_datetime(
    data[col],
    errors="coerce"
)
```

This is useful when dates are stored as strings or inconsistent values.

---

# 🏷️ 3. Category Conversion

Categorical columns can be converted using:

```python
Change_Data_Type_into_Category(
    df,
    "Category"
)
```

This converts the selected column into Pandas:

```text
category
```

data type.

---

# 🕳️ 4. Missing Value Detection

Missing values can be identified using:

```python
Missing_Value_Show(df)
```

The function uses:

```python
data.isnull().sum()
```

Example:

```text
Column          Missing Values
--------------------------------
Age                     2
Unit_Price              4
City                    3
Category                1
```

This provides a column-wise view of missing data.

---

# 🧮 5. Numeric Missing Value Handling

For numerical columns, the current implementation uses the column mean.

```python
Numberic_Value_Handel(
    df,
    "Unit_Price"
)
```

Conceptually:

```text
Missing Numeric Value
          │
          ▼
Calculate Column Mean
          │
          ▼
Fill Missing Value
```

The implementation uses:

```python
data[col].fillna(
    data[col].mean()
)
```

> **Note:** Mean imputation is a simple strategy. The appropriate method depends on the dataset and analysis objective.

---

# 🏷️ 6. Categorical Missing Value Handling

Categorical missing values can be handled using:

```python
Category_Value_Handel(
    df,
    "City"
)
```

The current implementation selects values from existing non-null categories.

Conceptually:

```text
Missing Category
       │
       ▼
Existing Non-Null Categories
       │
       ▼
Select Category
       │
       ▼
Fill Missing Value
```

> **Note:** Random categorical imputation is used here as a simple learning implementation. In a production workflow, strategies such as mode, group-based imputation or domain-specific rules may be more appropriate.

---

# 🗑️ 7. Removing Missing Rows

The project also provides:

```python
Remove_Missing_Value(df)
```

This uses:

```python
data.dropna(
    axis=0,
    inplace=True
)
```

It removes rows containing missing values.

This operation should be used carefully because removing incomplete rows can reduce the available dataset.

---

# ♻️ 8. Duplicate Detection

Total duplicate rows can be identified using:

```python
Show_Duplicated_Value(df)
```

Internally:

```python
data.duplicated().sum()
```

---

# 🔎 9. Column-Level Duplicate Detection

Duplicates in a particular column can be checked using:

```python
Show_Duplicated_Coumn(
    df,
    "Customer_ID"
)
```

This can be useful for identifying repeated values in columns where uniqueness may be expected.

---

# 🗑️ 10. Duplicate Removal

Duplicate rows can be removed using:

```python
Remove_Dupicated_Value(df)
```

Internally:

```python
data.drop_duplicates(
    inplace=True
)
```

Workflow:

```text
Dataset
   ↓
Detect Duplicates
   ↓
Review Duplicate Count
   ↓
Remove Duplicate Rows
   ↓
Continue Cleaning
```

---

# 🧹 11. Remove Unnecessary Columns

Selected columns can be removed using:

```python
l1 = [
    "Total_Sales",
    "Payment_Method"
]

Drop_Any_Column(df, l1)
```

This uses:

```python
data.drop(
    col,
    axis=1,
    inplace=True
)
```

It allows the user to remove columns that are not required for the intended analysis.

---

# 🔍 Part C — Data Quality Analysis

## 📊 1. Value Frequency Analysis

The `Data_In_Value()` function displays the frequency of values in each column.

```python
Data_In_Value(df)
```

It uses:

```python
value_counts()
```

This can help identify:

* Frequent categories
* Rare values
* Unexpected values
* Potential inconsistencies

---

# 🧽 2. Object & Numeric Value Inspection

The project also contains:

```python
Category_Object_Value(df)
```

The current implementation demonstrates:

### Object Columns

String values are displayed after title-case transformation:

```python
data[i].str.title()
```

### Numeric Columns

Absolute values are displayed using:

```python
abs(data[i])
```

This function currently serves as a basic value-cleaning and inspection demonstration and can be expanded with additional cleaning rules.

---

# 📋 3. Automated Data Quality Report

The `Data_Quality_Report()` function creates a DataFrame containing important quality information for every column.

```python
rs = Data_Quality_Report(df)

rs
```

The report contains:

| **Column**    | **Description**                           |
| ------------- | ----------------------------------------- |
| Column        | Name of the dataset column                |
| Unique Value  | Number of unique values                   |
| Missing Value | Number of missing values                  |
| Duplicate     | Number of duplicated values in the column |
| Data Type     | Current Pandas data type                  |

Example:

```text
Column       Unique Value    Missing Value    Duplicate    Data Type
----------------------------------------------------------------------
Age                45               2             5          int64
City                8               3            20          object
Unit_Price         75               4             2          float64
Category             5               1            30          category
```

This gives a quick column-level overview of dataset quality.

---

# 💾 Part D — Clean Data Export

After cleaning, the project can save the resulting DataFrame in multiple formats.

## 📄 CSV

```python
Data_save(
    path,
    df,
    ".csv"
)
```

Uses:

```python
data.to_csv()
```

---

## 📊 Excel

```python
Data_save(
    path,
    df,
    ".xlsx"
)
```

Uses:

```python
data.to_excel()
```

---

## 🗂️ JSON

```python
Data_save(
    path,
    df,
    ".json"
)
```

Uses:

```python
data.to_json()
```

---

## 📁 Output Structure

The cleaned files are stored in:

```text
Clean_Data/
│
├── clean_data.csv
├── clean_data.xlsx
└── clean_data.json
```

This allows the cleaned dataset to be reused in different tools and workflows.

---

# 🛠️ Tech Stack

| **Technology / Concept** | **Purpose**                                 |
| ------------------------ | ------------------------------------------- |
| 🐍 Python                | Core programming language                   |
| 🐼 Pandas                | Data loading, cleaning and analysis         |
| 🔢 NumPy                 | Numerical and value-handling operations     |
| 📓 Jupyter Notebook      | Interactive project development and testing |
| 💻 VS Code               | Development environment                     |
| 📄 CSV                   | Input / output data format                  |
| 📊 Excel                 | Input / output data format                  |
| 🗂️ JSON                 | Input / output data format                  |

---

# 📚 Python & Data Concepts Practiced

This project helped me practice:

### Python

* Functions
* Parameters
* Conditional statements
* Return values
* Modules
* Importing functions
* Module reloading
* Reusable code

### Pandas

* DataFrame
* Series
* `read_csv()`
* `read_excel()`
* `read_json()`
* `isnull()`
* `fillna()`
* `dropna()`
* `duplicated()`
* `drop_duplicates()`
* `drop()`
* `astype()`
* `to_numeric()`
* `to_datetime()`
* `value_counts()`
* `describe()`
* `info()`
* `dtypes`
* `nunique()`
* `to_csv()`
* `to_excel()`
* `to_json()`

### NumPy

* `np.random.choice()`
* Numerical operations
* Array-based value selection

---

# 📈 Results & Project Output

The project produces three major types of output.

## 1️⃣ Dataset Inspection

The tool provides:

* Dataset shape
* Column names
* Data types
* Non-null information
* Statistical summary

---

## 2️⃣ Data Quality Information

The project can identify:

```text
Missing Values
      +
Duplicate Values
      +
Data Types
      +
Unique Values
      ↓
Data Quality Report
```

---

## 3️⃣ Clean Dataset

After applying selected cleaning operations, the processed dataset can be exported as:

```text
CSV
XLSX
JSON
```

The `Data_Clean_Report_Image` folder contains example screenshots/output images demonstrating the project execution and reporting.

---

# 🔍 Data Quality & Design Notes

## 1. Cleaning Rules Are Dataset Dependent

There is no single cleaning method that is correct for every dataset.

For example:

```text
Numeric Missing Value
        ↓
Mean / Median / Other Strategy
```

The correct approach depends on:

* Data distribution
* Business context
* Outlier presence
* Analysis objective

---

## 2. Numeric Imputation

The current implementation uses mean imputation:

```python
data[col].fillna(
    data[col].mean()
)
```

This is suitable as a basic demonstration but can be extended with other strategies.

---

## 3. Categorical Imputation

The current implementation uses random selection from existing non-null values.

This is mainly included as a practical learning implementation.

For production applications, more controlled approaches should be considered.

---

## 4. Duplicate Records

The project treats complete duplicate rows as duplicate records.

In real-world datasets, duplicate identification may require business-specific keys such as:

```text
Customer_ID
Order_ID
Date
Product_ID
```

---

## 5. Column Removal

Columns are manually selected for removal.

A future version could automatically suggest columns based on:

* Missing percentage
* Constant values
* Duplicate information
* Data type
* User-defined rules

---

## 6. Current Scope

The current project focuses mainly on:

```text
Data Loading
       ↓
Data Inspection
       ↓
Basic Data Cleaning
       ↓
Data Quality
       ↓
Data Export
```

It is not yet a complete automated EDA or Machine Learning preprocessing framework.

---

# 🏆 Advantages

| **Advantage**                  | **Details**                                                        |
| ------------------------------ | ------------------------------------------------------------------ |
| 🐍 **Python Practice**         | Converts individual Python/Pandas concepts into a complete project |
| ♻️ **Reusable Functions**      | Common operations can be reused across datasets                    |
| 📂 **Multiple Formats**        | Supports CSV, XLSX and JSON                                        |
| 🔍 **Data Inspection**         | Quickly checks dataset structure                                   |
| 🕳️ **Missing Value Analysis** | Identifies missing values column-wise                              |
| ♻️ **Duplicate Analysis**      | Detects duplicate records                                          |
| 🧹 **Cleaning Operations**     | Provides common cleaning functions                                 |
| 📊 **Quality Report**          | Generates a structured quality report                              |
| 💾 **Easy Export**             | Saves processed data in multiple formats                           |
| 📈 **EDA Preparation**         | Creates a foundation for further analysis                          |
| 🤖 **ML Preparation**          | Supports basic preprocessing before ML workflows                   |
| 📚 **Portfolio Project**       | Demonstrates practical Python and Data Analysis skills             |

---

# 🎯 Why I Built This Project

While learning Python, Pandas and Data Analysis, I wanted to move beyond individual coding exercises and create a practical project.

Instead of repeatedly writing separate commands for:

```text
Missing Values
Duplicates
Data Types
Column Removal
Data Inspection
File Export
```

I created reusable Python functions and combined them into a single workflow.

The purpose of the project is not to replace professional data-cleaning frameworks, but to understand how a practical data-processing utility can be designed using Python.

---

# 🤖 Connection with Data Analysis & Machine Learning

Data cleaning is an important part of many Data Analysis and Machine Learning workflows.

A simplified workflow is:

```text
                 Raw Data
                    │
                    ▼
              Data Loading
                    │
                    ▼
             Data Cleaning
                    │
                    ▼
            Data Quality Check
                    │
                    ▼
                   EDA
                    │
                    ▼
          Feature Engineering
                    │
                    ▼
           Data Preprocessing
                    │
                    ▼
             Model Training
                    │
                    ▼
            Model Evaluation
                    │
                    ▼
               Deployment
```

This project focuses primarily on:

```text
Data Loading
      ↓
Data Cleaning
      ↓
Data Quality
      ↓
EDA Preparation
```

The cleaned dataset can then be used as an input for subsequent **Data Analysis, Feature Engineering and Machine Learning workflows**.

This makes the project relevant to my learning journey toward **Machine Learning Engineering**.

---

# 🔮 Future Improvements

The project can be expanded into a more advanced data-preprocessing utility.

## 🔹 Advanced Missing Value Handling

Add:

* Median imputation
* Mode imputation
* Forward fill
* Backward fill
* Group-based imputation
* Missing-value percentage
* Configurable imputation strategies

---

## 🔹 Outlier Detection

Add automated:

* IQR method
* Z-score method
* Outlier count
* Outlier percentage
* Outlier capping
* Outlier removal

---

## 🔹 Automated EDA

Generate:

* Histograms
* Box plots
* Correlation matrix
* Distribution analysis
* Categorical analysis
* Numerical analysis
* Automated EDA report

---

## 🔹 Advanced Data Validation

Add validation for:

* Invalid values
* Negative values
* Impossible dates
* Inconsistent categories
* Duplicate IDs
* Missing percentages
* Unexpected data ranges

---

## 🔹 Data Cleaning Configuration

Allow users to define cleaning rules instead of manually changing Python code.

Example:

```text
Configuration
      ↓
Cleaning Rules
      ↓
Automatic Processing
      ↓
Clean Dataset
```

---

## 🔹 Interactive Interface

A future version could provide a user interface using:

* Streamlit
* Flask
* FastAPI

Possible workflow:

```text
Upload Dataset
      ↓
Data Quality Report
      ↓
Cleaning Suggestions
      ↓
Select Cleaning Operations
      ↓
Clean Dataset
      ↓
Download / Export
```

---

## 🔹 Machine Learning Preprocessing

Future versions can include:

* Encoding categorical variables
* Feature scaling
* Train-test split
* Feature selection
* Feature engineering
* ML-ready dataset generation

---

## 🔹 Advanced ML Dataset Preparation

The long-term concept can become:

```text
                 Upload Dataset
                       │
                       ▼
             Automated Data Quality
                       │
                       ▼
               Cleaning Suggestions
                       │
                       ▼
                 Data Cleaning
                       │
                       ▼
                      EDA
                       │
                       ▼
             Feature Engineering
                       │
                       ▼
              ML-Ready Dataset
```

---

# ▶️ How to Run

## 1️⃣ Install Python

Make sure Python is installed.

Check the version:

```bash
python --version
```

---

## 2️⃣ Install Required Libraries

Install Pandas and NumPy:

```bash
pip install pandas numpy
```

For Excel file support, install:

```bash
pip install openpyxl
```

---

## 3️⃣ Clone the Repository

Clone the project repository and open the project folder in VS Code.

---

## 4️⃣ Project Files

Make sure the project contains:

```text
Data_Source.py
Data_Cleaning_Tool.ipynb
Massi_Data/
```

---

## 5️⃣ Open the Notebook

Open:

```text
Data_Cleaning_Tool.ipynb
```

in Jupyter Notebook / JupyterLab or VS Code.

---

## 6️⃣ Import the Python Module

The notebook uses:

```python
import importlib
import Data_Source

importlib.reload(Data_Source)

from Data_Source import *
```

The `reload()` step is useful during development when changes are made to `Data_Source.py`.

---

## 7️⃣ Load Dataset

Example:

```python
df = Data_Load(
    "Massi_Data/Data_Cleaning_Practice_Dataset.xlsx"
)

df.head(3)
```

---

## 8️⃣ Perform Cleaning Operations

Run the required functions from the notebook:

```python
Show_Data_Type(df)

Missing_Value_Show(df)

Show_Duplicated_Value(df)

Data_Quality_Report(df)
```

Then apply the required cleaning operations.

---

## 9️⃣ Save Clean Data

Example:

```python
Data_save(
    "Clean_Data",
    df,
    ".csv"
)
```

or:

```python
Data_save(
    "Clean_Data",
    df,
    ".xlsx"
)
```

or:

```python
Data_save(
    "Clean_Data",
    df,
    ".json"
)
```

---

# 📂 Input & Output

## Input

```text
Massi_Data/
│
├── Data_Cleaning_Practice_Dataset.csv
├── Data_Cleaning_Practice_Dataset.xlsx
└── Data_Cleaning_Practice_Dataset.json
```

## Output

```text
Clean_Data/
│
├── clean_data.csv
├── clean_data.xlsx
└── clean_data.json
```

## Reports / Screenshots

```text
Data_Clean_Report_Image/
```

---

# 📌 Learning Outcome

Through this project, I learned how to convert individual Python and Pandas concepts into a reusable practical utility.

The project strengthened my understanding of:

```text
Python
   ↓
Functions & Modules
   ↓
Pandas + NumPy
   ↓
Data Cleaning
   ↓
Data Quality
   ↓
EDA Preparation
   ↓
ML Data Preparation
```

It also helped me understand how raw datasets can be systematically inspected and prepared before they are used for further analysis or Machine Learning.

---

# 👤 Author

### **Himanshi Sangani**

🎓 **BCA Graduate**

**AI/ML & Data Science Learner | Aspiring ML Engineer**

### Areas of Interest

* 🐍 Python
* 📊 Data Analysis
* 🗃️ SQL
* 📈 Data Visualization
* 🤖 Machine Learning
* 🧹 Data Preprocessing
* ⚙️ Feature Engineering
* 🧠 Deep Learning
* 💬 NLP
* 👁️ Computer Vision

> *"Learning Python and Data Analysis today, building practical Machine Learning solutions tomorrow."*

---

# 🙏 Acknowledgements

This project was developed through hands-on learning and practical experimentation with Python and Data Analysis concepts.

I would like to acknowledge:

* 📚 Python learning resources
* 🐼 Pandas documentation and learning resources
* 🔢 NumPy documentation and learning resources
* 📓 Jupyter Notebook
* 💻 VS Code
* 🧪 Practical dataset experimentation
* 🚀 Continuous learning and project-based practice

---

# ⭐ Conclusion

The **Automated Data Cleaning & EDA Tool** is a practical Python project that combines reusable data-cleaning functions into a structured workflow.

The current version focuses on:

```text
📥 Data Loading
      ↓
🔍 Data Inspection
      ↓
🧹 Data Cleaning
      ↓
📊 Data Quality Analysis
      ↓
💾 Clean Data Export
```

With future development, the project can be extended toward **Automated EDA, Advanced Data Preprocessing and ML-Ready Dataset Preparation**.

This project represents a practical step in my journey from **Python and Data Analysis toward Machine Learning Engineering**.
