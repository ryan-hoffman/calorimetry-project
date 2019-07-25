# -*- coding: utf-8 -*-
#
#----------------------------------------------------------------------------------------------------
import pdb   # debugger
#----------------------------------------------------------------------------------------------------
class TemperatureConverter:

   fahrenheit = None
   centigrade = None

   def __init__(self, fahrenheit, centigrade):

      self.fahrenheit = fahrenheit
      self.centigrade = centigrade

   def validObject(self):
     validDataType = isinstance(self.fahrenheit, (int, float)) or isinstance(self.centigrade, (int,float))
     if(not validDataType):
        return(False)
     validRange = self.fahrenheit > -459.67 and self.fahrenheit < 1000000 or self.centigrade > -273 and self.centigrade < 555538
     allTests = [validDataType, validRange]
     return(all(allTests))

   def show(self):

       print("--- a TemperatureConverter object with these values:")
       print("initial fahrenheit value: %s" % self.fahrenheit)
       print("initial centigrade value: %s" % self.centigrade)

   def toCentigrade(self):

        converted_centigrade = (self.fahrenheit - 32.0) * 5 / 9
        return(round(converted_centigrade))

   def toFahrenheit(self):

        converted_fahrenheit = (self.centigrade * 9/5) + 32
        return(round(converted_fahrenheit))





