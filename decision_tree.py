from abc import ABC, abstractmethod
import re 


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



class FisherActuatorFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return "actuator" in text and "fisher" in text 
    
    def __str__(self) -> str:
        return "fisher_actuator"



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


class DanielFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return "daniel" in text
     
    def __str__(self) -> str:
        return "daniel"
    






class BaileyBirkett(AbstractFilter):
    def filter_passed(self, text: str):
        return "bailey" in text and 'birkett' in text  or ('birkett' in text)
     
    def __str__(self) -> str:
        return "bailey-birkett"



class PositionerFilterDVC(AbstractFilter):
    def filter_passed(self, text: str):
        return "dvc6200" in text 
     
    def __str__(self) -> str:
        return "dvc_positioner"


class TemperatureDetector(AbstractFilter):

    def filter_passed(self, text: str):
        return 'detector' in text and 'temperature' in text
    
    def __str__(self) -> str:
        return 'temperature_detector'


class ValveReliefFilter(AbstractFilter):

    def filter_passed(self, text: str):
        return 'valve' in text  and 'relief' in text
    
    def __str__(self) -> str:
        return 'valve_relief'



class Rosemount3300HTFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return '3300ht' in text or '3300htvp' in text or '3400ht' in text or '3400htvp' in text or '3500p' in text or '3500vp' in text 
    
    def __str__(self) -> str:
        return 'ph_sensor_rosemount'
    

class TartariniFilter(AbstractFilter):
    def filter_passed(self,text: str):
        return 'tartarini' in text
    
    def __str__(self) -> str:
        return 'tartarini'


class TopworxFilter(AbstractFilter):

    def filter_passed(self, text: str):
        return 'topworx' in text 
    

    def __str__(self) -> str:
        return 'topworx'


class MR95HFilter(AbstractFilter):

    def filter_passed(self, text: str):
        return 'mr95h' in text 
    
    def __str__(self) -> str:
        return "mr95h"
    

class FLowControlTechnologies(AbstractFilter):

    def filter_passed(self, text: str):
        return 'flow' in text and 'control' in text and 'technologies' in text
    

    def __str__(self) -> str:
        return "fct"


class GroveleyDetectorFilter(AbstractFilter):
    def filter_passed(self, text: str):
        return 'groveley' in text and 'detection' in text 
    
    def __str__(self) -> str:
        return 'groveley_detection'





class Rosemount0096ThermowellFilter(AbstractFilter):

    pattern =r"^0096[dyajkpz]\d{4}[t,f,d,w,e]\d{2}t\d{3}[adt]"
    def filter_passed(self, text: str):
        words= re.split(r'\W+', text)

        for word in words:
            if re.match(self.pattern, word):
                return True 

        return False
    
    def __str__(self) -> str:
        return 'rosemount_0096'




class Trex375FieldCommunicatorFilter(AbstractFilter):

    pattern =r"^(00275|00375|00475)-(0096|0002|0003|0004|0005|0006|0015|0018|0035|0043|0044|0045|0047|0049)-(0001|0022|0044|0003|0002|0008|dvd1)"

    def filter_passed(self, text: str):
        words= text.split()

        for word in words:
            if re.match(self.pattern, word):
                return True 

        return False
    
    def __str__(self) -> str:
        return 'trex_field_communicator_375'





class GeFisherSpareFilter(AbstractFilter):
    pattern=r"ge\d{5}x\d{3}"

    def filter_passed(self, text: str):
        words= text.split()

        for word in words:
            if re.match(self.pattern, word):
                return True 

        return False
    
    def __str__(self) -> str:
        return 'ge_fisher_spare'



class GenericFisherSpareFilter(AbstractFilter):

    pattern =r"^(1[0-9]|2[0-9])(a|b)\d{4}(d|f|x)\d{3}$"


    def filter_passed(self, text: str):
        words= text.split()

        for word in words:
            if re.match(self.pattern, word):
                return True 

        return False
    
    def __str__(self) -> str:
        return 'generic_fisher'




class Actuator3025SpareFilter(AbstractFilter):
    pattern =r"^(014|015|016|041|026|027|029|122|123|126|128|134|138|160|163)\d{4}"


    def filter_passed(self, text: str):
        words= text.split()

        for word in words:
            if re.match(self.pattern, word):
                return True 

        return False
    
    def __str__(self) -> str:
        return '3025_actuator_spare'
    


class RosemountManifoldSpare(AbstractFilter):
    pattern =r"^(03031|00304|00305|01151|01166)-\d{4}-\d{4}"

    def filter_passed(self, text: str):
        words= text.split()

        for word in words:
            if re.match(self.pattern, word):
                return True 

        return False
    
    def __str__(self) -> str:
        return 'rosemount_manifold_kit'



class FisherSpare25002503(AbstractFilter):
    pattern =r"^(r250).{7}$|^(rrelay)"


    def filter_passed(self, text: str):
        words= text.split()

        for word in words:
            if re.match(self.pattern, word):
                return True 

        return False
    
    def __str__(self) -> str:
        return 'fisher_spare_25032500'
    




class RosemountManifold(AbstractFilter):

    pattern =r"^(0304|0305|0306)|^(r304|r305|r306)"


    def filter_passed(self, text: str):
        words= text.split()

        for word in words:
            if re.match(self.pattern, word):
                return True 

        return False
    
    def __str__(self) -> str:
        return 'rosemount_manifold'




class RousemountORingPackageFilter(AbstractFilter):
    pattern =r"^(03151)-\d{4}-\d{4}"


    def filter_passed(self, text: str):
        words= text.split()

        for word in words:
            if re.match(self.pattern, word):
                return True 

        return False
    
    def __str__(self) -> str:
        return 'rosemount_oring'    
    


class R249FisherSpareFilterr(AbstractFilter):

    def filter_passed(self, text: str):
        words= text.split()

        for word in words:
           if word=='r249x000012':
                return True 

        return False
    
    def __str__(self) -> str:
        return 'rosemount_oring'    
    
class HSGTemperatureTransmitterFilter(AbstractFilter):

    pattern =r"^(hsg)\d+"

    def filter_passed(self, text: str):
        words= text.split()

        for word in words:
            if re.match(self.pattern, word):
                return True 

        return False
       
    
    def __str__(self) -> str:
        return 'hsg_transmitter' 




class R299HFisherSpareFilter(AbstractFilter):
    def filter_passed(self, text: str):
        words= text.split()
        r299spares=["d103127x012",
  "d102684x012",
  "d102601x012",
  "d101555x012",
  "1a7715t0012",
  "20762078",
  "t80391-5",
  "d103695x012",
  "t13707t0012",
  "t13589t0012",
  "1n3112x0012",
  "1b413727222",
  "t13593t0012",
  "t13671t0012",
  "t13600t0012",
  "19b0432x012",
  "19b0432x022",
  "r299x000012",
  "eraa10462a1",
  "eraa10463a1",
  "1l928308012",
  "eraa51389a0",
  "eraa21736a0",
  "t13831t0012",
  "1a341224122",
  "t13918t0012",
  "t13463t0012",
  "t20986t0012",
  "1f914106992",
  "t13814t0012",
  "1l143311992",
  "t13833t0012",
  "1h979309022",
  "1h979409022",
  "1h979509022",
  "t14098t0012",
  "1h979609022",
  "1h979709022",
  "1p7349000a2",
  "1e216306992",
  "t12587t0012",
  "1l1426000a2",
  "t40578t0012",
  "1j190419012",
  "1h968919012",
  "t80445t0012",
  "2l425119012",
  "eraa11740a0",
  "eraa11741a0",
  "eraa11742a0",
  "eraa11743a0",
  "eraa11744a0",
  "1j1904t0022",
  "1h9689t0022",
  "t80415t0012",
  "t14034t0012",
  "t14082t0012",
  "13299h",
  "1c379124052",
  "1b420428982",
  "1h972935032",
  "t13813t0012",
  "y602-12",
  "27a5516x012",
  "t14259t0012",
  "24b1301x012",
  "t14069t0012",
  "t14097t0012",
  "eraa10464a1",
  "t13917t0012",
  "t14135t0012",
  "1a352224122",
  "t14133t0012",
  "1e985324142",
  "1f230328992",
  "t13915t0012",
  "t14033t0012",
  "t13914t0012",
  "t14136t0012",
  "t14031t0012",
  "1a954828992",
  "t13916t0012",
  "16a6977x012",
  "t14258t0012",
  "t13920t0012",
  "t13824t0012",
  "1h9666t0012",
  "t13939t0012",
  "t13825t0012",
  "t13791t0012",
  "t13955t0012",
  "1d682506992",
  "13a2331x022",
  "1e175828982",
  "t14134t0012",
  "1a767524662",
  "17a0960x012",
  "1e501728982",
  "t14088t0012",
  "17a2029x012",
  "17a2030x012",
  "17a7277x012",
  "p593-1",
  "aj5004t0012",
  "p594-1",
  "aj5004000a2",
  "t13830t0012",
  "t13812t0012",
  "t14013t0012",
  "t1072606562",
  "t14039t0012",
  "t13769t0012",
  "t13772t0012",
  "1c629828992",
  "t14030t0012",
  "t1215806032",
  "t1215906032",
  "19b0553x012",
  "t13543t0042",
  "eraa51390a0",
  "eraa52227a0",
  "18b2129x012",
  "1h2926x0032",
  "1n659106242",
  "t80391-2",
  "t80391-3",
  "14299h",
  "11109l2",
  "t80391-7",
  "t80391",
  "t80391-4",
  "15299h",
  "t80391-1",
  "16299h",
  "17299h",
  "t80391-6"
                ]

        for word in words:
           if word in r299spares:
               return True

        return False
    
    def __str__(self) -> str:
        return '299H_spare'  





class R1018SFisherSpare(AbstractFilter):

    def filter_passed(self, text: str):
        words= text.split()
        r1018sspare=[
  "0319686",
  "1882945",
  "19a3273x012",
  "0225924",
  "2472244",
  "2473852",
  "2473879",
  "2148218",
  "2465825",
  "2424576",
  "2424584",
  "2424622",
  "2424649",
  "2424657",
  "2465876",
  "2424606",
  "2424614",
  "2424665",
  "2424673",
  "2424681",
  "0869236",
  "2472678",
  "19a4913x012",
  "0225932",
  "1q57018e012",
  "1882953",
  "1882988",
  "1882996",
  "gf00191",
  "gf00190",
  "0483729",
  "0483788",
  "1936387",
  "1975218",
  "0483737",
  "0483745",
  "0483800",
  "1073435",
  "1q57227e012",
  "1073591",
  "1073605",
  "2424347",
  "2424355",
  "2424428",
  "2424436",
  "2424495",
  "2424509",
  "2424517",
  "2470101",
  "2469944",
  "2464144",
  "2464152",
  "2464179",
  "2464586",
  "2464594",

  "2470217",
  "2469456",
  
  "2464217",
  "2464225",
  "2464233",
  
  "2424371",
  "2424398",
  "2424452",
  "2424479",
  "2424169",
  "2424177",
  "2424185",
  "2466465",
  "2466473",
  "2316064",
  "2464195",
  "2464209",
  "2464616",
  "2464624",
  "2464632",
  "2424223",
  "2424231",
  "2424258",
  "2464241",
  "2464268",
  "2464276",
  "1278231",
  "19a4908x012",
  "2472562",
  "1898272",
  "1898299",
  "1278258",
  "2473984",
  "2473887",
  "1867105",
  "1898221",
  "1882961",
  "d102624x012",
  "10a9421-a",
  "aj5428-d",
  "a0832-2/il",
  "gf00180",
  "gf00181",
  "gf00182",
  "gf00183",
  "gf00185",
  "gf00184",
  "vpc-61",
  "gf00186",
  "gf00187",
  "gf00192",
  
  "r1018sy0072",
  "r1018sy0082",
  "r1018sy0092",
  "r1018sy0102",
  "r1018sy0112",
  "r1018sy0122",
  "rpacky00012",
  "rpacky00022",
  "rpacky00032",
  "rpacky00042",
  "rpackyrt052",
  "rpackyrt062",
  "rpackyrt072",
  "rpackyrt082",
  "2474042",
  "2222477",
  "2217171",
  "2227272",
  "1992163",
  "2526905",
  "2217198",
  "2218534",
  "0471267",
  "0471275",
  "0471291",
  "1097458",
  "gf00195",
  "gf00193",
  "0483478",
  "0483516",
  "0483486",
  "048352415",
  "0483494",
  "0483532",
  "0483575",
  "0483630",
  "0483583",
  "0483648",
  "0483591",
  "048365625",
  "0483605",
  "0483664",
  "1856251",
  "1936484",
  "0483796",
  "048379650",
  "0483753",
  "0483818",
  "0483982",
  "0484032",
  "0483990",
  "0484040",
  "0484008",
  "0484059",
  "0484016",
  "0483265",
  "0483346",
  "0483400",
  "0483354",
  "0483419",
  "1029681",
  "1029703",
  "1029665",
  "1181556",
  "0566470",
  "1q57014e012",
  "2527898",
  "1222589",
  "0591238",
  "1q57226e012",
  "2527871",
  "1262777",
  "2424363",
  "242444415",
  "2469235",
  "2469243",
  "2469251",
  "2469278",
  "2469286",
  "2469294",
  "2471566",
  "2469308",
  "2471612",
  "2424266",
  "2424274",
  "2424282",
  "242436325",
  "2424444",
  "2470497",
  "247049750",
  "2464438",
  "2464446",
  "2464454",
  "2470179",
  "2470403",
  "2471426",
  "2470187",
  "2470411",
  "2471434",
  "2469634",
  "2469642",
  "2469677",
  "2464608",
  "2462608",
  "2464713",
  "2464721",
  "2464748",
  "2470543",
  "2470195",
  "2469421",
  "2470527",
  "2470209",
  "2469448",
  "2470535",
  "247054325",
  "2470225",
  "2469979",
  "2470551",
  "2424703",
  "2424711",
  "2424738",
  "2464519",
  "2464527",
  "2464535",
  "2464659",
  "2464667",
  "2464675",
  "2464799",
  "2464802",
  "2464829",
  "2424401",
  "242448715",
  "2221756",
  "2465035",
  "2465124",
  "2466414",
  "2466422",
  "2466457",
  "2465221",
  "2465213",
  "2465256",
  "2424304",
  "2424312",
  "2424339",
  "242440125",
  "2424487",
  "2466503",
  "246650350",
  "2464462",
  "2464489",
  "2464497",
  "2466341",
  "2466368",
  "2466449",
  "2466481",
  "2464969",
  "2465019",
  "2465264",
  "2465272",
  "2465329",
  "2464756",
  "2464764",
  "2464772",
  "2465841",
  "2465906",
  "2466007",
  "2466031",
  "2466317",
  "2466325",
  "2466023",
  "2466058",
  "2466066",
  "2424746",
  "2424754",
  "2424762",
  "2316056",
  "2464551",
  "2464578",
  "2464683",
  "2464691",
  "2464705",
  "2464837",
  "2464853",
  "2464861",
  "2061333",
  "2535432",
  "12b8283x012",
  "13b6564x012",
  "12b8281x012",
  "13b6089x012",
  "13b6074x012",
  "19b4146x012",
  "13b6076x012",
  "19b4147x012",
  "13b6078x012",
  "1q57143f012",
  "2073676",
  "0280607",
  "0819573",
  "1q57147f012",
  "0802808",
  "0802786",
  "16mm",
  "031986",
  "2061341",
  "2218585",
  "13b6564e012",
  "2218593",
  "2218666",
  "2218631",
  "19b4152x012",
  "2218658",
  "19b4151x012",
  "13b6078e012",
  "1q57156f012",
  "2073684",
  "1q57488f012",
  "0819581",
  "1q57159f012",
  "0802794",
  "0802778"]

        for word in words:
           if word in r1018sspare:
               return True

        return False
    
    def __str__(self) -> str:
        return 'r1018s_spare' 




class R310A32AFisherSpare(AbstractFilter):
    def filter_passed(self, text: str):
        words= text.split()
        r310a32aspares=[
  "1d809627022",
  "1e392527022",
  "1d387227022",
  "1d465127142",
  "13a5543x012",
  "1r752604152",
  "d102068x012",
  "24b4134",
  "1f463606992",
  "1n571406382",
  "steel/nylon",
  "1f2620x0012",
  "1n423906382",
  "nickel-based",
  "1a368228982",
  "1v211714012",
  "17b8959x012",
  "1b828626012",
  "r310x000072",
  "15a6002xw32",
  "r32ax000012",
  "r32ax000022",
  "2r742222012",
  "11a8122x012",
  "1d995448702",
  "1h483324122",
  "1r742524092",
  "1b139324052",
  "1r742604022",
  "1r742724152",
  "1r742806992",
  "1u448302462",
  "1d651538992",
  "2r742924092",
  "2r7429x0052",
  "1r7430000a2",
  "1r7430x0022",
  "1d687506992",
  "1n430406382",
  "1e216306992",
  "1l949306382",
  "eraa50447a0",
  "1r743335132",
  "1r7433x0012",
  "1r743435132",
  "1r7434x0012",
  "10a4912x012",
  "12a3962x012",
  "10a4912x082",
  "1r743835162",
  "1d986735132",
  "1d9867x0012",
  "1a309324122",
  "34b3863x012",
  "34b3880x012",
  "34b3880x022",
  "1u379006992",
  "1v101506382",
  "1r744228982",
  "14b3881x012",
  "14b3881x022",
  "1r744535232",
  "1r7445x0012",
  "1e218106992",
  "1n530106382",
  "1f262035032",
  "1d191706992",
  "1r744637022",
  "12b7884x012",
  "1u550637022",
  "12b7883x012",
  "15a6002x462",
  "17a6570x012",
  "1v205699012",
  "1b6149x0012",
  "1b6149x0032",
  "r310x000012",
  "r310x000032",
  "r310x000052",
  "r310x000022",
  "r310x000042",
  "r310x000062",
  "r310x000082",
  "44b3869x012",
  "44b3870x012",
  "44b3870x022",
  "44b3872x012",
  "44b3872x022",
  "44b3874x012",
  "44b3874x022",
  "44b3876x012",
  "44b3876x022",
  "44b3871x012",
  "44b3871x022",
  "44b3873x012",
  "44b3873x052",
  "44b3875x012",
  "44b3877x012",
  "24b5843x012",
  "24b5843x032",
  "24b6356x012",
  "24b6356x032",
  "24b8847x022",
  "24b8847x032",
  "24b9998x022",
  "24b9998x042",
  "24b6355x012",
  "24b6355x042",
  "24b6357x012",
  "24b6357x032",
  "27b0251x022",
  "24b8813x012",
  "34b4103x012",
  "34b3980x012",
  "34b3980x022",
  "44b3981x012",
  "44b3981x022",
  "44b3982x012",
  "44b3982x022",
  "44b3983x012",
  "44b3983x022",
  "44b4110x012",
  "34b4104x012",
  "34b4104x022",
  "44b4105x012",
  "44b4105x052",
  "44b4106x012",
  "44b4107x012",
  "44b4111x012",
  "3r746822012",
  "3u357022012",
  "3u3570x0072",
  "4u356822012",
  "4u3568x0152",
  "4u357222012",
  "4u3572x0062",
  "4u357622012",
  "4u3576x0052",
  "41a8162x012",
  "3r746622012",
  "4r740422012",
  "4r749422012",
  "4r751222012",
  "40a9616x012",
  "10a8220x012",
  "20a8221x012",
  "20a8222x012",
  "20a8223x012",
  "20a9619x012",
  "1r747024092",
  "1r7470x0012",
  "1r740724392",
  "1r7407x0012",
  "1r749624392",
  "1r7496x0012",
  "1r751425012",
  "1r7514x0012",
  "1r747124092",
  "1r7471x0012",
  "1r740922012",
  "1r7409x0012",
  "2r749822012",
  "2r7498x0012",
  "2r751622012",
  "2r7516x0012",
  "1r747299982",
  "1r741099982",
  "1r749999982",
  "2r751799982",
  "21a1929x022",
  "21a1930x022",
  "21a1931x022",
  "21a1932x022",
  "1r747335132",
  "1r7473x0012",
  "1r741135132",
  "1r7411x0012",
  "1r750035132",
  "1r7500x0012",
  "1r751835132",
  "1r7518x0012",
  "1u888627112",
  "13b7203x012",
  "1u888527132",
  "12b7885x012",
  "1u888727082",
  "13b9520x012",
  "1u888827082",
  "14b3560x012",
  "10a9620x012",
  "1e736906992",
  "1h2921x0012",
  "eraa19160a0",
  "1h862106992",
  "1n163306382",
  "1r752306382",
  "1l111206382",
  "1u448406382",
  "1r747538982",
  "1r7475x0012",
  "1r741438982",
  "1r7414x0012",
  "1r740638982",
  "1r7406x0012",
  "1r741338982",
  "1r7413x0012",
  "1u984499012",
  "10a8217x022",
  "10a8218x032",
  "10a8217x012",
  "10a8218x012",
  "10a8202x012",
  "10a8203x012",
  "19a0690x012",
  "10a8204x012",
  "10a8204x022",
  "20a8205x012",
  "20a8206x012",
  "20a8207x012",
  "20a8208x012",
  "20a8208x022",
  "20a8209x012",
  "20a8210x012",
  "20a8211x012",
  "10a8212x012",
  "10a8212x022",
  "20a8213x012",
  "20a8214x012",
  "20a8215x012",
  "20a8216x012",
  "20a8216x022",
  "1a3321x0032",
  "1a3321x0042",
  "1u154838982",
  "1u1548x0032",
  "1e304428982",
  "1e3044x0012",
  "1n2579x0022",
  "1a560632982",
  "1a771132982",
  "1l469632982",
  "1r752132982",
  "1r7477x0012",
  "1r7416x0012",
  "1r7503x0012",
  "1r7527x0012",
  "10a9621x022",
  "1r747838982",
  "1r741738982",
  "1r750838982",
  "1r752238982",
  "10a9622x012",
  "1r748204152",
  "1r745203362",
  "1r750704152",
  "12a6413x012",
  "12a6414x012",
  "12a6415x012",
  "1c941928982",
  "1a369224492",
  "1v435606242",
  "1v435706242",
  "1v435806242",
  "1v435906242",
  "10a8224x012",
  "10a8225x012",
  "10a8226x012",
  "10a8227x012",
  "303/316",
  "10a8228x012",
  "10a8228x022",
  "10a8229x012",
  "10a8229x022",
  "10a8234x012",
  "10a8234x022",
  "10a8235x012",
  "10a8235x022",
  "34b4129-b",
  "11a6853x012",
  "11a6854x012",
  "11a6855x012",
  "11a6856x012",
  "15a6002x612",
  "14b8803x012",
  "15a6002xw22",
  "1k201428992",
  "1b352626012",
  "1b860628992",
  "1d7469x00a2",
  "14b5625x012",
  "1h359428992",
]

        for word in words:
           if word in r310a32aspares:
               return True

        return False
    
    def __str__(self) -> str:
        return '310a-32a' 



class R377TripValveSpare(AbstractFilter):

    def filter_passed(self, text: str):
        words= text.split()

        r377_trip_valve_sparer=["r377x000012","r377x000032"]
        for word in words:
           if word in r377_trip_valve_sparer:
               return True

        return False
    
    def __str__(self) -> str:
        return 'r_377_trip_valve'


class R667ActuatorSpare(AbstractFilter):
    def filter_passed(self, text: str):
        words= text.split()

        r667_actuator_spare=["r667x000302",
  "r667x000402",
  "r667x000502",
  "r667x000702",
  "r667x000762",
  "r667x000312",
  "r667x000412",
  "r667x000422",
  "r667x000512",
  "r667x000522",
  "r667x000532",
  "r667x000542",
  "r667x000722",
  "r667x000772",
  "r667x000732",
  "30a8778x0e2",
  "30a8778x0f2",
  "30a8778x0g2",
  "30a8778x0h2",
  "40a8779x0a2",
  "40a8779x0b2",
  "40a8779x0c2",
  "40a8779x0d2",
  "ge71635x0e2",
  "ge71635x0f2",
  "ge71635x0g2",
  "ge71635x0h2",
  "ge71636x0a2",
  "ge71636x0b2",
  "ge71636x0c2",
  "ge71636x0d2",
  "ge71635x0j2",
  "ge71636x0e2",
  "30b3940x102",
  "30b3940x022",
  "30b3940x042",
  "cv8060x0012",
  "30b3940x052",
  "30b3940x062",
  "30b3940x092",
  "33b9224x022",
  "33b9224x032",
  
  "30b3940",
  "30b3942\u2010a",
  "45/45i\u201076/76i",
  "33b9224\u2010b",
  "cv8060\u2010j",
  "ge61626-a",
  "30a8778\u2010d",
  "ge71635-a",
  "40a8779\u2010d",
  "ge71636-a",
  "bv8094\u2010b",
  "38a1212\u2010b",
  "28a1208\u2010b",
  "28a1204\u2010b",
  "av8096\u2010b"]
        for word in words:
           if word in r667_actuator_spare:
               return True

        return False
    def __str__(self) -> str:
        return 'r667actuator_spare'




class  R67CRegulatorSpare(AbstractFilter):
    def filter_passed(self, text: str):
        words= text.split()

        r667_actuator_spare=["67c",
  "67cfr",
  "67cfsr",
  "67cf",
  "67cr",
  "67cfs",
  "67csr",
  "67cs",

  "t14113t0012",
  "t14114t0012",
  "t14115t0012",

  "d102601x012",

  "ge07809t012",
  "t14059t0012",
  "t14058t0012",
  "t14060t0012",

  "10c1729x012",
  "10c1730x012",

  "t14116t0012",
  "t14103t0012",
  "ah3946x0052",
  "t13526t0012",
  "1a9463x0042",

  "r67cx000012",
  "r67cx000n12",
  "r67crx00012",
  "r67crx00n12",
  "r67csx00012",
  "r67csrx0012",
  "r67cfx00012",
  "r67cfx00n12",
  "r67cfrx0012",
  "r67cfrx0n12",
  "r67cfsrx012",
  "t14121t0012",
  "t14121t0032",
  "t14121t0022",
  "t14121t0042",
  "t14121t0052",
  "t14121t0062",
  "t14121t0072",
  "t14121t0092",
  "t14121t0102",
  "t14121t0112",
  
  "r67adnx0012",
  "r67adfx0012",
  "r67adnx0022",
  "r67adfx0022",
  "t14053t0012",
  "t14053t0022",
  "t14053t0032",
  "t14053t0042",
  "t14053t0052",
  "t14105t0012",
  "t14071t0012",
  "t14063t0012",
  "t14063t0022",
  "t14063t0032",
  "t14055t0012",
  "t14055t0022",
  "t14119t0022",
  "t14119t0042",
  "t14119t0012",
  "t14119t0032",
  "t14119t0052",
  "t14119t0062",
  "t14119t0072",
  "t14119t0082",
  "t14119t0092",
  "t14119t0102",
  "t14061t0012",
  "t14102t0012",
  "t14104t0012",
  "t14101t0012",
  "t14198t0012",
  "t40643t0rg2",
  "ge00909x012",
  "t80510t0012",
  "40c1887x012",
  "eraa17101a0",
  "eraa17101a1",
  "eraa17102a0",
  "eraa17102a1",
  "1k418918992",
  "gg00554x012",
  "gg00554x022",
  "14b3987x012",
  "t13526t0042",
  "t14380t0012",
  "t14380t0022",
  "t14380t0032",
  "t14057t0042",
  "t14057t0022",
  "t14057t0032",
  "t21040t0012",
  "ge34605x012",
  "ge34606x012",
  "20c1726x012",
  "ge34607x012",
  "ge31792x012",
  "ge32761x012",
  "17a1457x012",
  "15a5967x022",
  "t14070t0012",
  "t14070t0022",
  "20c1727x012",
  "t14052t0012",
  "t14052t0022",
  "t80434t0012",

  "t40645",
  "ge03521",
  "t14101t0022",
  "1a946324122",
  "t14051t0042",
  "t14051t0012",
  "11b8579x022",
  "11b8579x032",
  "11b8579x042",
  "11b9639x012",
  "11b9639x022",
  "11b9639x032",
  "1c333528992",
  "1a767535072",
  "1h447099022",
  "t14081t0012",
  "t14081t0022",
  "19a6034x012",
  "10b2657x012",
  "1u7581000a2",
  "23b9152x012",
  "t14123t0012",
  "t14123t0022",
  "t14196t0012",
  "t14196t0022",
  "ge03520xrg2",
  "ge03520x012",
  "0l078343062",
  "t21043t0012",
  "1e591406992",
  "1c898603012"]
        for word in words:
           if word in r667_actuator_spare:
               return True

        return False
    def __str__(self) -> str:
        return 'r67c_regulator_spare'
    



class  R546TransducerSpare(AbstractFilter):
    def filter_passed(self, text: str):
        words= text.split()

        r667_actuator_spare=[
  "15a6002x162", 
  "1d687506992",
  "15a6002x202",
  "3p426825022",
  "1a582824052",
  "1c225728982",
  "29a1594-h",
  "26a5936-h",
  "d200108x012", 
  "12b8041-b",
  "a6072-1",
  "cp4285\u2013a",
  "a1505\u20133",
  "19a1361-a",
  "r546x000022",
  "r546x000032",
  "r82x0000022",
  "10a8593x082",
  "10a8593x142",
  "30a8595-l",
  "b1768-3",
  "1p4210000a2",
  "3p4213000a2",
  "1m3590x0012",
  "13b6776x012",
  "1d444806992",
  "14b7744x012",

  "11b8582x022",
  "11b8582x042",
  "11b8579x072",
  "17b0404x012",
  "1p426928982",
  "1c197024052",
  "1e591406992",
  "14b7748x012",
  "1c678926232",
  "17b7757x012",
  "1e878406992",
  "1a913221992",
 
  "1a767524662",
  "1n107318992",
  "1p425315052",
  "14b7743x012",
  "30a8594-k",
  "b1767-3",
  "1c782206992",
  "14b7747x012",
  "12b2577x012",
  "1u3958000a2",
  "1u3975000a2",
  "1r6521000a2",
  "1p4242000a2",
  "11b2218x012",
  "3p4192x0022",
  "2p419347052",
  "2p419447052",
  "1p419514012",
  "1p419615102",
  "1p4197x0032",
  "26a5657x012",
  "1u8160x0012",
  "1p420324102",
  "0l078343062",
  "1p420437022",
  "15a3181x012",
  "1p420606992",
  "1p420706992",
  "1d134606992",
  "a1504-1",
  "10b6513x012",
  "59061140x22",
  "12b8041x012",
  "12b8041x022",
  "12b8041x032",
  "12b8041x042",
  "48a9176-b",
  "a5425-1",
  "30b1265x022",
  "2r1552x0022",
  "35a4153x012",
  "42b0737-a",
  "a5426-1",
  "1f401225072",
  "2r100125022",
  "22a7618x012",
  "1n789132992",
  "1b865928982",
  "1c870224052",
  "1c5958x0022",
  "1a352624052",
  "1b989624052",
  "1k747624052",
  "1a368324052",
  "1k766824092",
  "1r801924092",
  "1f906724092",
  "1v102624052",
  "1l200624092",
  "18a1696x012",
  "3l276725092",
  "1a352724122",
  "1p427028982",
  "19a7930x012",
  "19a4838x022",
  "10b6610x012",
  "1h723125072"]
        for word in words:
            if word in r667_actuator_spare:
                return True

        return False
    def __str__(self) -> str:
        return 'r546_fisher_spare'

class RFisher4660Spare(AbstractFilter):

    def filter_passed(self, text: str):
        words= text.split()

        r667_actuator_spare=[
        
  "d200163x012",  
  "39a1578-a",
  "38a6087-b",
  "38a6086-b",
  "38a6084-b",
  "38a6085-b",
  "18a3804\u2010g",
  "39a1578\u2010a",
  "a3300\u20101",
  "38a3803\u2010a",
  "a2898\u20102",
  "r4660xavr52",
  "r4660xbtfj2",
  "r4660xbtfk2",
  "r4660xbtfl2",
  "r4660xbtfm2",
  "r4660xbtfn2",
  "r4660xbtfr2",
  "r4660xbtfs2",
  "r4660xbtf12",
  "r4660xbtf22",
  "r4660xbtf32",
  "r4660xbtf42",
  "r4660xbtf52",
  "r4660xbtf62",
  "r4660xbtf72",
  "r4660xbtf82",
  "r4660xbtf92",
  "r4660xfca22",
  "r4660x0put2",
  "r4660xspa32",
  "r4660xspa22",
  "r4660xspa12",
  "r4660xsp1a2",
  "r4660xsp1b2",
  "r4660xsp1c2",
  "r4660xsp1d2",
  "r4660xsp1e2",
  "r4660xsp1f2",
  "r4660xsp1g2",
  "r4660xsp1h2",
  "r4660xsp1t2",
  "48a3536\u2010h",
  "r4660xsp1j2",
  "r4660xsp1k2",
  "r4660xsp1l2",
  "r4660xsp1m2",
  "r4660xsp1n2",
  "r4660xsp1p2",
  "r4660xsp1r2",
  "r4660xsp1s2",
  "r4660xsp1u2",
  "r4660xstp22",
  "r4660xtpc12",

        ]
        for word in words:
            if word in r667_actuator_spare:
                return True

        return False
    def __str__(self) -> str:
        return 'r4660_fisher_spare'




class RFishe667Spare(AbstractFilter):

    def filter_passed(self, text: str):
        words= text.split()

        r667_actuator_spare=[
  "10b3077x012",
  "10b3078x012",
  "10b3079x012",
  
 
  "d102778x012",
  
  "10b3076x012",
 
  "30b8734x012",
  "30b3102x012",
  "d101328x012",
  "1a560724052",
  "1a5607x0052",
  "30b3104x012",
  "39a5987x012",
  "eraa51241a0",
  "30b3055x012",
  "30b3102x092",
  "r627x000a12",
  "r627x000s12",
  "r627hx00s12",
  "r627rx00a12",
  "r627rx00s12",
  "30b3046x012",
  "30b3048x012",
  "eraa42554a0",
  "30b3096x012",
  "39b2451x012",
  "39b0414x012",
  "30b3050x012",
  "30b3051x012",
  "30b7452x012",
  "39b0412x012",
  "39b0415x012",
  "40b6754x012",
  "40b6756x012",
  "41b8978x012",
  "41b8080x012",
  "43b8656x022",
  "44b0666x012",
  "33b6723x012",
  "38b1688x012",
  "44b0386x012",
  "44b3342x012",
  "30b3050x062",
  "30b3051x092",
  "30b7452x052",
  "43b8656x052",
  "44b0666x022",
  "41b8978x072",
  "41b8080x072",
  "40b6754x102",
  "40b6756x062",
  "44b0386x032",
  "44b3342x032",
  "eraa33145a0",
  "eraa31302a0",
  "eraa44998a0",
  "eraa45039a0",
  "eraa45040a0",
  "eraa33146a0",
  "eraa32902a0",
  "eraa45027a0",
  "eraa45029a0",
  "eraa45031a0",
  "eraa34615a0",
  "eraa34616a0",
  "eraa45033a0",
  "eraa45038a0",
  "eraa45041a0",
  "eraa34618a0",
  "eraa34619a0",
  "eraa45028a0",
  "eraa45030a0",
  "eraa45032a0",
  "0r044109022",
  "1a936709012",
  "00991209012",
  "0b042009012",
  "0b042209012",
  "1a928809012",
  "0r044135032",
  "1a936735032",
  "00991235032",
  "0b042035032",
  "0b042235032",
  "1a928835032",
  "0r0441x0012",
  "1a9367x0022",
  "009912x0012",
  "0b0420x0012",
  "0b0422x0012",
  "1a9288x0012",
  "1a352524052",
  "10a3869x012",
  "10a3869x022",
  "gf05446x572",
  "17a2325x022",
  "10a0037x012",
  "40b3084x012",
  "11b5380x012",
  "30b3053x012",
  "31b0641x012",
  "30b3104x082",
  "30b3056x012",
  "30b3057x012",
  "10b3060x012",
  "10b3060x022",
  "20b3061x012",
  "1c4248x0212",
  "1c4248x0202",
  "1c4248x00a2",
  "1c4248x0062",
  "1c4248x0262",
  "1c4248x0252",
  "1c4248x0052",
  "1c4248x0182",
  "1c4248x0192",
  "10b3059x012",
  "10b3059x022",
  "1d687506992",
  "1n430406382",
  "1k786806992",
  "10b3058x012",
  "1h3671x0012",
  "20b3063x012",
  "30b3097x012",
  "10b3083x012",
  "10b3083x022",
  "10b7454x012",
  "1b2905x0012",

  "10b3089x012",
  "eraa51240a0",
  
  "eraa51241a1",
  "28b8832x012",
  "10b7449x012",
  "10b3069x012",
  "10b8735x012",
  "10b3068x012",
  "10b8736x012",
  "12b0178x012",
  "10b8736x022",
  "10b8735x042",
  "10b3068x022",
  "10b3069x032",
  "1d666428982",
  "10b3071x012",
  "12b0175x012",
  "10b7446x012",
  "10b7450x012",
  "10b6757x012",
  "1b541327022",
  "1j108506992",
  "1j1085x0042",
  "40b3086x012",
  "10b3093x012",
  "1d666625072",
  "20b3073x012",
  "1d667125072",
  "1d667728982",
  "10b3081x012",
  "10b3080x012",
  "20b3082x012",
  "1a391724052",
  "1a368324052",
  "1a3683x0062",
  "1a3917x0062",
  "1a346424052",
  "1a3464x0022",
  "10b3085x012",
  "1e264306992",
  "1e2643x0022",
  "10b3106x012",
  "1b290524052",
  "1c379124052",
  "10b7445x012",
  "1d682506992",
  "1n423906382",
  "30b3100x012",
  "22b0176x012",
  "1k877606992",
  "1c853806992",
  "1d8293t0022",
  "1a368228982",
  "1a767524662",
  "eraa32884a0",
  "ge29958x012",
  "30b3092_g",
  "30b3089_g",
  "1310161714",
  "38b4843_c",
  "30b6433_e",
  "30b6434_e",
  "5229323435",
  "31b5374_d",
  "31b9872_d"

        ]
        for word in words:
            if word in r667_actuator_spare:
                return True

        return False
    def __str__(self) -> str:
        return '627_fisher_spare'






class RFisher6350Series(AbstractFilter):

    def filter_passed(self, text: str):
        words= text.split()

        r667_actuator_spare=[
             "1k748527202",
  "14a9673x012",

  "1b788327022",
  "1e392527022",
 
  "d103153x012",

  "1b986027212",
  "14a9672x012",

  "15a9258x012",
  "25a6220x012",
  "20b9389x022",
  "1b798525062",
  "10b7192x012",
  "1a946324122",
  "1c724018992",
  "1c488226232",
  "1c4882x0032",
 
  "23b9152x012",
  "16a5929x042",
  "15a6218x012",

  "d100339x012",
  "d103091x012",


  "r6351x00012",
  "1b7971x0092",
  "1b7971x0342",
  "1b7971x0122",
  "18b6542x022",
  "18b6542x042",
  "18b6542x052",
  "18b6542x062",
  "20b9389x012",
  "20b9389x042",
  "29b9389x032",
  "1b797937022",
  "19a2860x012",
  "1b7980000b2",
  "1b7980x00a2",
  "1b7980000c2",
  "1h305028982",
  "t13305t0012",
  "10b2695x012",
  "10b2696x012",
 
  "16a5929x012",
  "16a5929x022",
  "r6352x00012",
  "r6353x00012",
  "r6354x00012",
  "35a6228x012",
  "17a8075x012",
  "39a5971x012",
  "17a8075x022",
  "28a9277x012",
  "15a6221x012",
  "15a6221x042",
  "15a6207x012",
  "15a6207x052",
  "15a6207x042",
  "15a6207x112",
  "15a6216x012",
  "15a6216x022",
  "15a6216x092",
  "15a6216x162",
  "15a6216x032",
  "15a6216x152",
  "15a6216x552",
  "15a6216x542",
  "15a6216x562",
  "15a6216x572",
  "15a6216x582",
  "1k748527022",
  "1k155828982",
  "15a6222x012",
  "15a6222x022",
  "10b3692x012",
  "10b6190x012",
  "1h2369x0032",
  "1c495704022",
  "1f113906992",
  "1n463906382",
  "10b6189x022",
  "1v4360x0022",
  "16a5929x052",
  "16a5929x032",
  "16a5929x072",
  "15a6202x032",
  "15a6202x022",
  "1d682506992",
  "1d6825x0012",
  "1c488238982",
  "17a2030x012",
  "17a2029x012",
  "15a9259x012",
  "10b4407x012",
  "19a6034x012",
  "1u7581x0022",
  "1l449635072",
  "0p077624102",
  "1l217544992",
  "1a329128982",
  "1e985428982",
  "1f125437012",
  "1b487099202",
  "1k885035072",
  "1f124801012",
  "1f124401012",
  "1f125236042",
  "1c752601012",
  "21b5621x012",
  "cb7988",
  "34a6635-b",
  "35a8889",
  "35a6236"
        ]
        for word in words:
            if word in r667_actuator_spare:
                return True

        return False
    def __str__(self) -> str:
        return '6350_fisher_spare'

texts=['regulator pressure 316 stainless steel fisher body',
       'cover terminal block o ring rosemount', 
       'seal electric actauator biffi',
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
       "gas chromatograph", 
       'daniel tube',
       'actuator diafragm fisher', 
       'bailey birkett valve', 
       'positioner dvc6200s', 
       'valve relief emerson jos', 
       'sensor submersion inserting range epdm o ring 3300ht-vp-12-30', 
       'kit spares regulator pilot valve tartarini', 
       'temperature detector 65 series', 
       'switch limit topworx',
       'mr95h filter emerson', 
       'multiflow regulator step groveley detection', 
       'flow control technologies valve', 
       "thrmowl:flg,1-1/2in,375mm insertion lg,1 thermowell: flanged,1-1/2in,375mm insertion lg,1/2in npt,w/ material certification,80mm,class 900/1500,rf,tapered thermowell:flg,375mm insertion lg,1-1/2in,class 900/1500,rf,1/2in anpt,tapered,80mm lagging lg emerson 0096a0375f64t080dq8r",
       "set:lead,field communicator 475,w/ conne set: lead,field communicator 475,w/ connector set:lead,475 field communicator,w/ connectors emerson 00375-0004-0001",
       "gauge,pres:dual scale,0 to 30 psig,0 to gauge,pressure: dual scale,0 to 30 psig,0 to 2 kg/cm2,stainless steel case gauge,pressure:dual scale,0-30 psig,ss case emerson 11b8583x032", 
       "pin:grooved,7/16in dia,3in lg,ss,asme sa pin: grooved,7/16in dia,3in lg,stainless steel,asme sa479/uns s31600,gr 316,hardness: 22 hrc pin:grooved,10mm dia,316 ss,f/ 10 & 12in type 24 v150 vee ball control valve emerson 11b8596x012",
       "ring,bk-up:uns s31803 ring,back-up: uns s31803 ring,back-up:uns s31803 emerson 11b9659x022", 
       "ring,scraper:wiper,30mm,40mm,7.5mm thk,n ring,scraper: wiper,30mm,40mm,7.5mm thk,nitrile,steel ring,wiper:valve,30 id x 40 od x 7.5mm thk,buna-n/stl emerson 1234722", 
       "kit:manifold to flange,20mm id x 25mm od kit: manifold to flange,20mm id x 25mm od x 3mm thk ptfe o-ring,12/set o-ring set:20 id x 25mm od,3mm thk,glass-filled teflon,12/set,304 manifold to flg emerson 03031-0019-0003", 
       "kit:rep,relay valve level controller,bal kit: relay valve,repair,level controller,consists of ball bearing assy,zinc ga glass gasket,relay base gasket,filter gasket,flappera                                                  ssy,f/ 2500 series high temp controller kit:relay valve,repair,level controller,consists of ball bearing assy,zinc ga glass gasket,relay base gasket,filter gasket,flapper assy,f/ 2500 series high temp controller fisher controls r2500x00h32", 
       "kit:replacement,rep,level controller,xmt kit: replacement,repair,level controller,transmitter,high temperature relay gasket,fisher kit:repair,replacement,level controller/transmitter,w/ relay gasket,high temp emerson rrelay-x0h22", 
       "rrelayx0h22",
       "transmitter,diff pres:coplanar,scalable transmitter,differential pressure: coplanar,scalable,4-20ma output,-250 to 250in wc,stainless steel flange bracket mount,10.5-42.4dc                                                  v,28dcv,stainless steel,hastelloy c276,lcd,atex,iso 15156,nace mr0175,cable entryd e t a i l :  m 2 0  c o n d u i t , f l a n g e  m a t e r i a l :  3 1 6  s t a i n l e s s  steel,pressure rating: 373m bar,w/ 030 5r c5 3b 11 be l8 q 8 ma ni f ol d transmitter,differential pressure: 373mbar range,4 to 20ma output,12 to 45vdc input,ss housing,28vdc max supply output,m20 conduit,3                                                 16 ss mounting bracket/flg,0305rc53b11bel8q8 manifold emerson 3051s2cd2a3a11a1kd4i1y2m5p1q4q8q15a1043", 
       "cover:electronics,316l ss,74.8 id x 82.4 cover: electronics,74.8 id x 82.4mm od,316l ss,o-ring cover:electronics,74.8 id x 82.4mm od,316l ss,o-ring 0351-9030-0002", 
       "kit:rep,level controller,arm gasket,2x c kit: repair,level controller,arm gasket,2x cotter spring,tube end gasket,torque tube assembly kit:repair,level controller,consists of torque tube assy,cotter spring,arm gasket,tube end gasket emerson r249x000012", 
       "gf02167x012", 
       "0802786 gasket kit", 
       "2218593", 
       "1h359428992 pipe tee, carbon steel", 
       "r377x000012 soft kit", 
       "r667x000722 soft kit", 
       "r67cfrx0012 kit rep", 
       "r82x0000022", 
       "ge00085x022", 
       "hsg31630173 thermowell", 
       "r4660xbtfj2 kit soft kit",
       "10b3085x012", 
       "r4660xtpc12", 
       "1k748527202"
       ]



results=['final_control',
         'measurement_tech',
         'pentair_tech',
         'pentair_tech',
         'pentair_tech', 
         'measurement_tech',
           "pentair_tech", 
           "measurement_tech", 
           "pentair_tech", 
           "final_control",
           "measurement_tech",
           "pentair_tech", 
           "pentair_tech", 
           "pentair_tech",
             "pentair_tech", 
             "measurement_tech", 
             'measurement_tech', 
             'final_control', 
             'pentair_tech', 
             'final_control', 
             'pentair_tech', 
             'measurement_tech', 
             'pentair_tech', 
             'measurement_tech', 
             'pentair_tech', 
             'final_control', 
             'measurement_tech', 
             'pentair_tech', 
             'measurement_tech', 
             'measurement_tech',
             "final_control", 
             "final_control",
             "final_control", 
             "final_control",
             "measurement_tech", 
             "final_control", 
             "final_control", 
             "final_control",
             "measurement_tech", 
             "measurement_tech",
             "final_control", 
             "final_control", 
             "final_control",
             "final_control", 
             "final_control", 
             "final_control", 
             "final_control", 
             "final_control", 
             "final_control", 
             "final_control",
             "measurement_tech", 
             "final_control",
             "final_control", 
             "final_control",
             "final_control"
             ]



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
   DanielFilter(), 
   FisherActuatorFilter(), 
   PositionerFilterDVC(), 
   ValveReliefFilter(), 
   Rosemount3300HTFilter(),
   TemperatureDetector(), 
   MR95HFilter(), 
   GroveleyDetectorFilter(), 
   Rosemount0096ThermowellFilter(), 
   Trex375FieldCommunicatorFilter(), 
   GenericFisherSpareFilter(),
   Actuator3025SpareFilter(), 
   RosemountManifoldSpare(),
   FisherSpare25002503(), 
   RosemountManifold(), 
   RousemountORingPackageFilter(),
   R249FisherSpareFilterr(),  
   R299HFisherSpareFilter(), 
   R1018SFisherSpare(), 
   R310A32AFisherSpare(), 
   R377TripValveSpare(), 
   R667ActuatorSpare(), 
   R67CRegulatorSpare(), 
   R546TransducerSpare(), 
   GeFisherSpareFilter(), 

   HSGTemperatureTransmitterFilter(), 
   RFisher4660Spare(), 
   RFishe667Spare(), 
   RFisher6350Series()
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


plt.figure(figsize=(150, 90))

plot_tree(dt, filled=True, feature_names=df.columns, fontsize=20, class_names=dt.classes_)
plt.savefig("decision_tree_plot.png")



# test_texts=['dear pentair_tech please quote below biffi seal kit', 
#             "kit: garlock style  body gasket,garlock style  cap gasket,garlock style  set screw gasket,3", 
#            'thermowell insertion stainless steel rosemount', 
#            "rosemount transmitter fisher", 
#            "globe valve ez series", 
#            "anderson greenwood manifold", 
#            "kit gas chromotograph rosemount", 
#            "kit: repair,type 81 4001psig sp-1 safety relief valve,vespel seat", 
#            "transmitter differential pressure transmitter", 
#            "kit soft goods pilot valve", 
#            "dear pentair_tech please quote below pressure transmitter similiar to crosby", 
#            'kit pilot pressure safety valve buna soft goods pentair', 
#            "transmitter", 
#            "kit overhaul repair rebuild gas chromatograph valve diaphragm", 
#            'dvc6200s positioner mounting kit', 
#            'valve relief jos',
#            'valve check 303ss body', 

#             ]





test_read_from=pd.read_csv('test.csv')
combined_text_list=[]
results=[]

for j in range(test_read_from.shape[0]):
    combined_text = ' '.join(str(test_read_from.iloc[j, i]) for i in range(test_read_from.shape[1])).lower()  # Assuming text is in the first column (index 0)
    combined_text_list.append(combined_text)



input_result_test={}
for feature in  features:
        input_result_test[str(feature)]=[feature.filter_passed(text) for text in combined_text_list]



predicted_values=(dt.predict(pd.DataFrame(input_result_test)))

combined_data = {**{'Combined Text': combined_text_list}, **input_result_test, 'Prediction': predicted_values}

result_df = pd.DataFrame(combined_data)

result_df.to_csv('output.csv', index=False)

print(result_df[135:145])

