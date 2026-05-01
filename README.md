# Diabetes AI/ML Digital Twin Framework

**Zarrin Monirzadeh**  
Data Engineer | Software Engineer | AI in Healthcare  

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

## 📄 Paper

A condensed preview of the manuscript is included:

📄 [View Preview](paper/PreviewPaper.pdf)

The full version, including extended experiments, full dataset analysis, and technical derivations, is available upon request for academic or research purposes.

📧 **Request access:** monirzadehzarrin@gmail.com

---

## 🧪 Data Pipeline

This repository includes a reproducible pipeline from **raw CGM XML → structured CSV → modeling → simulation outputs**.

### Step 1 — Raw Data (XML)

```

code/sample_raw_xml/

```

### Step 2 — Structured CSV

```

code/sample_raw_csv/

````

### Step 3 — Modeling

- Regression (glucose prediction)
- Classification (glucose states)
- Temporal modeling

### Step 4 — Counterfactual Simulation

- Reduced carbohydrate intake
- Physical activity (walking)
- Scenario-based trajectory generation

### Step 5 — Outputs

- regression_results.csv  
- classification_results.csv  
- counterfactual_trajectories.csv  
- counterfactual_summary.csv  

---

## ▶️ How to Run

### Run notebooks:

- code/train_pipeline.ipynb  
- code/test_pipeline.ipynb  

### Or run script:

```bash
python code/demo_pipeline.py
````

### Install dependencies:

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## 📊 Results & Visualizations

### 🔹 CGM Data & Clinical Representation

#### Fig 01 — Daily CGM Profile

![Fig01](figures/Fig01.png)

#### Fig 02 — Ambulatory Glucose Profile

![Fig02](figures/Fig02.png)

#### Fig 03 — Same HbA1c, Different Dynamics

![Fig03](figures/Fig03.png)

#### Fig 04 — Glucose Threshold Monitoring

![Fig04](figures/Fig04.png)

---

### 🔹 Signal Processing & Temporal Modeling

#### Fig 05 — Smoothed CGM Signal

![Fig05](figures/Fig05.png)

#### Fig 06 — 24-Hour CGM Trajectory

![Fig06](figures/Fig06.png)

---

### 🔹 Counterfactual Simulation

#### Fig 07 — Intervention Simulation

![Fig07](figures/Fig07.png)

#### Fig 08 — Real vs Counterfactual

![Fig08](figures/Fig08.png)

#### Fig 09 — Clinical Sensitivity Analysis

![Fig09](figures/Fig09.png)

---

### 🔹 Causal Inference Framework

#### Fig 10 — Intervention vs Counterfactual

![Fig10](figures/Fig10.png)

#### Fig 11 — Difference-in-Differences (DiD)

![Fig11](figures/Fig11.png)

---

### 🔹 Behavioral & Physiological Effects

#### Fig 12 — Activity Impact

![Fig12](figures/Fig12.png)

---

### 🔹 Model Evaluation & Behavior

#### Fig 13 — Model Comparison

![Fig13](figures/Fig13.png)

#### Fig 14 — Linear vs Nonlinear Trends

![Fig14](figures/Fig14.png)

#### Fig 15 — Glucose Envelope Modeling

![Fig15](figures/Fig15.png)

---

### 🔹 Longitudinal & Stability Analysis

#### Fig 16 — Glucose Stability Zones

![Fig16](figures/Fig16.png)

#### Fig 17 — Longitudinal CGM (OhioT1DM)

![Fig17](figures/Fig17.png)

---

### 🔹 Model Fitting & Trends

#### Fig 18 — Regression Fit

![Fig18](figures/Fig18.png)

#### Fig 19 — Multi-Series Trends

![Fig19](figures/Fig19.png)

---

## 💡 Key Contributions

* Patient-specific digital twin modeling
* Simulation of treatment scenarios
* Causal inference for intervention effects
* Explainable AI for healthcare decision support
* End-to-end pipeline from raw XML → simulation outputs

---

## 🧪 Use Cases

* Personalized diabetes management
* Clinical decision support systems
* Research in causal ML for healthcare
* Simulation-based treatment planning

---

## 📁 Repository Structure

```
code/
├── train_pipeline.ipynb
├── test_pipeline.ipynb
├── demo_pipeline.py
├── sample_raw_xml/
├── sample_raw_csv/
├── *.csv results

figures/
├── Fig01–Fig19

paper/
├── PreviewPaper.pdf
├── PreviewPaper.tex
```

---

## 🚀 Future Work

* Deep learning temporal models (LSTM / Transformers)
* Reinforcement learning for insulin optimization
* Real-time digital twin deployment
* Integration with wearable devices

---

## 📌 Author

**Zarrin Monirzadeh**
Data Engineer | Software Engineer | AI in Healthcare

📧 [monirzadehzarrin@gmail.com](mailto:monirzadehzarrin@gmail.com)

---

## ⭐ Final Note

This work advances the paradigm from predictive AI to decision-aware AI, transforming machine learning systems from passive forecasting tools into active decision-support frameworks through the integration of causal inference and counterfactual simulation in healthcare.

```

---

If something still breaks after you paste (images, paths, etc.), tell me — I’ll fix it precisely.
```
