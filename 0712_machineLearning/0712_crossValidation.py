import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_diabetes

# 데이터 로드
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

print(X)
print(y)

# 모델 생성
nb = GaussianNB()

# 교차 검증
scores = cross_val_score(nb, X, y, cv=5)

print(f'Cross-validation scores: {scores}')
print(f'Mean CV Score: {np.mean(scores)}')

# 시각화
plt.plot(range(1, len(scores) + 1), scores, marker='o', linestyle='--', color='b')
plt.xlabel('Fold')
plt.ylabel('Accuracy')
plt.title('Cross-Validation Scores')
plt.show()