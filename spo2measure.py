import random
class Spo2Measure:
    def __init__(self):
        self.detectPulseOximeter()

    #method for simulating detecting result
    def  detectPulseOximeter(self):
     #put code here for sensor spo2 measurement
     self.spo2=random.randint(85,100)
     self.pulseRate=random.randint(60,100)
     self.perfusionIndex=random.uniform(0.2,2.0)

    #To measure spo2
    #return spo2 and status two value as number and string
    def spo2Measurement(self):
       status="";
       print("Spo2 Measurement Result")
       print("SpO2: {}%".format(self.spo2))
       print("Pulse rate: {} bpm".format(self.pulseRate))
       print("Perfusion index: {}".format(self.perfusionIndex))

       if self.spo2 >= 95 and self.pulseRate >= 60 and self.pulseRate <= 100:
         print("Your SpO2 level is normal.")
         status="Normal"
       elif self.spo2 >= 90 and self.spo2 < 95 and self.pulseRate >= 60 and self.pulseRate <= 100:
         print("SpO2 level is slightly low .")
         status="Warning"
       elif self.spo2  < 90 or self.pulseRate < 60 or self.pulseRate > 100:
          status="Danger"
          print("SpO2 level is low and do medical treatment immediately")
       
       return self.spo2,status
     
    def spo2Info(self):
        status="";
        if self.spo2 >= 95 and self.pulseRate >= 60 and self.pulseRate <= 100:
        # print("Your SpO2 level is normal.")
         status="Normal"
        elif self.spo2 >= 90 and self.spo2 < 95 and self.pulseRate >= 60 and self.pulseRate <= 100:
        # print("SpO2 level is slightly low .")
         status="Warning"
        elif self.spo2  < 90 or self.pulseRate < 60 or self.pulseRate > 100:
          status="Danger"
         # print("SpO2 level is low and do medical treatment immediately")
        return self.spo2,status
    
