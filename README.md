# Diabetes AI/ML Digital Twin Framework

A simulation-driven digital twin framework for diabetes that integrates machine learning, temporal modeling, and counterfactual analysis to support decision-oriented care.

---

## Overview
This repository provides a reproducible implementation of a digital twin architecture for diabetes modeling. The framework moves beyond prediction by enabling simulation of intervention scenarios such as dietary changes and physical activity, allowing structured comparison of potential outcomes.

The approach combines:
- Predictive modeling (regression and classification)
- Temporal data representation
- Counterfactual simulation
- Decision-support analysis

## 📊 Results & Visualizations

### 📌 Fig 01 — Daily CGM Profile (Real Patient)
![Fig01](figures/Fig01.png)

Shows real glucose fluctuations over a 24-hour period, including hyperglycemic and hypoglycemic episodes.

---

### 📌 Fig 02 — Ambulatory Glucose Profile (AGP)
![Fig02](figures/Fig02.png)

Summarizes glucose distribution, variability, and time-in-range statistics.

---

### 📌 Fig 03 — Same HbA1c, Different Glucose Dynamics
![Fig03](figures/Fig03.png)

Illustrates how two patients can have identical HbA1c but very different glucose variability.

---

### 📌 Fig 04 — Glucose Threshold Monitoring
![Fig04](figures/Fig04.png)

Highlights safe range boundaries (70–180 mg/dL) and excursions beyond them.

---

### 📌 Fig 05 — Smoothed CGM Signal with Trend
![Fig05](figures/Fig05.png)

Combines raw CGM signal with trend estimation and uncertainty.

---

### 📌 Fig 06 — 24-Hour CGM Trajectory
![Fig06](figures/Fig06.png)

Baseline time-series used for modeling and simulation.

---

### 📌 Fig 07 — Counterfactual Glucose Simulation
![Fig07](figures/Fig07.png)

Simulates interventions:
- Reduced carbohydrates
- Walking effect

---

### 📌 Fig 08 — Real vs Counterfactual Trajectories
![Fig08](figures/Fig08.png)

Compares observed CGM with simulated intervention outcomes.

---

### 📌 Fig 09 — Clinical Feature Sensitivity Analysis
![Fig09](figures/Fig09.png)

Evaluates how physiological variables respond to glucose perturbations.

---

### 📌 Fig 10 — Intervention vs Counterfactual Framework
![Fig10](figures/Fig10.png)

Core causal concept:
Observed vs counterfactual trajectories after intervention.

---

### 📌 Fig 11 — Difference-in-Differences (DiD)
![Fig11](figures/Fig11.png)

Estimates intervention effect using causal inference.

---

### 📌 Fig 12 — Activity Impact on Glucose
![Fig12](figures/Fig12.png)

Compares:
- Sitting
- Light activity
- Moderate activity

---

### 📌 Fig 13 — Model Behavior (Classic vs Improved)
![Fig13](figures/Fig13.png)

Comparison of baseline vs enhanced modeling approach.

---

### 📌 Fig 14 — Linear vs Nonlinear Trends
![Fig14](figures/Fig14.png)

Demonstrates limitations of linear modeling in physiological systems.

---

### 📌 Fig 15 — Glucose Envelope / Range Modeling
![Fig15](figures/Fig15.png)

Captures uncertainty and physiological bounds.

---

### 📌 Fig 16 — Glucose Stability Zones
![Fig16](figures/Fig16.png)

Defines:
- Hypoglycemia
- Normal range
- Hyperglycemia

---

### 📌 Fig 17 — Longitudinal CGM (OhioT1DM)
![Fig17](figures/Fig17.png)

Long-term variability across months.

---

### 📌 Fig 18 — Regression Fit Example
![Fig18](figures/Fig18.png)

Illustrates model fitting and parameter estimation.

---

### 📌 Fig 19 — Multi-Series Trend Comparison
![Fig19](figures/Fig19.png)

Comparison of multiple modeled trajectories.

---

## 📊 Key Insight

This framework enables:

- Predictive modeling of glucose
- Simulation of interventions (diet, activity)
- Causal inference (treatment effects)
- Digital twin representation of patient physiology
---

## Repository Structure
