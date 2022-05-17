import pytest
import bmi as bmi


# Mocking Test Data

# test_data = [{"Gender": "Male", "HeightCm": 172, "WeightKg": 85 }]
# Expected Output for above test data, BMI: 28.73,BMI Category: Moderately Obese, Health Risk:

# Functions to do Unit Test in Pytest module

def test_bmi():
    test_data = [{"Gender": "Male", "HeightCm": 172, "WeightKg": 85}]
    test_output = bmi.BMICalculator(test_data)
    test_output.add_bmi()
    assert test_output.pandas_df['BMI'][0] == 28.73


def test_bmi_category():
    test_data = [{"Gender": "Male", "HeightCm": 172, "WeightKg": 85}]
    test_output = bmi.BMICalculator(test_data)
    test_output.add_bmi()
    test_output.add_bmi_category()
    assert test_output.pandas_df['BMI Category'][0] == 'Moderately Obese'


def test_health_risk():
    test_data = [{"Gender": "Male", "HeightCm": 172, "WeightKg": 85}]
    test_output = bmi.BMICalculator(test_data)
    test_output.add_bmi()
    test_output.add_bmi_category()
    test_output.add_health_risk()
    assert test_output.pandas_df['Health Risk'][0] == 'Medium Risk'
