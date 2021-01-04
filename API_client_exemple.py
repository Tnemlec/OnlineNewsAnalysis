import pandas as pd
import requests
from sklearn.metrics import accuracy_score

# First let's load data from our dataset

data = pd.read_csv('OnlineNewsPopularity.csv', encoding='UTF-8')

# Now I will do a part of the cleaning on the data

data.columns = data.columns.str.strip()
data = data.drop(['url','timedelta'], axis=1)

y = data.pop('shares')
X = data

# I will create the y classes

def converter(x):
    x.astype(str)
    for index, value in x.items():
        if int(value) >= 1500:
            x[index] = 'popular'
        else:
            x[index] = 'unpopular'
    return x

y = converter(y)

# Now let's create a subsample of our data

X_sub = X.iloc[:4000, :]
y_sub = y.iloc[:4000]

# We can now send request to our API

host = 'localhost'
port=80

res = requests.post('http://localhost:80/api/submit', json = X_sub.to_json())

result = res.json()

# The result is an array containing the class, wether it is popular or not

print('Accuracy of the model : ' + str(accuracy_score(y_sub, result)))