import pandas as pd

data = [
        ['D1', 'Sunny','Hot', 'High', 'Weak', 'No'],
        ['D2', 'Sunny','Hot', 'High', 'Strong', 'No'],
        ['D3', 'Overcast','Hot', 'High', 'Weak', 'Yes'],
        ['D4', 'Rain','Mild', 'High', 'Weak', 'Yes'],
        ['D5', 'Rain','Cool', 'Normal', 'Weak', 'Yes'],
        ['D6', 'Rain','Cool', 'Normal', 'Strong', 'No'],
        ['D7', 'Overcast','Cool', 'Normal', 'Strong', 'Yes'],
        ['D8', 'Sunny','Mild', 'High', 'Weak', 'Yes'],
        ['D9', 'Sunny','Cool', 'Normal', 'Weak', 'No'],
        ['D10', 'Rain','Mild', 'Normal', 'Weak', 'Yes'],
        ['D11', 'Sunny','Mild', 'Normal', 'Strong', 'Yes'],
        ['D12', 'Overcast','Mild', 'High', 'Strong', 'No'],
        ['D13', 'Overcast','Hot', 'Normal', 'Weak', 'Yes'],
        ['D14', 'Rain','Mild', 'High', 'Strong', 'No'],
       ]



df = pd.DataFrame(data, columns=['day', 'outlook', 'temp', 'humidity', 'windy', 'play'])

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()

df['outlook'] = lb.fit_transform(df['outlook'])
df['temp'] = lb.fit_transform(df['temp'])
df['humidity'] = lb.fit_transform(df['humidity'])
df['windy'] = lb.fit_transform(df['windy'])
df['play'] = lb.fit_transform(df['play'])

print("\nTRANSFORM\n--------------------------\n")
print(df)

print("\nDESCRIBE\n--------------------------\n")
print(df.describe())  # tablonun genel tanımlayıcı istatistik değerlerini verir
