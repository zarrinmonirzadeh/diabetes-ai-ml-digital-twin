# Diabetes AI/ML Digital Twin Framework

## 📌 Author: **Zarrin Monirzadeh**  Data Engineer | Software Engineer | **AI in Healthcare**  

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![ML](https://img.shields.io/badge/MachineLearning-Enabled-green)
![AI](https://img.shields.io/badge/AI-Healthcare--Focused-purple)
![Status](https://img.shields.io/badge/Status-Research--Prototype-orange)

A simulation-driven digital twin framework for diabetes that integrates machine learning, temporal modeling, and causal inference to support decision-oriented care.
---

## 🧠 Overview

This repository presents a **reproducible digital twin architecture** for modeling glucose dynamics in diabetes patients using Continuous Glucose Monitoring (CGM) data.

Unlike traditional predictive models, this framework enables:

- Simulation of interventions (diet, activity)
- Counterfactual outcome estimation
- Temporal glucose modeling
- Decision-support insights
- **AI-driven decision-support insights**

---

## ⚙️ Methodology

The framework combines:

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
## 🧪 Data Pipeline

Raw CGM XML → CSV → AI Modeling → Simulation

- XML samples: `code/sample_raw_xml/`
- CSV outputs: `code/sample_raw_csv/`
- Pipelines:
  - `train_pipeline.ipynb`
  - `test_pipeline.ipynb`

---

## 📊 Sample Outputs (Already Added)

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


pip install pandas numpy matplotlib scikit-learn
python code/demo_pipeline.py
Or run:

train_pipeline.ipynb
test_pipeline.ipynb


## 📊 Results & Visualizations

### 🔹 CGM Data & Clinical Representation

#### 📌 Fig 01 — Daily CGM Profile (Real Patient)
![Fig01](figures/Fig01.png)
Real glucose fluctuations over 24 hours, including hyperglycemia and hypoglycemia.

#### 📌 Fig 02 — Ambulatory Glucose Profile (AGP)
![Fig02](figures/Fig02.png)
Glucose distribution, variability, and time-in-range metrics.

#### 📌 Fig 03 — Same HbA1c, Different Dynamics
![Fig03](figures/Fig03.png)
Identical HbA1c can mask very different glucose variability patterns.

#### 📌 Fig 04 — Glucose Threshold Monitoring
![Fig04](figures/Fig04.png)
Safe range (70–180 mg/dL) and excursions beyond clinical limits.

---

### 🔹 Signal Processing & Temporal Modeling

#### 📌 Fig 05 — Smoothed CGM Signal
![Fig05](figures/Fig05.png)
Trend extraction with uncertainty estimation.

#### 📌 Fig 06 — 24-Hour CGM Trajectory
![Fig06](figures/Fig06.png)
Baseline time-series used for modeling and simulation.

---

### 🔹 Counterfactual Simulation

#### 📌 Fig 07 — Intervention Simulation
![Fig07](figures/Fig07.png)
Simulated effects of:
- Reduced carbohydrate intake
- Physical activity (walking)

#### 📌 Fig 08 — Real vs Counterfactual
![Fig08](figures/Fig08.png)
Observed CGM compared with simulated intervention outcomes.

#### 📌 Fig 09 — Clinical Sensitivity Analysis
![Fig09](figures/Fig09.png)
Response of physiological variables to glucose perturbations.

---

### 🔹 Causal Inference Framework

#### 📌 Fig 10 — Intervention vs Counterfactual
![Fig10](figures/Fig10.png)
Observed vs counterfactual trajectories after intervention.

#### 📌 Fig 11 — Difference-in-Differences (DiD)
![Fig11](figures/Fig11.png)
Estimation of intervention effect using causal inference.

---

### 🔹 Behavioral & Physiological Effects

#### 📌 Fig 12 — Activity Impact
![Fig12](figures/Fig12.png)
Glucose response under:
- Sitting
- Light activity
- Moderate activity

---

### 🔹 Model Evaluation & Behavior

#### 📌 Fig 13 — Model Comparison
![Fig13](figures/Fig13.png)
Baseline vs enhanced modeling performance.

#### 📌 Fig 14 — Linear vs Nonlinear Trends
![Fig14](figures/Fig14.png)
Illustrates limitations of linear assumptions in physiological systems.

#### 📌 Fig 15 — Glucose Envelope Modeling
![Fig15](figures/Fig15.png)
Captures uncertainty and physiological bounds.

---

### 🔹 Longitudinal & Stability Analysis

#### 📌 Fig 16 — Glucose Stability Zones
![Fig16](figures/Fig16.png)
Defines hypo-, normo-, and hyperglycemic regions.

#### 📌 Fig 17 — Longitudinal CGM (OhioT1DM)
![Fig17](figures/Fig17.png)
Multi-month glucose variability patterns.

---

### 🔹 Model Fitting & Trends

#### 📌 Fig 18 — Regression Fit
![Fig18](figures/Fig18.png)
Parameter estimation and model fitting example.

#### 📌 Fig 19 — Multi-Series Trends
![Fig19](figures/Fig19.png)
Comparison of multiple modeled trajectories.

---

## 💡 Key Contributions

This framework enables:

- Patient-specific digital twin modeling
- Simulation of treatment scenarios
- Causal inference for intervention effects
- Explainable AI for healthcare decision support
- AI-driven digital twin modeling
- Counterfactual simulation engine
- Causal inference integration
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
code/
├── train_pipeline.ipynb
├── test_pipeline.ipynb
├── sample_raw_xml/
├── sample_raw_csv/

figures/
├── Fig01–Fig19

paper/
├── PreviewPaper.pdf

---

⭐ Final Note

This project shifts AI from:

👉 Prediction → Decision-Aware Intelligence

enabling real-world clinical decision support through simulation and causal reasoning.
