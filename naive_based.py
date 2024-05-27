import numpy as np 
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd 

data=np.array([['valve','crosby'], 
               ['valve', 'kit'], 
               ['disc', 'valve'], 
               ['transmitter', 'rosemount'], 
               ['temperature', 'sensor']
               ])

data_strings = [' '.join(row) for row in data]

output =['fc','fc','fc','ss','ss']

print(data_strings)
vc = CountVectorizer()

data_input = vc.fit_transform(data_strings)
df = pd.DataFrame(data_input.toarray(), columns=vc.get_feature_names_out())
print(df)

model = MultinomialNB()

model.fit(data_input, output)

print(model.predict(vc.transform(['dear gulu please quote  rosemount transmitter'])))

print(model.predict(vc.transform(['dear gulu please quote me transmitter from rosemount'])))

print(model.predict(vc.transform(['dear gulu please quote me rosemount filter'])))

print(model.predict(vc.transform(['dear gulu please quote me kit rosemount'])))