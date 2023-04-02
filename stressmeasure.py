import time
import random
from bpmmeasure import BpmMeasure
class StressMeasure:
    def __init__(self) -> None:
        pass
    
    #simulation method for skin conductance
    #return random skin value as Integer
    def measureSkinConductance(self):
     # although using random in simulation ,replace this code to accept sensor value
     return random.randint(1, 10)

    #To measure stress level
    #return stressLevel as string
    def measureStessLevel(self):
       restHrBpm=BpmMeasure().measureBpm()
       #print("Rest hr bpm is ",restHrBpm)

       restHrSkin=self.measureSkinConductance()
      # print("Rest hr Skin Conductance is ",restHrSkin)

       postHrBpm=BpmMeasure().measureBpm()
       #print("Current hr bpm is ",postHrBpm)

       postHrSkin=self.measureSkinConductance()
      # print("Current hr Skin Conductance is ",postHrSkin)

       stressLevel=""
       if postHrBpm > restHrBpm + 20 and postHrSkin - restHrSkin >= 3:
          stressLevel = "High"
          print("Stress level is high")
       elif postHrBpm > restHrBpm + 20  and postHrSkin - restHrSkin >= 1:
          stressLevel = "Moderate"
          print("Stress level is Moderate")
       else:
          stressLevel = "Low"
          print("Stress level is Normal")
      
       return stressLevel   
    
    #To measure Stress level
    #return stresslevel as String
    def measureStessInfo(self):
       restHrBpm=BpmMeasure().bpmInfo()
       restHrSkin=self.measureSkinConductance()
       postHrBpm=BpmMeasure().bpmInfo()
       postHrSkin=self.measureSkinConductance()
       stressLevel=""
       if postHrBpm > restHrBpm + 20 and postHrSkin - restHrSkin >= 3:
          stressLevel = "High"
       elif postHrBpm > restHrBpm + 20  and postHrSkin - restHrSkin >= 1:
          stressLevel = "Moderate"
       else:
          stressLevel = "Low"
       return stressLevel   
