from GUI import GUI
from HAL import HAL

import sys

import cv2
import numpy as np
from datetime import datetime
import time as tm
import math
# Enter sequential code!


def parse_laser_data (laser_data):
    laser = []
    i = 0
    while (i < 180):
        dist = laser_data.values[i]
        if dist > 10:
            dist = 10
        angle = math.radians(i-90) # because the front of the robot is -90 degrees
        laser += [(dist, angle)]
        i+=1
    return laser
    
def absolute2relative (x_abs, y_abs, robotx, roboty, robott):

    # robotx, roboty are the absolute coordinates of the robot
    # robott is its absolute orientation
    # Convert to relatives
    dx = x_abs - robotx
    dy = y_abs - roboty

    # Rotate with current angle
    x_rel = dx * math.cos (-robott) - dy * math.sin (-robott)
    y_rel = dx * math.sin (-robott) + dy * math.cos (-robott)

    return x_rel and y_rel
    
# Function to calculate angular velocity with dynamic damping adjustment
def calculate_angular_velocity(car_vector, k_angle, damping_factor_base, obstacle_magnitude_threshold, f):
    # sign = abs(car_vector[0]) / car_vector
    # Calculate the magnitude of the obstacle vector
    # obstacle_magnitude = np.linalg.norm(car_vector)
    obstacle_magnitude = car_vector[0]
    # f.write("obs mag : " + str(obstacle_magnitude) + " -> ")
    print("obs mag : ", obstacle_magnitude)
    
    # Adjust damping based on obstacle magnitude
    if abs(obstacle_magnitude) < obstacle_magnitude_threshold:
        damping_factor = damping_factor_base * (obstacle_magnitude_threshold / obstacle_magnitude)
    else:
        damping_factor = damping_factor_base
    
    # Calculate damped angular velocity
    angular_velocity = k_angle * car_vector[0]
    # f.write("func angv : " + str(angular_velocity) + " = ")
    print('damp factor : ', damping_factor)
    
    damped_angular_velocity = angular_velocity - damping_factor * angular_velocity
    # f.write("func damped angv : " + str(damped_angular_velocity) + "\n")
    
    return damped_angular_velocity

    
def solve(i : int):
    with open('out.txt', 'a') as f:
      # f.write(str(i) + '----------------------------------------------------------------------------------------------' + '\n')
      currentTarget = GUI.map.getNextTarget()
      targetx = currentTarget.getPose().x
      targety = currentTarget.getPose().y
      
      GUI.map.targetx = currentTarget.getPose().x
      GUI.map.targety = currentTarget.getPose().y

      roboPos_x = HAL.getPose3d().x
      roboPos_y = HAL.getPose3d().y
      
      GUI.map.posx = roboPos_x
      GUI.map.posy = roboPos_y

      k_obs = -0.5
      k_car = 0.1
      k_target = -0.4

      target_vector = [targetx - roboPos_x, targety - roboPos_y]
      rot_angle = (-1) * (HAL.getPose3d().yaw + math.pi / 2)

      target_vector = [
          target_vector[0] * math.cos(rot_angle) - target_vector[1] * math.sin(rot_angle),
          target_vector[0] * math.sin(rot_angle) + target_vector[1] * math.cos(rot_angle),
        ]
      
      target_vector[0] = k_target * target_vector[0]
      target_vector[1] = k_target * target_vector[1]

      obs_vector = [0, 0]
      angle = 180
#      f.write(str(HAL.getLaserData()) + '\n')

      # f.write(str(parse_laser_data(HAL.getLaserData())))
      # for r, angle in parse_laser_data(HAL.getLaserData()):
        # f.write("{:.2f} -> {:.6f}\n".format(math.degrees(angle), r))
      
      rang = 0
      lang = 0
      for r, angle in parse_laser_data(HAL.getLaserData()):
        # if r > 1:
        if angle < 0:
          rang += r
        else:
          lang += r
        if angle > math.radians(-45) and angle < math.radians(45):
          # obs_vector[0] += k_obs * (100 / (r ** 2)) * math.cos(angle) * (abs(angle) / angle) if angle != 0 else 1
          # obs_vector[0] += k_obs * (100 / ((r / 2) ** 2 + 1)) * math.sin(angle)
          # obs_vector[0] += k_obs * (100 / ((r / 1.2) ** 2 + 1)) * (1 - math.sin(angle))
          obs_vector[0] += k_obs * (100 / ((r) ** 2 + 1)) * (math.cos(angle)) * (abs(angle) / angle) if angle != 0 else 1
          # f.write('inrange  -> ' + str(100 / (r ** 2)) + ' , ' + str(k_obs * (100 / (r ** 2)) * math.cos(angle)) + ' = ')
          # f.write('inrange  -> ' + str(100 / (r ** 2)) + ' , ' + str(k_obs * (100 / (r ** 2)) * math.sin(angle)) + ' = ')
        else:
          # obs_vector[0] += k_obs * (10 / (r ** 2)) * math.cos(angle) * (abs(angle) / angle) if angle != 0 else 1
          # obs_vector[0] += k_obs * (10 / ((r / 2) ** 2 + 1)) * math.sin(angle)
          # obs_vector[0] += k_obs * (10 / ((r / 1.2) ** 2 + 1)) * (1 - math.sin(angle))
          obs_vector[0] += k_obs * (10 / ((r) ** 2 + 1)) * (math.cos(angle)) * (abs(angle) / angle) if angle != 0 else 1
          # f.write('outrange  -> ' + str(10 / (r ** 2)) + ' , ' + str(k_obs * (10 / (r ** 2)) * math.cos(angle)) + ' = ')
          # f.write('outrange  -> ' + str(10 / (r ** 2)) + ' , ' + str(k_obs * (10 / (r ** 2)) * math.sin(angle)) + ' = ')
        # f.write(str(math.degrees(angle)) + ' : ' + str(r) + ' => ' + str(obs_vector[0]) + '\n')
        # print(str(math.degrees(angle)) + ' , ' + str(math.sin(angle)) + ' : ' + str(r) + ' => ' + str(obs_vector[0]) + '\n')

      # f.write('right angle : ' + str(rang) + '\n')
      # f.write('left angle : ' + str(lang) + '\n')
      
      # for r in HAL.getLaserData().values:
      #   if angle > 90:
      #     rang += r
      #   else
      #     lang += r
      #   if angle > 45 and angle < 135:
      #     obs_vector[0] += k_obs * (100 / (r ** 2)) * math.cos(math.radians(angle))
      #   else:
      #     obs_vector[0] += k_obs * (10 / (r ** 2)) * math.cos(math.radians(angle))
      # f.write('right angle : ' + str(rang) + '\n')
      # f.write('left angle : ' + str(lang) + '\n')

      print('real obs vector : ', str(obs_vector))
      # if(abs(obs_vector[0]) > 20):
      #   obs_vector[0] = 20 * (abs(obs_vector[0]) / obs_vector[0])
      obs_vector = np.clip(obs_vector, a_min=-2000.0, a_max=2000.0)
      obs_vector = np.interp(obs_vector, [-2000.0, 2000.0], [-20.0, 20.0])
      
      # if(abs(obs_vector[0]) < 0.5):
      #   obs_vector[0] = 0

      car_vector = [0,0]

      car_vector[0] = k_car * (target_vector[0] + obs_vector[0])
      car_vector[1] = k_car * (target_vector[1] + obs_vector[1])
      
      print('obs vector : ', str(obs_vector))
      print('car vector : ', str(car_vector))
      print('target vector : ', str(target_vector))
      # f.write('car vector : ' + str(car_vector) + '\n')
      # f.write('obs vector : ' + str(obs_vector) + '\n')
      # f.write('target vector : ' + str(target_vector) + '\n')

      # HAL.setV(car_vector[1])
      HAL.setV(3)

      k_angle = 0.3
      # angular_velocity = k_angle * car_vector[0]
      # HAL.setW(angular_velocity - 0.4 * angular_velocity)
      angv = calculate_angular_velocity(obs_vector, k_angle, 0.2, 1.5, f)
      # f.write('angv : ' + str(angv) + '\n')
      print('angv : ', angv)
      HAL.setW(angv)
      # HAL.setW(1)
      
      # Car direction
      GUI.map.carx = -car_vector[1]
      GUI.map.cary = car_vector[0]
      
      # Obstacles direction
      GUI.map.obsx = -obs_vector[1]
      GUI.map.obsy = obs_vector[0]
      
      # Average direction
      GUI.map.avgx = -car_vector[1]
      GUI.map.avgy = car_vector[0]
      
      # Current target
      GUI.map.targetx = -targety
      GUI.map.targety = targetx
      # GUI.map.carx = 1
      # GUI.map.cary = 0
      
      # # Obstacles direction
      # GUI.map.obsx = 1
      # GUI.map.obsy = -1
      
      # # Average direction
      # GUI.map.avgx = 1
      # GUI.map.avgy = 1
      
      # # Current target
      # GUI.map.targetx = 0
      # GUI.map.targety = 1

with open('out.txt', 'w') as f:
  f.write('') 
# solve()
# currentTarget = GUI.map.getNextTarget()
# GUI.map.targetx = currentTarget.getPose().x
# GUI.map.targety = currentTarget.getPose().y

# obs_vector = [0, 0]
# angle = 180
# # print(HAL.getLaserData().values)

# for r in HAL.getLaserData().values:
#   if angle > 45 or angle < 135:
#     obs_vector[0] += k_obs * (100 / (r ** 2)) * math.cos(math.radians(angle))
#   else:
#     obs_vector[0] += k_obs * (100 / (r ** 2)) * math.cos(math.radians(angle))
#   angle -= 1

# if(obs_vector[0] > 20):
#   obs_vector[0] = 20 * (abs(obs_vector[0]) / obs_vector[0])
  
# # Obstacles direction
# GUI.map.obsx = obs_vector[0]
# GUI.map.obsy = obs_vector[1]

# print('car vector : ', car_vector)
# print('obs vector : ', obs_vector)
# print('target vector : ', target_vector)

i = 0
while True:
    # Enter iterative code!
    # solve()
    x = 1
    # HAL.setV(0)
    # HAL.setW(0)
    
    # print(HAL.getLaserData())
    
    i += 1
    print(i)
    solve(i)
    # if i >= 1:
    #   sys.exit()