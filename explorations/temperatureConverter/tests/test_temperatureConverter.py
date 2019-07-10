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

    converter = TemperatureConverter(fahrenheit=70)
    assert(converter.validObject())

#----------------------------------------------------------------------------------------------------
def test_constructorWithBadData():

    print("--- test_constructorWithBadData")

    converter = TemperatureConverter("seventy degrees F")
    assert(not converter.validObject())

#----------------------------------------------------------------------------------------------------
def test_calculation():

    print("--- test_calculation")
    converter = TemperatureConverter(70)
    centigrade = converter.toCentigrade()
    assert(centigrade == 21)

#----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    runTests()

