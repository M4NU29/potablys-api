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

### Parameters

- `temperature`: The temperature of the water in degrees Celsius.
- `do`: The dissolved oxygen in the water in milligrams per liter.
- `pH`: The pH level of the water.
- `conductivity`: The conductivity of the water in microsiemens per centimeter.
- `bod`: The biochemical oxygen demand of the water in milligrams per liter.

The response will be a JSON object like the following:

```json
{
	detail: [
		{
			type: "prediction_result",
			msg: true
		}
	]
}
```

Request
The request should be a POST request to /model/csv with a CSV file as the request body. The CSV file should have the following columns in the following order:

temperature (required, float)
do (required, float)
pH (required, float)
conductivity (required, float)
bod (optional, float, default: 0)
nitrate (optional, float, default: 0)
fecalcaliform (optional, float, default: 0)
totalcaliform (optional, float, default: 0)
The first row of the CSV file should be a header row containing the column names.

Response
The response will be a JSON object with the following structure:

Copy
Insert
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
The detail field is an array of objects, one for each row of the CSV file. Each object has a type field with the value "prediction_result", and a msg field with an object containing the following fields:

position (integer): the row number of the CSV file (starting from 0)
result (boolean): the prediction for the row
Example
Here's an example of a request and response:

Request:

Copy
Insert
POST /model/csv HTTP/1.1
Content-Type: text/csv

temperature,do,pH,conductivity,bod,nitrate,fecalcaliform,totalcaliform
25.0,8.0,7.5,500.0,10.0,50.0,0.0,0.0
26.0,7.0,8.0,400.0,0.0,100.0,50.0,100.0
Response:

Copy
Insert
{
  "detail": [
    {
      "type": "prediction_result",
      "msg": {
        "position": 0,
        "result": true
      }
    },
    {
      "type": "prediction_result",
      "msg": {
        "position": 1,
        "result": false
      }
    }
  ]
}

