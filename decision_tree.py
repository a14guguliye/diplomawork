from abc import ABC, abstractmethod



class AbstractFilter(ABC):
    @abstractmethod
    def filter_passed(text:str):
        pass 


    @abstractmethod
    def __str__() -> str:
        pass

class RosemountBrandFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return 'rosemount' in text

    def __str__(self) -> str:
        return "rosemount"

class BiffiBrandFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return 'biffi' in text 
    
    def __str__(self) -> str:
        return "biffi"


class CrosbyBrandFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return 'crosby' in text 
    
    def __str__(self) -> str:
        return "crosby"
    
class AndersonFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return 'anderson' in text and 'greenwood' in text 
    
    def __str__(self) -> str:
        return "anderson_greenwood"
    
class FisherFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return "fisher" in text 
    

    def __str__(self) -> str:
        return "fisher"
    
class AscoFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return "asco" in text 
    
    def __str__(self) -> str:
        return "asco"



class MicroMotionFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return 'micro' in text and 'motion' in text 


    def __str__(self) -> str:
        return "micro_motion"


class KeystoneFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return "keystone" in text 
    
    def __str__(self) -> str:
        return "keystone"



class GeneralTransmitterfilter(AbstractFilter):

    def filter_passed(self, text:str):
        return "transmitter" in text and not "fisher" in text 
    
    def __str__(self):
        return "transmitter"



class ActuatorPneumaticBiffiFilter(AbstractFilter):

    def filter_passed(self, text:str):
        return "pneumatic" in text and  "actuator" in text 
    
    def __str__(self):
        return "pneumatic_actuator"




class ElectricBiffiFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return "electric" in text and "actuator" in text 
    
    def __str__(self) -> str:
        return "electric_actuator"



class GlobeValveFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return "globe" in text and "valve" in text 
    
    def __str__(self) -> str:
        return "globe_valve"
    


class GarlockKitFilter(AbstractFilter):

    def filter_passed(self, text: str):
        return "kit" in text and "garlock" in text 
    
    def __str__(self) -> str:
        return "garlock_kit"
    

class TycoValvesFilter(AbstractFilter):

    def filter_passed(self, text: str):
        return "tyco" in text and "valve" in text 
    
    def __str__(self) -> str:
        return "tyco_valve"


class PentairClassifierFilter(AbstractFilter):

    def filter_passed(self, text: str):
        return "pentair" in text
    
    def __str__(self) -> str:
        return "pentair"


class GasChromotographFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return "gas" in text and "chromatograph" in text 
     
    def __str__(self) -> str:
        return "gas chromatograph"





texts=['regulator pressure 316 stainless steel fisher body',
       'cover terminal block o ring rosemount', 
       'seal electric actuator biffi',
       'solenoid valve 1/4in direct acting general valve asco service', 
       'valve,butterfly: 4in,class 150,raised face,tight shut-off,aluminum bronze astm b148 gr c95800 body,aluminum bronze astm b148 gr c95800 disc,monel k-500 stem,monel 400,rtfe,keystone',
       'kit upgrade transmitter electronics board enhandced hart electronic board no configuration button', 
       "actuator pneumatic single acting spring return inlet body material carbon steel body canted yoke", 
       "micro motion transmitter flow meter", 
       "electric actuator spare", 
       "valve,globe: 3in,class 300,raised face flange,shut-off,plain,carbon steel gr wcc body,316 stainless steel stem,metal disc,trim no 29,416 stainless steel,actuator,teflon/viton seal,port size: 3-1/16in,face to f a c e  d i m e n s i o n :  3 2 0 m m , s o f t g o o d s :  t e f l o n  p a c k i n g , s tainless steel stud and nut,softgoods:  fgm  gas k et", 
       "thermowell: 2in,222mm insertion lg,1/2in npsm,stainless steel,rosemount,225mm,class rating: class 150,flange face: flat face/raisedf ace,grade: 1.4462c,shank style: tapered,standard: asme b16.5",
       "valve,relief: 4 inlet x 6in outlet,class 300 x class 150,safety,balanced,semi nozzle,modulating non-flowing,rf flange,stainless steel asme sa351 gr cf8m body,41.38barg set,urethane,pilot operated,-54 to 315deg c, anderson greenwood", 
       "kit: garlock style  body gasket,garlock style  cap gasket,garlock style  set screw gasket,3", 
       "kit repair tyco valve", 
       "kit repair pentair", 
       "gas chromatograph"
       ]


results=['erkin','talib','gulu','gulu','gulu', 'talib', "gulu", "talib", "gulu", "erkin","talib","gulu", "gulu", "gulu", "gulu", "talib"]



features = [
    BiffiBrandFilter(),
    CrosbyBrandFilter(),
    AndersonFilter(),
    FisherFilter(),
    AscoFilter(), 
    KeystoneFilter(), 
    RosemountBrandFilter(),
    MicroMotionFilter(),
    ActuatorPneumaticBiffiFilter(),
    ElectricBiffiFilter(), 
    GlobeValveFilter(),
   GarlockKitFilter(), 
   GeneralTransmitterfilter(), 
   TycoValvesFilter(), 
   GasChromotographFilter(), 
]


input_results={}

if(len(texts)!=len(results)):
    raise Exception("results and input data should be same")
else:
    for feature in  features:
        input_results[str(feature)]=[feature.filter_passed(text) for text in texts]


        



import pandas as pd 
from sklearn.tree import DecisionTreeClassifier, plot_tree
import  matplotlib.pyplot as plt 

df = pd.DataFrame(input_results, index=results)


X_train=df
y_train= df.index

df.to_csv('out.csv')

dt=DecisionTreeClassifier(criterion='gini', random_state=10, max_features=len(df.columns), splitter='random')
dt.fit(X_train, y_train)

print(X_train)

plt.figure(figsize=(20, 12))

plot_tree(dt, filled=True, feature_names=df.columns, fontsize=20, class_names=dt.classes_)
plt.savefig("decision_tree_plot.png")



test_texts=['dear gulu please quote below biffi seal kit', 
            "kit: garlock style  body gasket,garlock style  cap gasket,garlock style  set screw gasket,3", 
           'thermowell insertion stainless steel rosemount', 
           "rosemount transmitter fisher", 
           "globe valve ez series", 
           "anderson greenwood manifold", 
           "kit gas chromotograph rosemount", 
           "kit: repair,type 81 4001psig sp-1 safety relief valve,vespel seat", 
           "transmitter differential pressure transmitter", 
           "kit soft goods pilot valve", 
           "dear gulu please quote below pressure transmitter similiar to crosby", 
           'kit pilot pressure safety valve buna soft goods pentair', 
           "transmitter", 
           "kit overhaul repair rebuild gas chromatograph valve diaphragm"
            ]
input_result_test={}
for feature in  features:
        input_result_test[str(feature)]=[feature.filter_passed(text) for text in test_texts]



print(dt.predict(pd.DataFrame(input_result_test)))











