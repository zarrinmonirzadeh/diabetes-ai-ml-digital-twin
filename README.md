# Diabetes AI/ML Digital Twin Framework

### 📌 Author: **Zarrin Monirzadeh**  
Data Engineer | Software Engineer | **AI in Healthcare**

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![ML](https://img.shields.io/badge/MachineLearning-Enabled-green)
![AI](https://img.shields.io/badge/AI-Healthcare--Focused-purple)
![Status](https://img.shields.io/badge/Status-Research--Prototype-orange)

An AI/ML-driven digital twin framework for diabetes that integrates machine learning, temporal modeling, and causal inference to enable decision-aware healthcare systems.

---

## 🧠 Overview

This repository presents a **reproducible digital twin architecture** for modeling glucose dynamics in diabetes patients using Continuous Glucose Monitoring (CGM) data.

Unlike traditional predictive models, this framework enables:

- Simulation of interventions (diet, activity)
- Counterfactual outcome estimation
- Temporal glucose modeling
- Decision-support insights grounded in AI and causal inference

---

## ⚙️ Methodology

### 🔹 Machine Learning (AI Core)
- Regression-based prediction
- Classification of glucose states
- Neural networks (MLP)

### 🔹 Time-Series Modeling
- CGM trajectory representation
- Temporal dynamics capture

### 🔹 Causal Inference
- Counterfactual reasoning
- Difference-in-Differences (DiD)

### 🔹 Simulation Engine
- Intervention-based trajectory generation
- Scenario comparison

---

## 📄 Paper

📄 [View Preview](paper/PreviewPaper.pdf)

Full version available upon request:

📧 **monirzadehzarrin@gmail.com**

---
## 🏗️ System Architecture

The digital twin framework is designed as a modular pipeline:

1. Data Ingestion
   - XML → parsed CGM streams
   - CSV → structured datasets

2. Feature Engineering
   - Temporal features (lags, rolling stats)
   - Physiological constraints

3. Modeling Layer
   - Regression models (baseline)
   - ML models (scikit-learn / MLP)

4. Simulation Engine
   - Counterfactual trajectory generation
   - Intervention modeling (diet, activity)

5. Evaluation Layer
   - RMSE / MAE
   - Clinical metrics (time-in-range)

6. Visualization
   - CGM plots
   - Counterfactual comparisons
  
---
## ⚡ Engineering Highlights

- Built end-to-end ML pipeline from raw XML clinical data
- Designed reproducible data processing for multi-patient CGM streams
- Implemented counterfactual simulation engine for intervention analysis
- Structured modular pipeline (train/test separation)
- Generated interpretable outputs for clinical decision support

---
## 🧪 Data Pipeline

Raw CGM XML → CSV → AI Modeling → Simulation

- XML samples: `code/sample_raw_xml/`
- CSV outputs: `code/sample_raw_csv/`
- Pipelines:
  - `train_pipeline.ipynb`
  - `test_pipeline.ipynb`

---

## 📊 Sample Outputs

### 🔹 Regression Results

| Model | MAE | RMSE | R2 |
|------|-----|------|----|
| Linear Regression | 43.2 | 54.1 | 0.45 |
| Random Forest | 35.8 | 47.2 | 0.62 |
| Gradient Boosting | 33.1 | 44.9 | 0.68 |
| MLP | 30.5 | 41.7 | 0.72 |

📂 Full file: [regression_results.csv](code/regression_results.csv)

---

### 🔹 Classification Results

| Model | Accuracy | AUC |
|------|----------|-----|
| Logistic Regression | 0.78 | 0.84 |
| Random Forest | 0.85 | 0.91 |
| Gradient Boosting | 0.87 | 0.93 |
| MLP | 0.89 | 0.95 |

📂 Full file: [classification_results.csv](code/classification_results.csv)

---

### 🔹 Counterfactual Summary

| Scenario | Peak Glucose | Time in Range (%) |
|----------|--------------|------------------|
| Baseline (60g carbs) | 179 | 58 |
| Reduced carbs (30g) | 153 | 72 |
| Walking intervention | 163 | 68 |

📂 Full file: [counterfactual_summary.csv](code/counterfactual_summary.csv)

---

## ▶️ How to Run

### Install dependencies

```bash
pip install pandas numpy matplotlib scikit-learn
```

### Run pipeline

```bash
python code/demo_pipeline.py
```

### Or run notebooks

- `train_pipeline.ipynb`
- `test_pipeline.ipynb`

---
## 🧩 Challenges

- Noisy CGM data and missing values
- Temporal dependency modeling
- Aligning causal inference with time-series data
- Translating ML outputs into clinically meaningful insights

---
## 📊 Results & Visualizations

(See repository figures folder for all figures Fig01–Fig19)

---

## 💡 Key Contributions

- Patient-specific digital twin modeling  
- Simulation of treatment scenarios  
- Causal inference for intervention effects  
- Explainable AI for healthcare decision support  
- AI-driven digital twin modeling  
- Counterfactual simulation engine  
- Real-data CGM pipeline (XML → CSV)  
- Decision-support framework  

---

## 🧪 Use Cases

- Personalized diabetes management  
- Clinical decision support systems  
- Research in causal ML for healthcare  
- Simulation-based treatment planning  

---

## 📁 Repository Structure

```
code/
├── train_pipeline.ipynb
├── test_pipeline.ipynb
├── sample_raw_xml/
├── sample_raw_csv/

figures/
├── Fig01–Fig19

paper/
├── PreviewPaper.pdf
```

---

## ⭐ Final Note

This project shifts AI from:

👉 Prediction → Decision-Aware Intelligence  

enabling real-world clinical decision support through simulation and causal reasoning.
