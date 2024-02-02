import re 
from collections import Counter
import  matplotlib.pyplot as plt 
from nltk.tokenize import  word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import nltk 
import os 
import json 



def write_to_database(json_data, path):
    if(os.path.exists("./database/"+path)):
        pass 
    else:
        with open("./database/"+path, 'w') as json_file:
            json_file.write(json_data)


def read_from_database(word):
    file_names=os.listdir("./database/")

    for file_name in file_names:
        with open("./database/"+file_name, 'r') as json_file:
            data = json.load(json_file)
            


def generate_dict_input():
    file_names=os.listdir("./database/")
    dict_output={}

    for file_name in file_names:
        with open("./database/"+file_name, 'r') as json_file:
            data = json.load(json_file)

            dict_output[file_name]=data

       

            # if isinstance(value, int) and value < 5:
            #     del dict_output[key]

    
    return dict_output





def tokenize_and_lemmatize(words):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in words]
    return lemmatized_tokens

def count_words_in_doc(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    words = word_tokenize(content)
# 
    words=[word.lower() for word in words if word.isalpha() and len(str(word))>=3]

    new_words = [
    word for word in words if word.lower() not in stopwords.words('english')]

    new_words=tokenize_and_lemmatize(new_words)
    word_counts = Counter(new_words)

    return word_counts.most_common()

def plot_histogram(word_counts):
    words, counts = zip(*word_counts.most_common())

    plt.bar(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Word Frequency Histogram')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.show()


database_path="./manuals/"
import os 
import json

file_names=os.listdir(database_path)
for file_name in file_names:
    results =count_words_in_doc('./manuals/'+file_name)
    
    write_to_database(json.dumps(dict(results), indent=2),file_name+'.json')





data=(generate_dict_input())

# # print(data.items())
# from sklearn.naive_bayes import MultinomialNB

# training_data=[]
# i=0
# for category, word_counts in data.items():
#     training_data.append({"cixis":category,**word_counts})
    
#     i=i+1



# # training_data = [{"category": category, **word_counts} for category, word_counts in data.items()]
# import numpy as np 
# import pandas as pd 
# from sklearn.impute import SimpleImputer

# # Convert the data into a Document-Term Matrix (DTM)
# df=pd.DataFrame(training_data)
# imputer=SimpleImputer(strategy='constant', fill_value=0)


# X_train=df.drop('cixis',axis=1)
# X_train=imputer.fit_transform(X_train)
# y_train=df['cixis']



# # vectorizer = DictVectorizer(sparse=False)
# # X_train = vectorizer.fit_transform(df.drop('cixis', axis=1).to_dict(orient="records"))
# # X_train=imputer.fit_transform(X_train)



# # y_train = [datacixis"] for data in training_data]

# # # # print(y_train)
# # # # Train the Multinomial Naive Bayes classifier
# clf = MultinomialNB()
# clf.fit(X_train, y_train)

# from sklearn.tree import DecisionTreeClassifier, plot_tree

# X_train=np.where(X_train>0,True,False)

# dt=DecisionTreeClassifier(random_state=11)
# dt.fit(X_train[10,:], y_train[10,:])


# text= "crosby nozzle valve"
# X_new=np.zeros((1,len(df.columns)-1))
# i=0
# for col in df.columns:
#     for word in text.split():
#         if(word==col):
#             X_new[0,i]=X_new[0,i]+1
    
#     i=i+1


# plt.figure(figsize=(20, 12))

# plot_tree(dt, filled=True, feature_names=df.columns,  class_names=y_train)
# plt.savefig("decision_tree_plot.png")
# plt.show()


# predicted_category = clf.predict(X_new)[0]

# print(clf.predict(X_new.reshape(1,-1)))
# print(dt.predict(X_new.reshape(1,-1)))

# # log_probabilities=(clf.predict_log_proba(vectorizer.transform([{'dear':1, 
# #                                                                 'gulu':1, 
# #                                                                 'thanks':1, 
# #                                                                 'please':1, 
# #                                                                 'quote':1, 
# #                                                                 'below':1, 
# #                                                                 'pressure':1, 
# #                                                                 'safety':1, 
# #                                                                 'valve':1, 
# #                                                                 'jos-e':1}])))


# # for category, log_probability in zip(clf.classes_, log_probabilities[0]):
# #     print(f"Log Probability of input belonging to {category}: {log_probability}")

# # print(clf.predict(vectorizer.transform([{'dear':1, 
# #                                                                 'gulu':1, 
# #                                                                 'thanks':1, 
# #                                                                 'please':1, 
# #                                                                 'quote':1, 
# #                                                                 'below':1, 
# #                                                                 'pressure':1, 
# #                                                                 'safety':1, 
# #                                                                 'valve':1, 
# #                                                                 'jos':1}]))[0])





