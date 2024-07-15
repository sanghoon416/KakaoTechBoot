import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from math import pi
import plotly.graph_objects as go

# 데이터 불러오기
file_path = 'weather_classification_data.csv'
data = pd.read_csv(file_path)

# 상관 행렬 계산
correlation_matrix = data[['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)', 
                           'Atmospheric Pressure', 'UV Index', 'Visibility (km)']].corr()

# 히트맵 생성
# 모든 변수들에 대해서 히트맵
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Weather Variables Correlation Heatmap')
plt.show()




# 트리맵 생성
# location 별로 weather type 의 비율을 알아보는 트리맵
grouped_data = data.groupby(['Location', 'Weather Type']).size().reset_index(name='Count')

fig = px.treemap(grouped_data, path=['Location', 'Weather Type'], values='Count', 
                 color='Count', color_continuous_scale='RdBu', 
                 title='Weather Type Distribution by Location')
fig.show()

# 버블차트 생성
# 온도, 습도, 풍속으로 버블차트 생성
x = data['Temperature']
y = data['Humidity']
sizes = data['Wind Speed'] * 5  
alpha = 0.4  

# 버블차트 생성
plt.figure(figsize=(12, 8))
plt.scatter(x, y, s=sizes, alpha=alpha, c=sizes, cmap='viridis')
plt.colorbar(label='Wind Speed')
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.title('Bubble Chart: Temperature vs Humidity vs Wind Speed')
plt.show()

'''
원의 크기와 투명도를 추가하지 않았을 때는 상당히 알아보기 어려운 버블차트가 나왔는 데
사이즈와 투명도를 조절해서 조금 더 보기 쉬운 차트를 만들 수 있었다.
그리고 그 결과로 어제 데이터셋에 이상함을 느끼는 게 맞았음을 알 수 있었다.
상당히 인위적인 데이터 값이 어마어마하게 많이 들어가 있었다.
'''

categories = ['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)', 'UV Index', 'Visibility (km)']
values = data[categories].mean().tolist()

# 레이더 차트 데이터를 원형으로 배열하기 위해 마지막에 첫 번째 값 추가
values += values[:1]

# 레이더 차트 생성
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# 각 변수에 대한 각도 계산
angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
angles += angles[:1]

# 레이더 차트 그리기
ax.plot(angles, values, linewidth=1, linestyle='solid')
ax.fill(angles, values, 'b', alpha=0.1)

# 카테고리 라벨 설정
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# 차트 제목 설정
plt.title('Average Weather Conditions')

plt.show()

grouped_data = data.groupby(['Location', 'Weather Type']).size().reset_index(name='Count')

# 노드 및 링크 데이터 준비
locations = grouped_data['Location'].unique().tolist()
weather_types = grouped_data['Weather Type'].unique().tolist()

# 노드 리스트 생성
nodes = locations + weather_types

# 노드 인덱스 매핑
node_indices = {node: i for i, node in enumerate(nodes)}

# 링크 데이터 생성
source_indices = grouped_data['Location'].map(node_indices).tolist()
target_indices = grouped_data['Weather Type'].map(node_indices).tolist()
values = grouped_data['Count'].tolist()

# 생키 다이어그램 생성
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=nodes
    ),
    link=dict(
        source=source_indices,
        target=target_indices,
        value=values
    ))])

fig.update_layout(title_text="Weather Type Distribution by Location", font_size=10)
fig.show()
