import pandas as pd

data = pd.read_csv('Travel details dataset.csv')

#데이터 종류, 속성 확인
print(data.info())

#데이터 구조 확인
print(data.head(5))

# Transportation cost 에 대해서 object -> int 형 변환
data['Transportation cost'] = data['Transportation cost'].replace('[\$,a-zA-Z]', '', regex=True)
data['Transportation cost'].fillna('0', inplace=True)
data['Transportation cost'] = data['Transportation cost'].astype(int)

# Accommodation cost 에 대해서 object -> int 형 변환
data['Accommodation cost'] = data['Accommodation cost'].replace('[\$,a-zA-Z]', '', regex=True)
data['Accommodation cost'].fillna('0', inplace=True)
data['Accommodation cost'] = data['Accommodation cost'].astype(int)

#범주형 데이터, 연속형 데이터 식별
categorical_cols = data.select_dtypes(include=['object', 'category']).columns
numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns

# 각 범주형 변수의 유니크한 값과 빈도수
for col in categorical_cols:
    print(f"\nUnique values in {col}:\n", data[col].value_counts())

# 수치형 데이터의 기초 통계
print("\nDescriptive Statistics for Numerical Data:\n", data[numerical_cols].describe())

# 결측치 확인
print("\nMissing Values:\n", data.isnull().sum())

# 데이터 중복 확인
duplicates = data.duplicated()
print("데이터 중복 확인 : ", duplicates.sum())

# 결측치가 존재하는 인덱스 확인
missing_rows = data[data.isnull().any(axis=1)]
print(missing_rows)

# 결측치가 있는 곳이 3곳 밖에 없기 때문에 삭제
data_cleaned = data.dropna()

# 결측치 재확인
print("\nMissing Values:\n", data_cleaned.isnull().sum())

# 왜도(Skewness): 0에 가까울수록 정규분포에 근사, 양의 값은 오른쪽 꼬리가 긴 분포(왼쪽으로 치우친), 음의 값은 왼쪽 꼬리가 긴 분포(오른쪽으로 치우친)
print("\nSkewness of the data:\n", data[numerical_cols].skew())

# 첨도(Kurtosis): 0에 가까울수록 정규분포에 근사, 높으면 분포가 뾰족하고, 낮으면 평평
print("\nKurtosis of the data:\n", data[numerical_cols].kurt())

# 피어슨 상관 계수
print("Pearson Correlation:\n", data[numerical_cols].corr(method='pearson'))

# 스피어만 상관 계수
print("\nSpearman Correlation:\n", data[numerical_cols].corr(method='spearman'))
