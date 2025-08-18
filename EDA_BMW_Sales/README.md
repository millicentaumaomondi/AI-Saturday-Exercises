# BMW Sales EDA Dashboard

This project provides an interactive dashboard for exploring and analyzing BMW sales data using Streamlit. The dashboard enables users to perform exploratory data analysis (EDA) on a rich dataset of BMW car sales, with interactive filters and a variety of insightful visualizations.

## Features & EDA Insights

The dashboard is organized into three main sections (tabs):

### 1. Overview
- **Sales Over Time:** Visualizes total sales volume by year, helping to identify trends and growth patterns.
- **Sales by Model:** Compares sales volumes across different BMW models.
- **Sales by Region:** Shows how sales are distributed across global regions.
- **Sales by Transmission:** Compares sales volumes for different transmission types (Automatic, Manual).
- **Sales by Fuel Type:** Analyzes the popularity of different fuel types (Petrol, Diesel, Hybrid, Electric).

### 2. Engine Analysis
- **Mileage by Engine Size:** Examines the relationship between engine size and mileage using a line plot.
- **Price by Engine Size:** Explores how engine size relates to car price.

### 3. Sales Classification
- **High/Low Sales per Fuel Type:** Grouped bar chart showing the number of high and low sales for each fuel type.
- **High/Low Sales per Region:** Grouped bar chart showing the number of high and low sales for each region.

### Interactive Features
- **Sidebar Filters:** Filter the data by year range, region, model, transmission, and fuel type.
- **Dynamic Visualizations:** All plots update automatically based on the selected filters.
- **Summary Stats:** The dashboard displays total sales volume and the top-selling model.

---

## EDA Insights

- **Sales Classification by Region:**
  - Across all regions (Africa, Asia, Europe, Middle East, North America, South America), the number of **Low** sales classifications significantly exceeds **High** sales classifications.
  - The distribution is consistent, suggesting that regardless of region, most sales fall into the "Low" classification.

- **Sales Over Time:**
  - **Sales volume has remained relatively stable** from 2010 to 2024, with only minor fluctuations year to year.
  - There are no dramatic spikes or drops, indicating a steady market for BMW sales over the years.

- **Sales Classification by Fuel Type:**
  - For all fuel types (Diesel, Electric, Hybrid, Petrol), **Low** sales classifications are much more common than **High**.
  - The difference is consistent across fuel types, suggesting that fuel type does not strongly influence the likelihood of a sale being classified as "High".

- **Sales Distribution by Model:**
  - Sales volumes are fairly similar across different BMW models, with no single model dominating the market.
  - There are some minor variations, but overall, the sales distribution is balanced.

- **Price by Engine Size:**
  - **Price does not show a strong trend with engine size**; prices fluctuate within a similar range across all engine sizes.
  - There is considerable variance, indicating that other factors besides engine size may play a larger role in determining price.

- **Sales Distribution by Transmission Over Time:**
  - Both **Manual** and **Automatic** transmissions have similar sales trends over time, with no clear dominance of one over the other.
  - Sales for both types remain steady, with overlapping confidence intervals.

- **Sales Distribution by Color:**
  - Sales volumes are very similar across all car colors (Red, Blue, Black, Silver, White, Grey).
  - This suggests that **color does not significantly impact sales volume** for BMWs.

- **Average Price by Color:**
  - The average price of BMWs is also very similar across all colors.
  - This indicates that no particular color commands a price premium or discount in the market.

- **Mileage by Engine Size:**
  - **Mileage remains relatively constant** across different engine sizes, with no clear upward or downward trend.
  - There is some variance, but no strong relationship is observed.

- **Sales Volume by Engine Size:**
  - Sales volume does not show a strong trend with engine size; it remains relatively stable across the range of engine sizes.

---

## How to Use These Insights

- **Market Strategy:** Focus on factors other than region, color, or engine size, as these do not show strong influence on sales volume or classification.
- **Product Development:** Since sales are balanced across models and features, BMW can maintain a diverse product lineup.
- **Further Analysis:** Investigate other variables (e.g., marketing campaigns, economic factors) that might explain the predominance of low sales classifications.

## How to Run the Dashboard

1. **Install dependencies:**
   Ensure you have Python 3.8+ installed. Install required packages with:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the dashboard:**
   ```bash
   streamlit run dashboard.py
   ```
3. **Interact:**
   Open the provided local URL in your browser to interact with the dashboard.

## Dataset
The dashboard uses a CSV file (`BMW_sales.csv`) containing columns such as Model, Year, Region, Color, Fuel_Type, Transmission, Engine_Size_L, Mileage_KM, Price_USD, Sales_Volume, and Sales_Classification.

## Dependencies
- streamlit
- pandas
- numpy
- matplotlib
- seaborn

---

