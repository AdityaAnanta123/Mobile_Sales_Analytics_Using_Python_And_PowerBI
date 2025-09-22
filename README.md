# 📊 Mobile Sales Analytics Using Python & Power BI

This project aims to **analyze Mobile and Laptop sales data** using:  
- **Python** → for preprocessing & uploading data to database  
- **MySQL** → for data storage & validation  
- **Power BI** → for analysis and interactive visualization  

The analysis is expected to provide **deeper insights** into product sales (brand, revenue, margin, quantity, etc.), which can serve as the basis for better business decision-making.  

## 🚀 Project Workflow
The workflow is divided into **3 main parts**:  

### 1️⃣ Python — Data Preprocessing & Upload
- Dataset source: Kaggle → *"Mobiles & Laptop Sales Data"* (by VINOTH KANNA S).  
- Used **`kagglehub`** to connect the Kaggle repo with the local repository.  
- Preprocessing includes:
  - Handling *missing values* using the **center of tendency** technique (mean/median/mode).  
  - Cleaning and standardizing columns.  
- The cleaned dataset is exported as `mobile_data.csv`.  
- Data is then uploaded to **MySQL** using **`sqlalchemy`** with database connection variables (host, user, password, dbname, port).  

### 2️⃣ MySQL — Data Storage & Validation
- The uploaded dataset is rechecked in MySQL.  
- Validation includes:
  - Data types (int, decimal, varchar, date).  
  - Data completeness (duplicate & null value checks).  
- The validated dataset is ready to be used as the **fact table** for analysis.  

### 3️⃣ Power BI — Dashboard & Insights
- Power BI is connected to MySQL using **MySQL Connector**.  
- The dashboard consists of 3 pages:
  1. **Overview** → KPI summary (Total Sales, Profit, Quantity, Avg. Margin).  
  2. **Product Analysis** → detailed product & brand analysis (Top-N products, YoY Sales %, Revenue vs Profit Margin scatter plot).  
  3. **Report Table** → complete data table with interactive filters.  
- Slicers are added (Brand, Region, Year) for dynamic analysis.  

## 📂 Project Structure
```bash
├── data/ # Dataset (CSV after preprocessing)
│   ├── mobile_data.csv
│   └── mobile_sales_data.csv
│
├── scripts/ # Python scripts for ETL
│   ├── import_dataset.py
│   ├── import_mysql.py
│   └── preprocessing.py
│
├── dashboards/ # Power BI file (.pbix) + screenshots
│   ├── Mobile_Sales_Dashboard.pbix
│   ├── Overview Page.png
│   ├── Product Page.png
│   └── Report Page.png
│
└── README.md
```
## 🛠️ Tech Stack & Libraries
**Python**: pandas, numpy, kagglehub, sqlalchemy, mysql-connector-python, python-dotenv
**Database**: MySQL
**Visualization**: Power BI

## 📌 How to Use This Repository

### 1️⃣ Clone Repository
```bash
git clone https://github.com/AdityaAnanta123/Mobile_Sales_Analytics_Using_Python_And_PowerBI.git
cd Mobile_Sales_Analytics_Using_Python_And_PowerBI
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Download Dataset
Make sure to connect your Kaggle account with kagglehub or download manually from Kaggle.
Save the dataset inside the data/ folder.

### 4️⃣ Run ETL with Python
```bash
python scripts/import_dataset.py
python scripts/import_mysql.py
python scripts/preprocessing.py
```

### 5️⃣ Verify in MySQL
Ensure the table is created successfully (e.g., mobile).
Run a simple query:
```bash
SELECT COUNT(*) FROM mobile;
```

### 6️⃣ Open Dashboard in Power BI
Open dashboards/Mobile_Sales_Dashboard.pbix

Refresh MySQL connection (enter host, username, password)

Dashboard is ready to use 🚀

## 📸 Dashboard Preview
Here are sample screenshots from the Power BI dashboard:
### 📌 Halaman Overview
![Overview Dashboard](https://github.com/AdityaAnanta123/Mobile_Sales_Analytics_Using_Python_And_PowerBI/blob/main/dashboards/Overview%20Page.png)

### 📌 Halaman Product Analysis
![Product Dashboard](https://github.com/AdityaAnanta123/Mobile_Sales_Analytics_Using_Python_And_PowerBI/blob/main/dashboards/Product%20Page.png)

### 📌 Halaman Report
![Report Dashboard](https://github.com/AdityaAnanta123/Mobile_Sales_Analytics_Using_Python_And_PowerBI/blob/main/dashboards/Report%20Page.png)





