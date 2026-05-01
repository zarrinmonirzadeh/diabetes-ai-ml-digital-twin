# Diabetes AI/ML Digital Twin Framework

A simulation-driven digital twin framework for diabetes that integrates machine learning, temporal modeling, and causal inference to support decision-oriented care.

---

## 🧠 Overview

This repository presents a reproducible digital twin architecture for modeling glucose dynamics in diabetes patients using Continuous Glucose Monitoring (CGM) data.

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

## 📄 Paper

A condensed version of the manuscript is provided for reference:

📄 [View Preview](paper/PreviewPaper.pdf)

The complete paper, including extended experiments and full technical details, is available upon request for research or academic purposes.

For access inquiries:

📧 monirzadehzarrin@gmail.com

---

## 📊 Results & Visualizations

### 🔹 CGM Data & Clinical Representation

#### 📌 Fig 01 — Daily CGM Profile (Real Patient)
Real glucose fluctuations over 24 hours, including hyperglycemia and hypoglycemia.

#### 📌 Fig 02 — Ambulatory Glucose Profile (AGP)
Glucose distribution, variability, and time-in-range metrics.

#### 📌 Fig 03 — Same HbA1c, Different Dynamics
Identical HbA1c can mask very different glucose variability patterns.

#### 📌 Fig 04 — Glucose Threshold Monitoring
Safe range (70–180 mg/dL) and excursions beyond clinical limits.

---

### 🔹 Signal Processing & Temporal Modeling

#### 📌 Fig 05 — Smoothed CGM Signal
Trend extraction with uncertainty estimation.

#### 📌 Fig 06 — 24-Hour CGM Trajectory
Baseline time-series used for modeling and simulation.

---

### 🔹 Counterfactual Simulation

#### 📌 Fig 07 — Intervention Simulation
Simulated effects of:
- Reduced carbohydrate intake
- Physical activity (walking)

#### 📌 Fig 08 — Real vs Counterfactual
Observed CGM compared with simulated intervention outcomes.

#### 📌 Fig 09 — Clinical Sensitivity Analysis
Response of physiological variables to glucose perturbations.

---

### 🔹 Causal Inference Framework

#### 📌 Fig 10 — Intervention vs Counterfactual
Observed vs counterfactual trajectories after intervention.

#### 📌 Fig 11 — Difference-in-Differences (DiD)
Estimation of intervention effect using causal inference.

---

### 🔹 Behavioral & Physiological Effects

#### 📌 Fig 12 — Activity Impact
Glucose response under:
- Sitting
- Light activity
- Moderate activity

---

### 🔹 Model Evaluation & Behavior

#### 📌 Fig 13 — Model Comparison
Baseline vs enhanced modeling performance.

#### 📌 Fig 14 — Linear vs Nonlinear Trends
Illustrates limitations of linear assumptions in physiological systems.

#### 📌 Fig 15 — Glucose Envelope Modeling
Captures uncertainty and physiological bounds.

---

### 🔹 Longitudinal & Stability Analysis

#### 📌 Fig 16 — Glucose Stability Zones
Defines hypo-, normo-, and hyperglycemic regions.

#### 📌 Fig 17 — Longitudinal CGM (OhioT1DM)
Multi-month glucose variability patterns.

---

### 🔹 Model Fitting & Trends

#### 📌 Fig 18 — Regression Fit
Parameter estimation and model fitting example.

#### 📌 Fig 19 — Multi-Series Trends
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

(To be completed based on project organization)

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

📧 monirzadehzarrin@gmail.com

---

## ⭐ Final Note

This work advances the paradigm from predictive AI to decision-aware AI,  
transforming machine learning systems from passive forecasting tools into  
active decision-support frameworks through the integration of causal inference  
and counterfactual simulation in healthcare.
