
# Load birth data
from pandas import Series
series = Series.from_csv('dates_birth.csv', header=0)
print(series.head())