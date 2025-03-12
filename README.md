# 📈 Open Manus – Stock Market Analysis  

## 🚀 Overview  
This project identifies **Indian stock market stocks** that hit their **52-week high** in the last month using Yahoo Finance API (`yfinance`). The script fetches stock data, compares the **52-week high** with the **highest price in the last month**, and outputs the stocks that match the criteria.  

## ⚙️ Setup & Installation  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/lalasa0/Open_Manus_Stocks.git
cd Open_Manus_Stocks
```
### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Script  
```bash
python fetch_stocks.py
```

## 📜 How It Works  
✔ Fetches stock data for selected **Indian stocks**.  
✔ Retrieves the **52-week high** and **highest price in the last month**.  
✔ Compares both values to check if the stock reached its 52-week high in the last month.  
✔ Displays the results.  

## ✅ Example Output  
```
Stock: RELIANCE.NS
52-Week High: 1608.8
Max High in Last Month: 1266.5

Stock: TCS.NS
52-Week High: 4592.25
Max High in Last Month: 4052.0

Stock: BAJFINANCE.NS
52-Week High: 8739.0
Max High in Last Month: 8739.0

Stocks that hit 52-week high in the last month:
BAJFINANCE.NS
```

## 📂 Files in the Repository  
📌 `fetch_stocks.py` – The main script  
📌 `requirements.txt` – Dependencies list  
📌 `README.md` – Documentation  

## 🔹 Notes  
  - Make sure `yfinance` is installed before execution.  
- The script is designed to work with **Indian stocks (NSE)**.  

📌 **Developed as part of Open Manus for Indian stock market analysis.**  
