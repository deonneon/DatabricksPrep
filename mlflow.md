# MLFlow

## Python Example Code

```py
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

# set the experiment id
mlflow.set_experiment(experiment_id="3480141376382286")

mlflow.autolog()
db = load_diabetes()

X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

# Create and train models.
rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
rf.fit(X_train, y_train)

# Use the model to make predictions on the test dataset.
predictions = rf.predict(X_test)
```

## Process

Data Handling: The script uses the diabetes dataset and splits it into training and test sets, which is a common practice in machine learning to evaluate model performance.

Model Training: A random forest regressor is configured with specific hyperparameters and trained on the data, after which it makes predictions on unseen test data.

MLflow Integration: The use of mlflow.set_experiment and mlflow.autolog() ensures that every detail of the model training (like hyperparameters and performance metrics) is automatically recorded. This is especially useful for experiment tracking and reproducibility.
