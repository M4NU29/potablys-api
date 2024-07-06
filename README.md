# Potablys API

This is a RESTful API that provides access to a water potability prediction model. It is built using FastAPI.

## Installation

To run this API locally, follow these steps:

1. Clone the repository.
2. Install the dependencies by running `pip install -r requirements.txt`.
3. Now, open the API in dev mode by running `fastapi dev ./src/main.py`.

## Usage

The API has three endpoints:

| Root | Description |
|------|-------------|
| `/` | Returns a welcome message. |
| `/model` | Predicts water potability based on the provided parameters. |
| `/model/csv` | Accepts a CSV file containing water quality data and returns a JSON response containing the predictions for each row of the CSV file. |

## `/model` endpoint

### Parameters

- `temperature`: The temperature of the water in degrees Celsius.
- `do`: The dissolved oxygen in the water in milligrams per liter.
- `pH`: The pH level of the water.
- `conductivity`: The conductivity of the water in microsiemens per centimeter.
- `bod`: The biochemical oxygen demand of the water in milligrams per liter.
- `nitrate`: The nitrate found in water as a result of agricultural runoff, sewage, and industrial waste, measured in milligrams per liter.
- `fecalcaliform`: The fecal coliform found in the intestines of warm-blooded animals, used as an indicator of water contamination by fecal matter, measured in colony-forming units per 100 milliliters.
- `totalcaliform`: The total Coliform found in the environment, used as an indicator of overall water quality, measured in colony-forming units per 100 milliliters.

### Response

The response will be a JSON object with the following structure:

```json
{
	"detail": [
		{
			"type": "prediction_result",
			"msg": <boolean>
		}
	]
}
```

## `/model/csv` endpoint

### Request

The request should be a POST request to `/model/csv` with a CSV file as the request body. The CSV file should have the following columns in the following order:

1. `temperature` (float)
2. `do` (float)
3. `pH` (float)
4. `conductivity` (float)
5. `bod` (float)
6. `nitrate` (float)
7. `fecalcaliform` (float)
8. `totalcaliform` (float)

**Important:** The first row of the CSV file should be a header row containing the column names.

### Response

The response will be a JSON object with the following structure:

```json
{
  "detail": [
    {
      "type": "prediction_result",
      "msg": {
        "position": <integer>,
        "result": <boolean>
      }
    },
    ...
  ]
}
```
