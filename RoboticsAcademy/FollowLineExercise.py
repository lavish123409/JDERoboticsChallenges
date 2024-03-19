from GUI import GUI
from HAL import HAL

import cv2
import numpy as np
from datetime import datetime
import time as tm
# Enter sequential code!

time = 0
integral = 0
time_prev = -1e-6
e_prev = 0

def PID(Kp, Ki, Kd, setpoint, measurement):
  global time, integral, time_prev, e_prev
  # Value of offset - when the error is equal zero
  offset = 0
  
  print(setpoint)
  print(measurement)
  
  # PID calculations
  e = setpoint - measurement
  print('error : ', e)
  P = Kp*e
  print('pk : ', P)
  dt = (time - time_prev) / 1000
  # integral = integral + Ki*e*dt
  integral = 0
  print('ik : ', integral)
  # print('time : ', time)
  # print('time_p : ', time_prev)
  D = Kd*(e - e_prev)/dt# calculate manipulated variable - MV
  print('dk : ', D)
  MV = offset + P + integral + D
  print('modified value : ', MV)
  # update stored data for next iteration
  e_prev = e
  time_prev = time
  time = datetime.now().microsecond
  return MV

while True:
    # Enter iterative code!
    img = HAL.getImage()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # print(hsv)
    
    lower = np.array([0, 100, 0])
    upper = np.array([90, 255, 255])
    
    mask = cv2.inRange(hsv, lower, upper)
    
    moments = cv2.moments(mask)
    
    # print(img.shape)
    c_x = 640 // 2
    
    try:
      c_x = int(moments['m10'] / moments['m00'])
    except ZeroDivisionError:
      print('m00 is 0')
      
    pid_value = PID(0.6, 0.2, 0.1, 317, c_x)
    print('c_x : ', c_x)
    print('cntrl : ', pid_value)
    
    # if pid_value > c_x:
    #   # move right
    #   HAL.setW(0.3)
    # elif pid_value < c_x:
    #   #move left
    #   HAL.setW(-0.3)
    HAL.setV(1)
    HAL.setW(0.01 * pid_value)
    
    GUI.showImage(mask)
    # tm.sleep(3)