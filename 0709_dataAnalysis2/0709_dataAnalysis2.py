import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''

'''

data = pd.read_csv('weather_classification_data.csv')

print(data.info())

print(data.head(8))

categorical = data.select_dtypes(include=['object', 'category']).columns
numerical = data.select_dtypes(include=['int64', 'float64']).columns

print("\nDescriptive Statistics for Numerical Data:\n", data[numerical].describe())

print("\nMissing Values:\n", data.isnull().sum())

# 상관계수 계산
correlation_matrix = data[numerical].corr()

# 상관계수 출력
print(correlation_matrix)

# 상관계수 히트맵 시각화
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()