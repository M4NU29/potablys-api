from fastapi import FastAPI, Query
from typing import Union
from model.model import predict_potability

app = FastAPI()

@app.get('/')
def read_root() -> dict[str, str]:
	return {"message": "Welcome to Potablys API"}

@app.get('/model')
def read_model(
	temperature: float,
  do: float = Query(..., ge=0, le=31),
  pH: float = Query(..., ge=2, le=14),
  conductivity: float = Query(..., ge=0, le=2000),
  bod: float = Query(..., ge=0, le=250),
  nitrate: float = Query(..., ge=0, le=900),
  fecalcaliform: float = Query(..., ge=0, le=900),
  totalcaliform: float = Query(..., ge=0, le=2000)
) -> dict[str, list[dict[str, Union[str, bool]]]]:
	return {
		"detail": [
			{
				"type": "prediction_result",
				"msg": bool(predict_potability(temperature, do, pH, conductivity, bod, nitrate, fecalcaliform, totalcaliform))
			}
		]
	}
