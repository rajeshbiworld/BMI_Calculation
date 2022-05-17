
import pandas as pd
import numpy as np

class BMICalculator:
  def __init__(self, survey_data):
    self.pandas_df = pd.DataFrame(survey_data)

  def add_bmi(self):
    self.pandas_df['BMI'] = self.pandas_df['WeightKg'] / (self.pandas_df['HeightCm'] ** 2) * 10000
    self.pandas_df['BMI'] = self.pandas_df['BMI'].round(2)

  def add_bmi_category(self):
    self.pandas_df['BMI Category'] = (
      np.where((self.pandas_df['BMI'] <= 18.4), 'Under Weight',
      np.where((self.pandas_df['BMI'] >= 18.5) & (self.pandas_df['BMI'] <= 24.9), 'Normal Weight',
      np.where((self.pandas_df['BMI'] >= 30) & (self.pandas_df['BMI'] <= 29.9), 'Over Weight',
      np.where((self.pandas_df['BMI'] >= 18.5) & (self.pandas_df['BMI'] <= 34.9),'Moderately Obese', 'Severly Obese'))))
    )

  def add_health_risk(self):
    self.pandas_df['Health Risk'] = (
      np.where(self.pandas_df['BMI Category'] == "Under Weight", 'Malnutrition Risk',
      np.where(self.pandas_df['BMI Category'] == "Normal Weight", "Low Risk",
      np.where(self.pandas_df['BMI Category'] == "Over Weight","Enhanced Risk",
      np.where(self.pandas_df['BMI Category'] == "Moderately Obese","Medium Risk",
      np.where(self.pandas_df['BMI Category'] == "Severly Obese","High Risk", "Very High Risk")))))
    )



survey_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]


bmi_output = BMICalculator(survey_data)
bmi_output.add_bmi()
bmi_output.add_bmi_category()
bmi_output.add_health_risk()


print(bmi_output.pandas_df)
