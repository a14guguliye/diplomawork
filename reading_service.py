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
    with open("./database/"+path, 'w') as json_file:
        json_file.write(json_data)


def read_from_database(word):
    file_names=os.listdir("./database/")

    for file_name in file_names:
        with open("./database/"+file_name, 'r') as json_file:
            data = json.load(json_file)
            try:
                print(word)
                print(data[word])
                print(file_name)
            except Exception:
                pass 



def tokenize_and_lemmatize(words):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in words]
    return lemmatized_tokens

def count_words_in_doc(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    words = word_tokenize(content)
# 
    words=[word.lower() for word in words if word.isalpha() and len(str(word))>=2]

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


# database_path="./manuals/"
# import os 
# import json

# file_names=os.listdir(database_path)
# for file_name in file_names:
#     results =count_words_in_doc('./manuals/'+file_name)
    
#     write_to_database(json.dumps(dict(results), indent=2),file_name+'.json')


read_from_database("crosby")
