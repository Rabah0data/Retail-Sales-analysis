# 🛍️ Retail Sales Analysis Dashboard

An interactive Streamlit dashboard analyzing 99,457 retail transactions across 10 shopping malls in Istanbul. The dashboard surfaces revenue trends, category performance, customer demographics, and payment behavior through a fully filterable interface.

**[🔗 Live Demo](#)** ← add your Streamlit Cloud URL here

![Dashboard Screenshot](screenshots/dashboard.png)

---

## 📌 Project Summary

Raw invoice-level transaction data was cleaned, feature-engineered, and transformed into a business intelligence dashboard. The goal was to identify who drives revenue, when demand peaks, and which product categories matter most — the kind of questions a retail or marketing team would ask before planning a quarter.

**Tech stack:** Python · Pandas · Streamlit · Plotly

**Dataset:** [Kaggle — Customer Shopping Dataset](https://www.kaggle.com/datasets/mehmettahiraslan/customer-shopping-dataset) (Istanbul retail transactions)

---

## 🔍 Key Findings

### 1. Female customers drive the majority of revenue
Female shoppers account for **59.7%** of total revenue ($150.2M) versus **40.3%** for male shoppers ($101.3M). This gap holds consistently across categories, suggesting marketing spend and inventory planning should weight toward female-oriented products and messaging.

### 2. Sales peak in winter, especially January
**January** is the single strongest month, and the **winter period (Dec–Feb)** accounts for **~30%** of annual revenue despite being only 25% of the calendar year. Revenue is comparatively flat through the rest of the year. This points to a clear seasonal buying pattern — likely tied to holiday shopping and New Year sales — that should inform inventory stocking and promotional timing.

### 3. Clothing dominates category revenue; Books and Souvenirs barely register
| Category | Revenue |
|---|---|
| Clothing | $114.0M |
| Shoes | $66.6M |
| Technology | $57.9M |
| Cosmetics | $6.8M |
| Toys | $4.0M |
| Food & Beverage | $0.85M |
| Books | $0.83M |
| Souvenir | $0.64M |

Clothing alone generates more revenue than every other category combined. Books and Souvenirs are effectively negligible — candidates for reduced shelf space or bundling strategies rather than standalone promotion.

### 4. The 35–45 age group has the highest purchasing power
Customers aged **36–45** generate the most revenue of any age bracket ($50.2M), narrowly ahead of 46–55 and 56–65. Purchasing power is concentrated in the **35–55** range overall, while under-25 and over-65 segments contribute significantly less. This is the core demographic to target for loyalty programs and premium product lines.

---

## ⚙️ Dashboard Features

- **Feature engineering:** `total` revenue (quantity × price), `month` extracted in `%b` format, custom age-group binning
- **KPI cards:** Revenue, Orders, Average Order Value
- **Visuals:**
  - Monthly sales trend (line chart)
  - Sales by category (bar chart)
  - Sales by gender (pie chart)
  - Payment method distribution (bar chart)
  - Age group revenue breakdown (bar chart)
- **Interactive filters:** category, month, gender, payment method (sidebar, live cross-filtering)
- **Key insights panel:** auto-generated from the currently filtered dataset
- **Raw data explorer:** expandable table of filtered records

---

## 🚀 Run Locally

```bash
git clone https://github.com/<your-username>/retail-sales-analysis.git
cd retail-sales-analysis/dashboard
pip install -r requirements.txt
streamlit run app_simple.py
```

Make sure `customer_shopping_data.csv` is in the same folder as `app_simple.py`.

---

## 🌐 Deployment

Hosted on [Streamlit Community Cloud](https://share.streamlit.io). To redeploy:
1. Push this repo to GitHub
2. Connect it at share.streamlit.io
3. Set the entry point to `dashboard/app_simple.py`

---

## 🔮 Next Steps

- Segment customers by recency, frequency, and monetary value (RFM analysis)
- Build a simple forecast model for next month's revenue
- Add a geographic breakdown by shopping mall
- A/B test hypothesis: does targeted winter promotion for the 35–45 female segment lift Clothing category revenue further?

---

Built by [Your Name] · [LinkedIn](#) · [Portfolio](#)
