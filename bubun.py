import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
one_hot = pd.DataFrame()


for val in data['whoAmI'].unique():
    one_hot[val] = (data['whoAmI'] == val)


print(data.head())
print(one_hot.head())

 

    

