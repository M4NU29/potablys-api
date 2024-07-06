import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras.models import load_model

model = load_model('.\best_model.keras')

def predict_potability(temperature: float, do: float, pH: float, conductivity: float, bod: float, nitrate: float, fecalcaliform: float, totalcaliform: float) -> int:
  training_df = pd.read_csv('.\training_data.csv')

  scaler = StandardScaler()
  scaler.fit(training_df[['Temperature', 'D.O','pH','Conductivity', 'B.O.D','Nitrate', 'Fecalcaliform','Totalcaliform']])

  input_data = np.array([temperature, do, pH, conductivity, bod, nitrate ,fecalcaliform, totalcaliform]).reshape(1, -1)
  input_data_scaled = scaler.transform(input_data)

  result = model.predict(input_data_scaled)

  return (result >= 0.5).astype(int)
