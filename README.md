# 📊 Mobile Sales Analytics Using Python & Power BI

Proyek ini bertujuan untuk **menganalisis data penjualan Mobile dan Laptop** dengan menggunakan:
- **Python** → untuk preprocessing & upload data ke database  
- **MySQL** → untuk penyimpanan & validasi data  
- **Power BI** → untuk analisis dan visualisasi interaktif  

Analisis ini diharapkan memberikan **insight mendalam** mengenai penjualan produk (brand, revenue, margin, quantity, dll.) sehingga bisa digunakan sebagai dasar pengambilan keputusan bisnis.


## 🚀 Alur Kerja Proyek
Alur kerja dibagi menjadi **3 bagian utama**:

### 1️⃣ Python — Data Preprocessing & Upload
- Dataset diperoleh dari Kaggle: *"Mobiles & Laptop Sales Data"* (oleh VINOTH KANNA S).  
- Menggunakan **library `kagglehub`** untuk menghubungkan Kaggle repo dengan repo lokal.  
- Preprocessing meliputi:
  - Penanganan *missing values* dengan teknik **center of tendency** (mean/median/mode).  
  - Pembersihan & standarisasi kolom.  
- Dataset hasil preprocessing diekspor menjadi `mobile_data.csv`.  
- Data kemudian di-*upload* ke **MySQL** menggunakan **`sqlalchemy`** dengan variabel koneksi database (host, user, password, dbname, port).  

### 2️⃣ MySQL — Data Storage & Validation
- Dataset yang sudah di-*upload* dicek kembali di MySQL.  
- Validasi meliputi:
  - Tipe data (int, decimal, varchar, date).  
  - Kelengkapan data (cek duplikasi & null values).  
- Data yang valid siap digunakan sebagai **fact table** untuk analisis.

### 3️⃣ Power BI — Dashboard & Insight
- Power BI dihubungkan ke MySQL menggunakan **MySQL Connector**.  
- Desain dashboard dibagi menjadi 3 halaman:
  1. **Overview** → ringkasan KPI utama (Total Sales, Profit, Quantity, Average Margin).  
  2. **Product Analysis** → analisis detail brand & produk (Top-N products, YoY Sales %, Revenue vs Profit Margin Scatter Plot).  
  3. **Report Table** → tampilan tabel lengkap dengan filter interaktif.  
- Slicer ditambahkan (Brand, Region, Tahun) untuk analisis dinamis.  


## 📂 Struktur Project
```bash
├── data/ # Dataset (CSV hasil preprocessing)
│ ├── mobile_data.csv
│ └── mobile_sales_data.csv
│
├── scripts/ # Python scripts untuk ETL
│ ├── import_dataset.py
│ ├── import_mysql.py
│ └── preprocessing.py
│
├── dashboards/ # File Power BI (.pbix) + Screenshot
│ ├── Mobile_Sales_Dashboard.pbix
│ ├── Overview Page.png
│ ├── Product Page.png
│ └── Report Page.png
│
└── README.md

## 🛠️ Teknologi & Library yang Digunakan
- **Python**: `pandas`, `numpy`, `kagglehub`, `sqlalchemy`, `mysql-connector-python`, `python-dotenv`  
- **Database**: MySQL  
- **Visualization**: Power BI  

## 📌 Cara Menggunakan Repo Ini

### 1️⃣ Clone Repository
```bash
git clone https://github.com/AdityaAnanta123/Mobile_Sales_Analytics_Using_Python_And_PowerBI.git
cd Mobile_Sales_Analytics_Using_Python_And_PowerBI



