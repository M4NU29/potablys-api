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
) -> dict[str, list[dict[str, str | dict[str, bool]]]]:
	return {
		"detail": [
			{
				"type": "prediction_result",
				"msg": {
					"is_potable": bool(predict_potability(temperature, do, pH, conductivity, bod, nitrate, fecalcaliform, totalcaliform))
				}
			}
		]
	}

@app.post("/model/csv")
async def get_predictions(
	skip: int = 0,
	limit: int = 100,
	file: UploadFile = File(...)
) -> dict[str, list[dict[str, str | dict[str, int | bool]]] | dict[str, int]]:
	csv_data: str = file.file.read().decode()
	reader: Iterator[list[str]] = csv.reader(StringIO(csv_data))

	next(reader)
	results: list[bool] = [bool(predict_potability(*map(float, line))) for line in reader]

	total = len(results)
	total_pages = (total // limit) + (1 if total % limit > 0 else 0)

	return {
		"pagination": {
			"page": skip // limit + 1,
			"total_items": total,
			"items_per_page": limit,
			"total_pages": total_pages
		},
		"detail": [
			{
				"type": "prediction_result",
				"msg": {
					"position": i,
					"is_potable": result
				}
			}
			for i, result in enumerate(results[skip:skip+limit])
		]
	}
