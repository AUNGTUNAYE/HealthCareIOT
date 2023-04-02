import time
import random
class BpmMeasure:
    def __init__(self) -> None:
        pass

    def measureBpm(self):
       print("--start measuring--")
       startTime = time.time()  # assign start time
       heartbeats = 0  # set heartbeats to 0
       while time.time() - startTime < 10:
        # although this code use random as value for heartbeat,it should accept data from sensor
          heartbeats += random.randint(0,2)
          time.sleep(1)
          print("---measuring heart beat .pls wait---")
       
       print("heartbeat:",heartbeats)
       
       # calculate BPM
       duration = time.time() - startTime
       print("duration",duration)
       bpm = self.calculateBpm(heartbeats, duration)
       return bpm
    
    def bpmInfo(self):
       startTime = time.time()  # assign start time
       heartbeats = 0  # set heartbeats to 0
       while time.time() - startTime < 10:
        # although this code use random as value for heartbeat,it should accept data from sensor
          heartbeats += random.randint(0,2)
          time.sleep(1)
          print(".")
       # calculate BPM
       duration = time.time() - startTime
       bpm = self.calculateBpm(heartbeats, duration)
       return bpm
       
    def calculateBpm(self,heartBeats,duration):
      return 60 * (heartBeats / duration)