📈 Open Manus – Stock Market Analysis
🚀 Overview
This project implements Open Manus, a stock market analysis tool that identifies Indian stocks that hit their 52-week high in the last month.

The script fetches stock data, compares the 52-week high with the highest price in the last month, and outputs the stocks that match the criteria.

📝 Requirements
Implement a fully working script that fetches and analyzes stock market data.
Ensure the solution is well-structured, properly tested, and meets expected standards.
Submit the code within 2 days from the assigned deadline.
⚙️ Setup & Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/mannaandpoem/OpenManus.git
cd OpenManus
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Script
bash
Copy
Edit
python fetch_stocks.py
📜 How It Works
Fetches stock data for selected Indian stocks.
Retrieves the 52-week high and highest price in the last month.
Compares both values to check if the stock reached its 52-week high in the last month.
Displays the results.
✅ Example Output
yaml
Copy
Edit
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
