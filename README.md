# 🏠 House Price Prediction

## 📌 Project Overview

This project focuses on predicting house prices using Machine Learning techniques. It explores different housing features and builds regression models to estimate house prices based on property characteristics.

The project includes Exploratory Data Analysis (EDA), Data Preprocessing, Model Training, Evaluation, and Model Comparison.

## 🎯 Objectives

- Understand housing data through Exploratory Data Analysis.
- Identify relationships between housing features and sale prices.
- Build Machine Learning regression models.
- Evaluate and compare model performance.
- Predict house prices using a trained model.

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── data/
│   └── house_prices_practice.csv
│
├── models/
│   └── house_price_model.pkl
│
├── notebooks/
|    └── houseprediction.ipynb
|
├── Visualization/
|   └──Visulization image
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 📊 Dataset Information

- Total Records: 300
- Total Features: 8
- Target Variable: `SalePrice`
- Missing Values: 0
- Duplicate Rows: 0

### Features Used

| Feature | Description |
|---|---|
| OverallQual | Overall material and finish quality |
| GrLivArea | Above-ground living area |
| GarageCars | Garage capacity |
| TotalBsmtSF | Total basement area |
| YearBuilt | Original construction year |
| FullBath | Number of full bathrooms |
| BedroomAbvGr | Bedrooms above ground |
| LotArea | Lot size |

**Target Variable:** `SalePrice`

## 🛠️ Technologies & Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

## ⚙️ Project Workflow

1. Data Loading and Understanding
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Feature and Target Separation
5. Train-Test Split (80:20)
6. Model Training
7. Model Evaluation
8. 5-Fold Cross Validation
9. Model Comparison
10. Residual Analysis
11. Feature Coefficient Analysis
12. New House Price Prediction
13. Model Saving using Joblib

## 🤖 Machine Learning Models

Three regression algorithms were implemented:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

## 📈 Model Performance

### Test Set Results

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 10,431.66 | 12,505.46 | 0.9724 |
| Decision Tree | 35,962.77 | 47,113.47 | 0.6088 |
| Random Forest | 21,414.52 | 27,405.67 | 0.8676 |

### 5-Fold Cross Validation Results

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 9,615.37 | 11,264.04 | 0.9767 |
| Decision Tree | 37,797.00 | 46,446.94 | 0.6015 |
| Random Forest | 23,589.44 | 29,054.83 | 0.8448 |

## 🏆 Best Performing Model

Based on the evaluation and cross-validation results, **Linear Regression** achieved the best performance among the three models.

- Test R² Score: 0.9724
- Cross Validation R² Score: 0.9767
- Test MAE: 10,431.66
- Test RMSE: 12,505.46

Therefore, Linear Regression was selected as the final model for house price prediction.

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/mdraihanmostafa746-coder/House-Price-Prediction-.git
```

### 2. Navigate to the Project Directory

```bash
cd House-Price-Prediction-
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Jupyter Notebook

```bash
jupyter notebook
```

Open `houseprediction.ipynb` and run the cells.

## 💾 Saved Model

The trained Linear Regression model is saved as:

`models/house_price_model.pkl`

The saved model can be loaded using Joblib for future predictions.

## 📌 Limitations

- The dataset contains only 300 records.
- Model performance may vary on larger or real-world housing datasets.
- Further validation on independent datasets is required before real-world use.

## 👨‍💻 Author

**MD Raihan Mostafa**

B.Sc. Data Science Student | Aspiring AI Engineer

GitHub: [mdraihanmostafa746-coder](https://github.com/mdraihanmostafa746-coder)

---

⭐ If you find this project useful, feel free to explore the repository!