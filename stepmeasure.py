import time
import random
class StepMeasure:
    def __init__(self) -> None:
        pass
    #To measure step and record 
    #return step as integer
    def measureStep(self):
       print("--start walking--")
       startTime = time.time()  # assign start time
       step = 0  # set heartbeats to 0
       count=0
       status=True
       while status:
        # although this code use random as value for heartbeat,it should accept data from sensor
          step += random.randint(5,15) 
          print("---Walking Steps "+str(step)+"---")
          time.sleep(1)  
          count+=1
          if count==5:
              count=0
              key=input("Do you want to stop measuring walking step?Type y for yes and n for no : ")
              
              if key=='n':
                  continue
              else:
                  print("Walking Finished.Total Step is "+ str(step))
                  status=False
       return step
    
    def stepInfo(self):
       #replace with sensor code
       step =  random.randint(100, 1000) 
       return step
    
    