import pandas as pd

# 데이터셋 로드
data = pd.read_csv('HeartDiseaseTrain-Test.csv')

# 데이터의 처음 몇 줄을 출력하여 구조 확인
print("#"*10)
print("데이터의 처음 몇 줄을 출력하여 구조 확인")
print(data.head())

# 데이터의 각 컬럼에 대한 정보 확인
print("#"*10)
print("데이터의 각 컬럼에 대한 정보 확인")
print(data.info())

# 데이터 타입 확인
print("#"*10)
print("데이터 타입 확인")
print("Data Types:\n", data.dtypes)

# 범주형 및 수치형 데이터 분리하여 분석
categorical_cols = data.select_dtypes(include=['object', 'category']).columns
numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns

print("#"*10)
print("범주형 데이터 분리하여 분석")
print("\nCategorical Columns:\n", categorical_cols)

print("#"*10)
print("수치형 데이터 분리하여 분석")
print("\nNumerical Columns:\n", numerical_cols)

# 결측치 확인
print("\nMissing Values:\n", data.isnull().sum())

# 각 범주형 변수의 유니크한 값과 빈도수
for col in categorical_cols:
    print(f"\nUnique values in {col}:\n", data[col].value_counts())

# 수치형 데이터의 기초 통계
print("\nDescriptive Statistics for Numerical Data:\n", data[numerical_cols].describe())