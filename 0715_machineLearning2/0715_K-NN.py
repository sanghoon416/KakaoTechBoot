from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# 유방암 데이터셋 로드
cancer = load_breast_cancer()
X, y = cancer.data, cancer.target

# 데이터셋을 학습 세트와 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 데이터 표준화
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# K-NN 모델 학습
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 예측 및 평가
y_pred = knn.predict(X_test)
print(classification_report(y_test, y_pred))

# 혼동 행렬 시각화
ConfusionMatrixDisplay.from_estimator(knn, X_test, y_test)
plt.title("K-NN Confusion Matrix")
plt.show()