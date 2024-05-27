# import pandas as pd 
# from sklearn.model_selection import train_test_split


# data=pd.read_csv(r"spam.csv", usecols=['v1', 'v2'])

# #1st step data cleaning from non coding items. there were somecoding issues while 
# #reading the data. 

# print(data.describe())


# data_dummies=data #pd.get_dummies(data, columns=['v1'])
# #print(data_dummies.head())


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# stop_words = set(stopwords.words('english')) 


# def remove_stops(text):
#     word_tokens = word_tokenize(text)
#     tokenized_cleaned = [str(w) for w in word_tokens if w.lower()  not in stop_words and w.isalnum() and w.isalpha()]
#     return ' '.join(tokenized_cleaned)

# ps=PorterStemmer()


# def stem_text(text):
#     word_tokens=word_tokenize(text)
#     stemmed_words = [ps.stem(word) for word in word_tokens]

#     return ' '.join(stemmed_words)


# data_dummies['v2'] = data_dummies['v2'].apply(remove_stops)
# data_dummies['v2'] = data_dummies['v2'].apply(stem_text)


# # print(data_dummies.head())

# X=data_dummies['v2']
# y=data_dummies['v1']

# print(X.head())

# X_train, X_test, y_train, y_test= train_test_split(X,y, test_size=0.3)




from sklearn.feature_extraction.text import TfidfVectorizer
from array import array
import numpy as np
from sklearn.linear_model import LogisticRegression

# vec=TfidfVectorizer()
# X_train_vec=vec.fit_transform(X_train)
# X_test_vec=vec.transform(X_test)


# model=LogisticRegression()
# model.fit(X_train_vec, y_train)

# print(model.score(X_test_vec, y_test))




# data=np.array([['valve','crosby'], 
#                ['valve', 'kit'], 
#                ['disc', 'valve'], 
#                ['transmitter', 'rosemount'], 
#                ['temperature', 'sensor']
#                ])

# data_strings = [' '.join(row) for row in data]

# output =['fc','fc','fc','ss','ss']



# vec=TfidfVectorizer()
# X_train_vec=vec.fit_transform(data_strings)


# model=LogisticRegression()
# model.fit(X_train_vec, output)


# print(model.predict(vec.transform(['dear gulu please quote  rosemount transmitter'])))

# print(model.predict(vec.transform(['dear gulu please quote me transmitter from rosemount'])))

# print(model.predict(vec.transform(['dear gulu please quote me rosemount filter'])))

# print(model.predict(vec.transform(['dear gulu please quote me kit rosemount'])))
# print(model.predict(vec.transform(['dear gulu please quote me disc from rosemount'])))
#=========================================================================================
import pandas as pd
from sklearn.model_selection import train_test_split 
data=pd.read_csv(r"enron.csv", nrows=5000)

data.drop(['Message ID','Date'], inplace=True, axis=1)



data['Message']=data['Subject'].astype(str)+" "+data['Message'].astype(str)
data.drop(['Subject'],  inplace=True, axis=1)








import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words('english')) 


def remove_stops(text):
    word_tokens = word_tokenize(text)
    tokenized_cleaned = [str(w) for w in word_tokens if w.lower()  not in stop_words and w.isalnum() and w.isalpha()]
    return ' '.join(tokenized_cleaned)

ps=PorterStemmer()


def stem_text(text):
    word_tokens=word_tokenize(text)
    stemmed_words = [ps.stem(word) for word in word_tokens]

    return ' '.join(stemmed_words)


data['Message'] = data['Message'].apply(remove_stops)
data['Message'] = data['Message'].apply(stem_text)

X=data['Message']
y=data['Spam/Ham']

X_train, X_test, y_train, y_test= train_test_split(X,y, test_size=0.3)

vec=TfidfVectorizer()
X_train_vec=vec.fit_transform(X_train)
X_test_vec=vec.transform(X_test)


from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
label_encoder=LabelEncoder()


y_train=label_encoder.fit_transform(y_train)
y_test=label_encoder.transform(y_test)

model = KNeighborsClassifier()


model.fit(X_train_vec, y_train)

print(accuracy_score(y_test, model.predict(X_test_vec)))


from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler



data=np.array([['valve','crosby'], 
               ['valve', 'kit'], 
               ['disc', 'valve'], 
               ['transmitter', 'rosemount'], 
               ['temperature', 'sensor']
               ])

data_strings = [' '.join(row) for row in data]

output =['fc','fc','fc','ss','ss']



vec=TfidfVectorizer()
X_train_vec=vec.fit_transform(data_strings)


model=KNeighborsClassifier()
model.fit(X_train_vec, output)


print(model.predict(vec.transform(['dear gulu please quote  rosemount transmitter'])))

print(model.predict(vec.transform(['dear gulu please quote me transmitter from rosemount'])))

print(model.predict(vec.transform(['dear gulu please quote me rosemount filter'])))

print(model.predict(vec.transform(['dear gulu please quote me kit rosemount'])))
print(model.predict(vec.transform(['dear gulu please quote me disc from rosemount'])))