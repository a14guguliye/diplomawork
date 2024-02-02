import os 
import json 




class FisherReadingService:
    def __init__(self) -> None:
        pass


    def read_from_database(self):
        fisher_files=os.listdir("./filtered/fisher/")
        output={}
        
        for file_name in fisher_files:
            with open("./filtered/fisher/"+file_name, 'r') as json_file:
                data = json.load(json_file)
                output[file_name]=data
    
        return output
    

class RosemountReadingService:

    def __init__(self) -> None:
        pass 



    def read_from_database(self):
        rmt_files=os.listdir("./filtered/rsmt/")
        output={}
        
        for file_name in rmt_files:
            with open("./filtered/rsmt/"+file_name, 'r') as json_file:
                data = json.load(json_file)
                output[file_name]=data
    
        return output
    

    

class BiffiReadingService:

    def __init__(self) -> None:
        pass 



    def read_from_database(self):
        crosby_files=os.listdir("./filtered/biffi/")
        output={}
        
        for file_name in crosby_files:
            with open("./filtered/biffi/"+file_name, 'r') as json_file:
                data = json.load(json_file)
                output[file_name]=data
    
        return output
    


class CrosbyReadingService:

    def __init__(self) -> None:
        pass 



    def read_from_database(self):
        crosby_files=os.listdir("./filtered/crosby/")
        output={}
        
        for file_name in crosby_files:
            with open("./filtered/crosby/"+file_name, 'r') as json_file:
                data = json.load(json_file)
                output[file_name]=data
    
        return output 
    
from sklearn.naive_bayes import MultinomialNB


    



crosby_service=CrosbyReadingService()
data=(crosby_service.read_from_database())
training_data=[]
for cat, word_numers in data.items():
    training_data.append({"cixis":"final-control",**word_numers})


biffi_service=BiffiReadingService()
data=biffi_service.read_from_database()
for cat, word_numers in data.items():
    training_data.append({"cixis":"final-control",**word_numers})



rmt_service=RosemountReadingService()
rmd_data=rmt_service.read_from_database()
for cat, word_numers in rmd_data.items():
    training_data.append({"cixis":"rmt",**word_numers})


fisher_service=FisherReadingService()
fisher_data=fisher_service.read_from_database()
for cat, word_numers in fisher_data.items():
    training_data.append({"cixis":"final-control",**word_numers})



import pandas as pd 
from sklearn.impute import SimpleImputer
import numpy as np 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

df=pd.DataFrame(training_data)

X_train=SimpleImputer(strategy='constant', fill_value=0).fit_transform(df.drop('cixis',axis=1))
y_train=df['cixis']






mm=MultinomialNB()
mm.fit(X_train, y_train)

text='dear qulu please resistance temperature detector rosemount dual 3 wire stainless steel rosemount'


X_new=np.zeros((1,len(df.columns)-1))
i=0
for col in df.columns:
    for word in text.split():
        if(word==col):
            X_new[0,i]=X_new[0,i]+1
    
    i=i+1


print(mm.predict(X_new))
print(mm.predict_proba(X_new))





















