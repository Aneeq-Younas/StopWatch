import os    
import time  
import random  
second = 0    
minute = 0    
hours = 0  
Runway_empty = True
Landing_number = 0
Takeoff_number = 0
Landing_time =0
Takeoff_time = 0
totaltakeoff_time = 0
totallanding_time=0
Landing_Rate = 0
Takeoff_Rate = 0
Landing_queue = 0
Takeoff_queue = 0
number1 =0
number2 =0
minutes_pause = 0
takeoff_average = 0
landing_average = 0

def gen(a,b): 
  display_number = random.randint(a,b)
  return display_number
  
def Limit():
    global Landing_Rate , Takeoff_Rate
    Landing_Rate = gen(0,30)
    Takeoff_Rate = gen(0,30)
    
def timecalculator():
    fig= gen(1,3)
    return fig


def landing():
    global Landing_queue , totallanding_time, minutes_pause, Runway_empty , landing_average , Landing_number
    Landing_queue =  +1
    Landing_time = timecalculator()
    totallanding_time = totallanding_time + Landing_time
    minutes_pause = minutes_pause + Landing_time
    Runway_empty = False
    Landing_number =  Landing_number  +1
    landing_average = totallanding_time / Landing_number

def takeoff():
    global Takeoff_queue , totaltakeoff_time , minutes_pause , Runway_empty , takeoff_average , Takeoff_number
    Takeoff_queue =  +1
    Takeoff_time=timecalculator()
    totaltakeoff_time = totaltakeoff_time + Takeoff_time
    minutes_pause = minutes_pause + Takeoff_time
    Runway_empty = False
    Takeoff_number = Takeoff_number +1
    takeoff_average = totaltakeoff_time / Takeoff_number
        
   
   


def ratecalculater():
    global number1 , number2, Landing_Rate , Takeoff_Rate  
     
    number1 = gen(0,1)
    number2 = gen(0,1)
    if number1 < Landing_Rate:
        landing()  
    if number2 < Takeoff_Rate:
        takeoff()
   
    
        
        




Limit()
while(True):
    print('\t\t\t\t\t\t\t\t  %d : %d : %d '%(hours,minute,second))   
    print("average time a plane spends in the takeoff queue" , takeoff_average )
    print( "average time a plane spends in the landing queue" ,landing_average )
    print( "average length of the landing queue" ,Landing_number )
    print("average length of the takeoff queue" ,  Takeoff_number)
    time.sleep(1)    
    second+=1    
    if(second == 60):    
        second = 0    
        minute+=1 
        if minute >= minutes_pause:
            ratecalculater()
            Runway_empty = True
            Landing_queue = Landing_queue -1
            Takeoff_queue = Takeoff_queue - 1
        
    
    
    if(minute == 60):    
        minute = 0    
        hours+=1  
        Limit() 
        landing_queue = 0
        takeoff_queue = 0 
    os.system('cls')





    