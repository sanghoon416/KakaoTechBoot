import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('weather_classification_data.csv')

data.info()

print(data.head(10))

# 막대그래프
season_temp_data = data[['Season', 'Temperature']]
average_temp_by_season = season_temp_data.groupby('Season').mean().reset_index()
season_order = ['Spring', 'Summer', 'Autumn', 'Winter']
average_temp_by_season['Season'] = pd.Categorical(average_temp_by_season['Season'], categories=season_order, ordered=True)
average_temp_by_season = average_temp_by_season.sort_values('Season')

plt.figure(figsize=(10, 6))
plt.bar(average_temp_by_season['Season'], average_temp_by_season['Temperature'], color='skyblue')
plt.title('Average Temperature by Season')
plt.xlabel('Season')
plt.ylabel('Average Temperature (°C)')
plt.show()

'''
계절 별로 온도를 막대그래프로 나태냈다.
막대그래프의 결과로 summer, winter 의 온도는 차이가 나지만 spring, autumn, summer 의 
온도는 차이가 나지 않는다. 아마도 이상치가 존재하는 것 같아서 박스플롯을 먼저 진행해 이상치를 확인해보겠다.
'''

# 박스플롯
plt.figure(figsize=(10, 6))
plt.boxplot(
    [data[data['Season'] == season]['Temperature'] for season in season_order],
    labels=season_order,
    patch_artist=True,
    boxprops=dict(facecolor='skyblue')
)
plt.title('Temperature Distribution by Season')
plt.xlabel('Season')
plt.ylabel('Temperature (°C)')
plt.show()

'''
박스플롯을 이용하여 25, 50, 75 퍼센트에 위치한 값과 이상치들을 확인했는 데
우선 spring, summer, autumn 에 비슷한 값을 갖는 다는 것을 확인했다.
여기까지 하고 느낀건데 location 이 존재하고 내륙, 산, 연안이 나누어져있어서 
이런식의 데이터 분석은 의미가 없는 것 같기는 하지만 그래도 겨울은 값이 낮은 게
눈에 보이는 데 여름은 왜 값이 낮지 않은 건지 궁금하긴 하다.
'''

spring_data = data[data['Season'] == 'Spring'].groupby('Location')['Temperature'].mean()
summer_data = data[data['Season'] == 'Summer'].groupby('Location')['Temperature'].mean()
autumn_data = data[data['Season'] == 'Autumn'].groupby('Location')['Temperature'].mean()
winter_data = data[data['Season'] == 'Winter'].groupby('Location')['Temperature'].mean()

plt.figure(figsize=(10, 6))

plt.plot(spring_data.index, spring_data.values, marker='o', color='pink', label='Spring')
plt.plot(summer_data.index, summer_data.values, marker='o', color='red', label='Summer')
plt.plot(autumn_data.index, autumn_data.values, marker='o', color='brown', label='Autumn')
plt.plot(winter_data.index, winter_data.values, marker='o', color='blue', label='Winter')
plt.title('Average Temperature by Location for Seasons')
plt.xlabel('Location')
plt.ylabel('Average Temperature (°C)')
plt.ylim(0, 40)
plt.yticks(range(0, 41, 5))
plt.legend()
plt.show()

'''
여름 혹은 겨울의 값에 대해서 알아보고 싶어서 선 그래프로 각 지역 별로 계절에 따른 온도를 알아보려고 했는데
결과가 마음에 안들기는 한다. 일단 데이터셋을 들고 온 입장에서는 온도에 큰 의미를 두지 않고 만든 것 같다.
그럼에도 나름의 결론을 조금 내보자면 겨울만 추운 곳인데 해안가는 사계절이 뚜렷하게 남지 않는 지역인 것 같다.
'''

# 히스토그램

# 파이차트

# 산점도
