import csv
from fastapi import FastAPI, Query, File, UploadFile
from io import StringIO
from model.model import predict_potability
from typing import Iterator

app = FastAPI()

@app.get('/')
def read_root() -> dict[str, list[dict[str, str]]]:
	return {
		"detail": [
			{
				"type": "welcome_message",
				"msg": "Welcome to Potablys API"
			}
		]
	}

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
) -> dict[str, list[dict[str, str | bool]]]:
	return {
		"detail": [
			{
				"type": "prediction_result",
				"msg": bool(predict_potability(temperature, do, pH, conductivity, bod, nitrate, fecalcaliform, totalcaliform))
			}
		]
	}

@app.post("/model/csv")
async def get_predictions(file: UploadFile = File(...)) -> dict[str, list[dict[str, str | dict[str, int | bool]]]]:
	csv_data: str = file.file.read().decode()
	reader: Iterator[list[str]] = csv.reader(StringIO(csv_data))

	next(reader)
	results: list[bool] = [bool(predict_potability(*map(float, line))) for line in reader]

	return {
		"detail": [
			{
				"type": "prediction_result",
				"msg": {
					"position": i,
					"result": result
				}
			}
			for i, result in enumerate(results)
		]
	}
