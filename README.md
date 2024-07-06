# Potablys API

This is a RESTful API that provides access to a water potability prediction model. It is built using FastAPI.

## Installation

To run this API locally, follow these steps:

1. Clone the repository.
2. Install the dependencies by running `pip install -r requirements.txt`.
3. Now, open the API in dev mode by running `fastapi dev ./src/main.py`.

## Usage

The API has two endpoints:

| Root | Description |
|------|-------------|
| `/` | Returns a welcome message. |
| `/model` | Predicts water potability based on the provided parameters. |

### Parameters

- `temperature`: The temperature of the water in degrees Celsius.
- `do`: The dissolved oxygen in the water in milligrams per liter.
- `pH`: The pH level of the water.
- `conductivity`: The conductivity of the water in microsiemens per centimeter.
- `bod`: The biochemical oxygen demand of the water in milligrams per liter.
- `nitrate`: The nitrate found in water as a result of agricultural runoff, sewage, and industrial waste, measured in milligrams per liter.
- `fecalcaliform`: The fecal coliform found in the intestines of warm-blooded animals, used as an indicator of water contamination by fecal matter, measured in colony-forming units per 100 milliliters.
- `totalcaliform`: The total Coliform found in the environment, used as an indicator of overall water quality, measured in colony-forming units per 100 milliliters.

The response will be a JSON object like the following:

```json
{
	"detail": [
		{
			"type": "prediction_result",
			"msg": true
		}
	]
}
```
