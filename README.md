# Diabetes AI/ML Digital Twin Framework

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![ML](https://img.shields.io/badge/MachineLearning-Enabled-green)
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

---

## ⚙️ Methodology

The framework combines:

### 🔹 Machine Learning
- Regression-based prediction
- Feature-driven modeling

### 🔹 Time-Series Modeling
- CGM trajectory representation
- Temporal dynamics capture

### 🔹 Causal Inference
- Counterfactual reasoning
- Difference-in-Differences (DiD)

### 🔹 Simulation Engine
- Intervention-based trajectory generation

---

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

---

## 🧪 Use Cases

- Personalized diabetes management
- Clinical decision support systems
- Research in causal ML for healthcare
- Simulation-based treatment planning

---

## 📁 Repository Structure

---

## 🚀 Future Work

- Deep learning temporal models (LSTM / Transformers)
- Reinforcement learning for insulin optimization
- Real-time digital twin deployment
- Integration with wearable devices

---

## 📌 Author

**Zarrin Monirzadeh**  
Data Engineer | Software Engineer | AI in Healthcare  

---

## ⭐ Final Note

TThis work advances the paradigm from predictive AI to decision-aware AI, integrating machine learning with causal inference and simulation to enable intervention-driven analysis and personalized decision support in healthcare.
