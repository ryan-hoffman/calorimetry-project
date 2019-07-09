# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from calorimetryCalculator import *
#----------------------------------------------------------------------------------------------------
def runTests():

    test_constructor()
    test_constructorWithBadData()
    test_calculation()

#----------------------------------------------------------------------------------------------------
def test_constructor():

    print("--- test_constructor")

    calculator = CalorimetryCalculator(sample_name = "unitTest sample",
                                       start_temp = 32,
                                       end_temp = 100,
                                       water_mass = 24,
                                       start_weight = 10,
                                       end_weight = 2)
    assert(calculator.validObject())

#----------------------------------------------------------------------------------------------------
def test_constructorWithBadData():

    print("--- test_constructorWithBadData")

    calculator = CalorimetryCalculator(sample_name = "unitTest sample",
                                       start_temp = 32,
                                       end_temp = 100,
                                       water_mass = 24,
                                       start_weight = -10,
                                       end_weight = 2)
    assert(not calculator.validObject())

#----------------------------------------------------------------------------------------------------
def test_calculation():

    print("--- test_calculation")
    calculator = CalorimetryCalculator(sample_name = "unitTest sample",
                                       start_temp = 32,
                                       end_temp = 100,
                                       water_mass = 24,
                                       start_weight = 10,
                                       end_weight = 2)
    heatTransfer = calculator.calculate()
    assert(heatTransfer == 1.632)

#----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    runTests()

