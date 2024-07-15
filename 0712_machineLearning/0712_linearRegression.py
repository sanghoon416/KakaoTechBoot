import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 회귀 분석
from sklearn.datasets import fetch_california_housing

# 데이터 로드
california = fetch_california_housing()

X = california.data
Y = california.target

print(f"X: {X}")
print(f"Y: {Y}")

# 데이터 분할
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 모델 학습
lin_reg = LinearRegression()
lin_reg.fit(X_train, Y_train)

# 예측
Y_pred = lin_reg.predict(X_test)

# 평가
mse = mean_squared_error(Y_test, Y_pred)    # 평균제곱오차
r2 = r2_score(Y_test, Y_pred)               # 결정계수

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# 시각화
plt.figure(figsize=(10, 6))
plt.scatter(Y_test, Y_pred, color='blue', alpha=0.5, label='Predicted vs Actual')
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], 'k--', lw=2, label='Perfect Prediction')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Linear Regression: Actual vs Predicted')
plt.legend()
plt.show()

'''
우선은 선형 회귀를 이용하여 시각화까지 진행해보기는 했지만 R^2 값이 0.55 정도로 적합하지 않은 분석 방식인 것 같다.
남은 실습 문제들을 모두 진행해보고 다른 방식으로 접근해보겠다.
'''

