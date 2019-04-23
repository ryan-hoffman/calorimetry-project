# -*- coding: utf-8 -*-
#
# calorimetryCalculator.py: a simple class to calculate heat transfer
#
# from https://en.wikipedia.org/wiki/Calorimetry:
#
# Calorimetry is the science or act of measuring changes in state variables of a body for the
# purpose of deriving the heat transfer associated with changes of its state due, for example, to
# chemical reactions, physical changes, or phase transitions under specified
# constraints. Calorimetry is performed with a calorimeter. The word calorimetry is derived from the
# Latin word calor, meaning heat and the Greek word μέτρον (metron), meaning measure. Scottish
# physician and scientist Joseph Black, who was the first to recognize the distinction between heat
# and temperature, is said to be the founder of the science of calorimetry.
#
#----------------------------------------------------------------------------------------------------
import pdb   # debugger
#----------------------------------------------------------------------------------------------------
class CalorimetryCalculator:

   sample_name = None
   start_temp = None
   end_temp = None
   water_mass = None
   start_weight = None
   end_weight = None

   def __init__(self, sample_name, start_temp, end_temp, water_mass, start_weight, end_weight):

      self.sample_name = sample_name
      self.start_temp = start_temp
      self.end_temp = end_temp
      self.water_mass = water_mass
      self.start_weight = start_weight
      self.end_weight = end_weight

   def validObject(self):
     goodName = len(self.sample_name) > 0
     goodStartingTemp = isinstance(self.start_temp, (int, float))
     goodEndingTemp = isinstance(self.end_temp, (int, float))
     goodWaterMass = isinstance(self.water_mass, (int, float)) and (self.water_mass > 0)
     goodStartingWeight = isinstance(self.start_weight, (int, float)) and (self.start_weight > 0)
     goodEndingWeight = isinstance(self.end_weight, (int, float)) and (self.end_weight > 0)
     allTests = [goodName, goodStartingTemp, goodEndingTemp, goodWaterMass, goodStartingWeight, goodEndingWeight]
     return(all(allTests))

   def show(self):

       print("--- a CalorimetryCalculator object with these values:")
       print("sample_name: %s" % self.sample_name)
       print("start_temp: %f" % self.start_temp)
       print("end_temp: %f" % self.end_temp)
       print("water_mass: %f" % self.water_mass)
       print("start_weight: %f" % self.start_weight)
       print("end_weight: %f" % self.end_weight)


   def calculate(self):

        delta_temp = self.end_temp - self.start_temp
        constant = float(1)
        mass = self.water_mass
        Q = mass * constant * delta_temp
        cal = Q
        C = cal/1000
        return(C)





