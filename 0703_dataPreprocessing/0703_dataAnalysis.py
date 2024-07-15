import pandas as pd

data = pd.read_csv('customer_purchase_data.csv')

#데이터 정보 확인
data.info()

#상위 n개의 데이터 샘플 확인
print(data.head(5))

#평균, 최빈값 등등의 데이터 기초 통게 확인
print(data.describe())

#결측값 확인
missing_values = data.isnull().sum()
print("Missing values in each column:\n", missing_values)

#결측값 처리 (평균값으로 대체)
data['Age'].fillna(data['Age'].mean(), inplace=True)

#결측값 처리 (최빈값으로 대체)
data['Gender'].fillna(data['Gender'].mode()[0], inplace=True)

#코랩 주소
#https://colab.research.google.com/drive/1NdEyXIoSlJnb0pWCJLT5Wu1pnvMk8U_D?usp=sharing#scrollTo=DDEZzDKMUY6U