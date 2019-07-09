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
class TemperatureConverter:

   fahrenheit = None

   def __init__(self, fahrenheit):

      self.fahrenheit = fahrenheit

   def validObject(self):
     validDataType = isinstance(self.fahrenheit, (int, float))
     validRange = self.fahrenheit > - 459.67 & self.fahrenheit < 1000000
     allTests = [validDataType, validRange]
     return(all(allTests))

   def show(self):

       print("--- a TemperatureConverter object with these values:")
       print("initial fahrenheit value: %s" % self.fahrenheit)

   def toCentrigrade(self):

        centigrade = (self.fahrenheit - 32.0) * 5 / 9
        return(centigrate)





