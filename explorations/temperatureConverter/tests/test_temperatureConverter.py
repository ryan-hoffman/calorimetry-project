# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from temperatureConverter import *
#----------------------------------------------------------------------------------------------------
def runTests():

    test_constructor()
    test_constructorWithBadData()
    test_calculation()

#----------------------------------------------------------------------------------------------------
def test_constructor():

    print("--- test_constructor")

    converter = TemperatureConverter(fahrenheit=70, centigrade=30)
    assert(converter.validObject())

#----------------------------------------------------------------------------------------------------
def test_constructorWithBadData():

    print("--- test_constructorWithBadData")

    converter = TemperatureConverter("seventy degrees F", "yabba dabba doo!")
    assert(not converter.validObject())

#----------------------------------------------------------------------------------------------------
def test_calculation():

    print("--- test_calculation")
    converter = TemperatureConverter(70, 30)
    converted_centigrade = converter.toCentigrade()
    converted_fahrenheit = converter.toFahrenheit()
    assert(converted_centigrade == 21 and converted_fahrenheit == 86)

#----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    runTests()

