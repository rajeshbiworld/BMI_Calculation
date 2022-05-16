import pandas as pd
import numpy as np

survey_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

#Converting List to Pandas DataFrame
pandas_df = pd.DataFrame(survey_data)

#Adding additional columns to existing Pandas DataFrame

pandas_df['BMI'] = pandas_df['WeightKg']/(pandas_df['HeightCm']**2)*10000

pandas_df['BMI Category'] = np.where((pandas_df['BMI'] <= 18.4),'Under Weight',
                            np.where((pandas_df['BMI'] >= 18.5) & (pandas_df['BMI'] <= 24.9),'Normal Weight',  
                            np.where((pandas_df['BMI'] >= 30) & (pandas_df['BMI'] <= 29.9),'Over Weight',
                            np.where((pandas_df['BMI'] >= 18.5) & (pandas_df['BMI'] <= 34.9),'Moderately Obese','Severly Obese'))))

pandas_df['Health Risk'] =  np.where(pandas_df['BMI Category'] == "Under Weight" , 'Malnutrition Risk',
                            np.where(pandas_df['BMI Category'] == "Normal Weight", "Low Risk",
                            np.where(pandas_df['BMI Category'] == "Over Weight", "Enhanced Risk",
                            np.where(pandas_df['BMI Category'] == "Moderately Obese", "Medium Risk",
                            np.where(pandas_df['BMI Category'] == "Severly Obese", "High Risk",  "Very High Risk")))))                                   

pandas_df.round(2)

print(pandas_df)