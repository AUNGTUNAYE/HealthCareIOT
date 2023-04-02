from datetime import datetime
import time
from bpmmeasure import BpmMeasure
from stepmeasure import StepMeasure
from stressmeasure import StressMeasure
from spo2measure import Spo2Measure

healthOverView={"bpm":0,"step":0,"stresslevel":"","spo2":0,"spo2result":""}
firstTime=0

#for measuring bpm ,spo2 ,steps and stress
def dashBoard():
  if firstTime==0:
    print("Wait for overall result")
    #calling measure result
    bpm= BpmMeasure()
    healthOverView["bpm"]=round(bpm.bpmInfo())#store bpm data in healthOverview dictionary
    #calling step method
    healthOverView["step"]= healthOverView["step"]+StepMeasure().stepInfo()
    #calling stress measure
    stressLevel=StressMeasure().measureStessInfo()
    healthOverView["stresslevel"]=stressLevel   #store stess data in healthOverview dictionary 
    #calling spo2 measure1
    spo2data,spo2result=Spo2Measure().spo2Info()
    healthOverView["spo2"]=spo2data #store spo2 data in healthOverview dictionary
    healthOverView["spo2result"]=spo2result
  print("----Over All Heatlh Status---")
  #loop to show information for healthoverview
  for key in healthOverView:
    print(key, ' : ', healthOverView[key])
  print("-------- Main Menu ---------")
  print("0.Exit")
  print("1.Health Care Measurement Menu")
  command=int(input("Type number for actions"))
  return command

#for displaying main menu
def mainMenu():
  print("-------- HealthCare Measurement Menu ---------")
  print("Type Number of Menu No to execute Health Care Measurement ")
  print("0.Back to OverAll")
  print("1.BPM")
  print("2.Steps")
  print("3.Stress ")
  print("4.Spo2 ")
  command=int(input("Type number for actions"))
  return command
 
#for authenticating user who use system
def login(uname,pwd): 
 account=[{"username":"admin","password":"12345678","name":"Aung Tun Aye"},
          {"username":"aya","password":"12345678","name":"Aung Tun "},
           {"username":"test","password":"test","name":"Test User"}
         
         ] 
#loop account list for matching with user name and password which user enter and
#store vale from list 
 for data in account:
   if data["username"]==uname and data["password"]==pwd:
     return data["name"],True
 return "Invalid Login",False 

#for displaying BPM Measurement Ui  
def bpmUi():
     print("---- Measure BPM -----")
     bpm= BpmMeasure()
     result=bpm.measureBpm()
     print("BPM ",result)
     healthOverView["bpm"]=round(result)

    

b=True
print("-----------------Welcome to Health Care Stimulation Program---------")
loginstatus=False
level=0 
#loop will run until user choose exit
while b==True:
  #use loginstatus for checking valid user or not 
  if loginstatus==False:
   username=input("Please enter user name(example test) :")
   password=input("Please enter Password( example test) :")
   #login method return two value one is loginstatus and another is name of user or error
   name,loginstatus=login(username,password)
   if loginstatus==False:
      print(name)
      continue
  else:
    #for dashboard
    if level==0:
      command=dashBoard()
      if command==0:
        level=0
        break
      else:
        level=1
    else:
      number=mainMenu()
      if(number==0):
       level=0
       #command=dashBoard()
      elif number==1:
        bpmUi()
        number=mainMenu()
      elif number==2:
        stepResult=StepMeasure().measureStep()
        healthOverView["step"]=stepResult
     
      elif number==3:
        print("---Measure Stress Level----")
        stressLevel=StressMeasure().measureStessLevel()
        healthOverView["stresslevel"]=stressLevel

      elif number==4:
        print("---Measure SPO2 and result----")
        spo2,spo2result=Spo2Measure().spo2Measurement()
        healthOverView["spo2"]=spo2
        healthOverView["spo2result"]=spo2result


      
