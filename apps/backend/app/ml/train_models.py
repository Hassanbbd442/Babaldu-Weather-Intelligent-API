import joblib
import pandas as pd





from sklearn.model_selection import (
    train_test_split
)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from sklearn.ensemble import (
    RandomForestRegressor
)

from sklearn.linear_model import (
    LinearRegression
)

from xgboost import XGBRegressor

# =========================
# LOAD DATASET
# =========================

DATASET_PATH = (
    "../../models/datasets/babaldu_weather.csv"
)

df = pd.read_csv(DATASET_PATH)

# =========================
# FEATURES
# =========================

FEATURE_COLUMNS = [

    "temp_max",
    "temp_min",
    "temp_mean",

    "rainfall",

    "wind_speed",

    "humidity",

    "pressure",

    "cloud_cover",

    "temp_mean_lag1",

    "rainfall_lag1",

    "temp_rolling_3",

    "rainfall_rolling_3"
]

# =========================
# TARGET
# =========================

TARGET_COLUMN = "target_temp_t1"

X = df[FEATURE_COLUMNS]

y = df[TARGET_COLUMN]

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,

        test_size=0.2,

        random_state=42,

        shuffle=False
    )
)

# =========================
# MODELS
# =========================

models = {

    "RandomForest": RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ),

    "LinearRegression": LinearRegression(),

    "XGBoost": XGBRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=6,
        random_state=42
    )
}

# =========================
# TRAINING LOOP
# =========================

best_model = None
best_rmse = float("inf")

for name, model in models.items():

    print(f"\nTraining {name}...\n")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = mean_squared_error(
        y_test,
        predictions
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    print(f"{name} Results")

    print(f"MAE  : {mae:.3f}")

    print(f"RMSE : {rmse:.3f}")

    print(f"R²   : {r2:.3f}")

    # Save best model
    if rmse < best_rmse:

        best_rmse = rmse

        best_model = model

        best_model_name = name

# =========================
# SAVE BEST MODEL
# =========================

MODEL_OUTPUT_PATH = (
    "../../models/trained/"
    "best_temperature_model.pkl"
)

joblib.dump(
    best_model,
    MODEL_OUTPUT_PATH
)

print("\n===================")

print(
    f"Best Model: {best_model_name}"
)

print(
    f"Best RMSE : {best_rmse:.3f}"
)

print("===================\n")

print(
    "Model saved successfully."
)