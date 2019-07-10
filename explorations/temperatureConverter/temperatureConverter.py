# -*- coding: utf-8 -*-
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
     if(not validDataType):
        return(False)
     validRange = self.fahrenheit > -459.67 and self.fahrenheit < 1000000
     allTests = [validDataType, validRange]
     return(all(allTests))

   def show(self):

       print("--- a TemperatureConverter object with these values:")
       print("initial fahrenheit value: %s" % self.fahrenheit)

   def toCentigrade(self):

        centigrade = (self.fahrenheit - 32.0) * 5 / 9
        return(round(centigrade))





