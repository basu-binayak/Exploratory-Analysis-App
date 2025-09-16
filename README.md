# 📊 Exploratory-Analysis-App

An **interactive Streamlit web application** for performing **Exploratory Data Analysis (EDA)** with ease.
This app helps you quickly upload datasets, explore data distributions, identify patterns, visualize correlations, and generate advanced insights without writing code.

---

## 🚀 Features

* **📂 File Upload**: Upload CSV or Excel files.
* **👀 Dataset Preview**: View dataset head and metadata.
* **📊 Data Overview**: Summary statistics, missing values, unique counts.
* **🎨 Univariate Analysis**: Histograms, boxplots, bar charts.
* **🔗 Bivariate Analysis**: Scatterplots, grouped boxplots, correlation heatmaps.
* **⚡ Advanced EDA**:

  * Feature importance (using Random Forest)
  * PCA visualization for dimensionality reduction
  * Automated profiling report (`pandas-profiling` / `ydata-profiling`)
* **🖥️ Sidebar Navigation**: Organized workflow for seamless analysis.
* **🎨 Theming**: Clean UI with Streamlit themes.

---

## 🛠️ Tech Stack

* **Frontend & Backend**: [Streamlit](https://streamlit.io/)
* **Data Handling**: [Pandas](https://pandas.pydata.org/)
* **Visualization**: [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)
* **Advanced Analysis**: [Scikit-learn](https://scikit-learn.org/), [ydata-profiling](https://github.com/ydataai/ydata-profiling)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Exploratory-Analysis-App.git
cd Exploratory-Analysis-App
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open your browser at [http://localhost:8501](http://localhost:8501).

---

## 🌐 Deployment

You can deploy the app easily on:

* [Streamlit Cloud](https://streamlit.io/cloud) (recommended)
* [Heroku](https://www.heroku.com/)
* [Railway](https://railway.app/)

---

## 📌 Project Structure

```
Exploratory-Analysis-App/
│── app.py                 # Main Streamlit app
│── requirements.txt       # Project dependencies
│── README.md              # Project documentation
│── data/                  # (Optional) Sample datasets
│── assets/                # (Optional) Images, logos, etc.
```

---

## 🎯 Roadmap

* [x] Dataset Upload & Preview
* [x] Data Overview
* [x] Univariate Analysis
* [x] Bivariate Analysis
* [x] Advanced EDA (Feature Importance, PCA, Auto-EDA)
* [x] Polished UI with Sidebar Navigation
* [x] Add interactive filters & drill-downs
* [ ] Support for large datasets with Dask/Polars
* [ ] Export insights as PDF/HTML report

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request.

---

## 📜 License

This project is licensed under the **Apache 2.0 License** – see the [LICENSE](LICENSE) file for details.

---

