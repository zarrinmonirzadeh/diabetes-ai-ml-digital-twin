"""
Demo pipeline for the Diabetes AI/ML Digital Twin Framework.

This script provides a simplified, reproducible version of the modeling
and simulation workflow. The full implementation, extended experiments,
and complete data-processing pipeline are not publicly released.

Author: Zarrin Monirzadeh
"""

import math
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    accuracy_score,
    roc_auc_score,
)
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import (
    RandomForestRegressor,
    RandomForestClassifier,
    GradientBoostingRegressor,
    GradientBoostingClassifier,
)
from sklearn.neural_network import MLPRegressor, MLPClassifier


OUTDIR = "outputs"
RANDOM_STATE = 42

os.makedirs(OUTDIR, exist_ok=True)
np.random.seed(RANDOM_STATE)


# ============================================================
# 1. Benchmark regression experiment
# ============================================================

X, y = load_diabetes(return_X_y=True, as_frame=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=RANDOM_STATE,
)

regression_models = {
    "Linear Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearRegression()),
    ]),
    "Random Forest": RandomForestRegressor(
        n_estimators=300,
        random_state=RANDOM_STATE,
    ),
    "Gradient Boosting": GradientBoostingRegressor(
        random_state=RANDOM_STATE,
    ),
    "MLP": Pipeline([
        ("scaler", StandardScaler()),
        ("model", MLPRegressor(
            hidden_layer_sizes=(64, 32),
            max_iter=5000,
            random_state=RANDOM_STATE,
        )),
    ]),
}

regression_results = []

for name, model in regression_models.items():
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)

    regression_results.append({
        "Model": name,
        "MAE": round(mean_absolute_error(y_test, prediction), 2),
        "RMSE": round(math.sqrt(mean_squared_error(y_test, prediction)), 2),
        "R2": round(r2_score(y_test, prediction), 3),
    })

regression_df = (
    pd.DataFrame(regression_results)
    .sort_values("RMSE")
    .reset_index(drop=True)
)

regression_df.to_csv(
    f"{OUTDIR}/regression_results.csv",
    index=False,
)


# ============================================================
# 2. Derived binary classification benchmark
# ============================================================

y_binary = (y > y.median()).astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_binary,
    test_size=0.2,
    random_state=RANDOM_STATE,
    stratify=y_binary,
)

classification_models = {
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000)),
    ]),
    "Random Forest": RandomForestClassifier(
        n_estimators=300,
        random_state=RANDOM_STATE,
    ),
    "Gradient Boosting": GradientBoostingClassifier(
        random_state=RANDOM_STATE,
    ),
    "MLP": Pipeline([
        ("scaler", StandardScaler()),
        ("model", MLPClassifier(
            hidden_layer_sizes=(64, 32),
            max_iter=5000,
            random_state=RANDOM_STATE,
        )),
    ]),
}

classification_results = []

for name, model in classification_models.items():
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(X_test)[:, 1]
    else:
        probability = model.decision_function(X_test)

    classification_results.append({
        "Model": name,
        "Accuracy": round(accuracy_score(y_test, prediction), 3),
        "AUC": round(roc_auc_score(y_test, probability), 3),
    })

classification_df = (
    pd.DataFrame(classification_results)
    .sort_values("AUC", ascending=False)
    .reset_index(drop=True)
)

classification_df.to_csv(
    f"{OUTDIR}/classification_results.csv",
    index=False,
)


# ============================================================
# 3. Simplified counterfactual simulation
# ============================================================

minutes = np.arange(0, 121, 5)

baseline_meal = (
    110
    + 70 * np.exp(-((minutes - 55) ** 2) / (2 * 22 ** 2))
    + np.random.normal(0, 2, size=len(minutes))
)

reduced_carbs = (
    108
    + 45 * np.exp(-((minutes - 50) ** 2) / (2 * 20 ** 2))
    + np.random.normal(0, 2, size=len(minutes))
)

baseline_plus_walking = (
    109
    + 55 * np.exp(-((minutes - 52) ** 2) / (2 * 21 ** 2))
    - 10 * (1 / (1 + np.exp(-(minutes - 70) / 8)))
    + np.random.normal(0, 2, size=len(minutes))
)

counterfactual_df = pd.DataFrame({
    "minutes": minutes,
    "baseline_meal_60g": baseline_meal,
    "reduced_carbs_30g": reduced_carbs,
    "baseline_plus_walking": baseline_plus_walking,
})

counterfactual_df.to_csv(
    f"{OUTDIR}/counterfactual_trajectories.csv",
    index=False,
)

summary_df = pd.DataFrame([
    {
        "Scenario": "Baseline meal (60 g)",
        "Peak Glucose": round(baseline_meal.max(), 0),
        "Time in Range (%)": round(
            np.mean((baseline_meal >= 70) & (baseline_meal <= 180)) * 100,
            0,
        ),
    },
    {
        "Scenario": "Reduced carbohydrates (30 g)",
        "Peak Glucose": round(reduced_carbs.max(), 0),
        "Time in Range (%)": round(
            np.mean((reduced_carbs >= 70) & (reduced_carbs <= 180)) * 100,
            0,
        ),
    },
    {
        "Scenario": "Baseline plus walking",
        "Peak Glucose": round(baseline_plus_walking.max(), 0),
        "Time in Range (%)": round(
            np.mean((baseline_plus_walking >= 70) & (baseline_plus_walking <= 180)) * 100,
            0,
        ),
    },
])

summary_df.to_csv(
    f"{OUTDIR}/counterfactual_summary.csv",
    index=False,
)


# ============================================================
# 4. Generate demonstration figure
# ============================================================

plt.figure(figsize=(6, 4))

plt.plot(
    counterfactual_df["minutes"],
    counterfactual_df["baseline_meal_60g"],
    label="Baseline meal (60g)",
    linewidth=2,
)

plt.plot(
    counterfactual_df["minutes"],
    counterfactual_df["reduced_carbs_30g"],
    label="Reduced carbs (30g)",
    linewidth=2,
)

plt.plot(
    counterfactual_df["minutes"],
    counterfactual_df["baseline_plus_walking"],
    label="Baseline + walking",
    linewidth=2,
)

plt.xlabel("Time (minutes)")
plt.ylabel("Glucose (mg/dL)")
plt.title("Counterfactual Glucose Trajectories")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig(
    f"{OUTDIR}/counterfactual_plot.png",
    dpi=300,
)

plt.close()


# ============================================================
# 5. Output summary
# ============================================================

print("\nRegression Results")
print(regression_df)

print("\nClassification Results")
print(classification_df)

print("\nCounterfactual Summary")
print(summary_df)

print("\nGenerated files:")
for filename in os.listdir(OUTDIR):
    print(f"- {filename}")
