from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

# 데이터 로드
california = fetch_california_housing()

X = california.data
Y = california.target

print(f"X: {X}")
print(f"Y: {Y}")

# 데이터 분할
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 랜덤 포레스트 모델 학습
rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)
rf_reg.fit(X_train, Y_train)

# 예측
Y_pred_rf = rf_reg.predict(X_test)

# 평가
mse_rf = mean_squared_error(Y_test, Y_pred_rf)
r2_rf = r2_score(Y_test, Y_pred_rf)

print(f'Random Forest Mean Squared Error: {mse_rf}')
print(f'Random Forest R^2 Score: {r2_rf}')

# 교차 검증 점수
scores = cross_val_score(rf_reg, X, Y, cv=5, scoring='r2')
print(f'Cross-validated R^2 scores: {scores}')
print(f'Average cross-validated R^2 score: {scores.mean()}')

plt.figure(figsize=(10, 6))
plt.scatter(Y_test, Y_pred_rf, color='blue', alpha=0.5, label='Predicted vs Actual')
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], 'k--', lw=2, label='Perfect Prediction')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Linear Regression: Actual vs Predicted')
plt.legend()
plt.show()