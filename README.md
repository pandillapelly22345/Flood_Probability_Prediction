# 🌊 Flood Prediction Using Machine Learning

**Contributors:**  
- Aditya Kumar Singh  
- Harsh Vishwakarma  
- Nutan Kumari  
- Pandillapelly Harshvardhini  

---

## 📌 Project Overview

This project presents a machine learning-based flood prediction system that forecasts flood probability using environmental and infrastructure-related features. With a dataset of over **1.8 million entries**, the model aims to provide accurate early flood warnings, aiding disaster preparedness and management.

🔗 [GitHub Repository](https://github.com/pandillapelly22345/Flood_Probability_Prediction)

---

## 💡 Motivation

Floods are devastating natural disasters, and existing prediction models often fail to capture complex environmental interactions. This project seeks to develop an **AI-driven predictive system** that improves the **timeliness and accuracy** of flood risk detection using real-world features.

---

## 📊 Dataset Details

- **Records:** 1.8 million+
- **Features (20)** include:
  - Monsoon Intensity, Deforestation, Topography Drainage, Urbanization
  - Dams Quality, Climate Change, Infrastructure Decay
  - Drainage Systems, Encroachments, Wetland Loss, etc.
- **Target Variable:** Flood Probability (continuous)

**Preprocessing Highlights:**
- Handled missing values (especially in the target column)
- Conducted correlation analysis to reduce multicollinearity
- Feature engineering and re-evaluation improved model performance

---

## 🔍 Machine Learning Models Used

| Model               | After Tuning - R² Score | RMSE      |
|--------------------|--------------------------|-----------|
| Linear Regression  | 0.8449                   | 0.02008   |
| Decision Tree      | 0.3024                   | 0.04258   |
| Random Forest      | 0.6270                   | 0.03110   |
| Support Vector Reg | 0.8395                   | 0.02040   |
| MLP Regressor      | **0.8614**               | **0.01897** |

📈 **Best Performing Model:** MLP Regressor  
📌 **Baseline Model:** Linear Regression

---

## ⚙️ Methodology

- Regression models trained on 80-20 train-test split
- Evaluation metrics: **MSE, MAE, RMSE, R² Score**
- Hyperparameter tuning significantly improved all model performances
- Feature selection re-adjusted after observing model behavior

---

## 🖥️ GUI Application

Developed using **Flask**, this web-based GUI allows users to:
- Input values for 20 environmental factors
- Receive real-time prediction from the trained ML model
- Get flood risk output: "Flood Expected" or "No Flood"

✅ **Model used in GUI:** Pre-trained MLP model (.pkl)

---

## 🔬 Key Insights

- Infrastructure deterioration and poor drainage strongly correlate with higher flood probability
- MLP outperformed other models in both accuracy and generalization
- Feature reintroduction (even with multicollinearity) enhanced performance
- GUI makes model accessible for non-technical users and policy planners

---

## 📚 References

- [Numpy Documentation](https://numpy.org/doc/)
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [Matplotlib](https://matplotlib.org/)
- [ScienceDirect – Flood ML Papers](https://www.sciencedirect.com/science/article/pii/S2212420921001205)

---


The dataset used for this project can be found on Kaggle at the following link:
[Flood Prediction Features Dataset](https://www.kaggle.com/datasets/huli12/flood-prediction-features/data)

