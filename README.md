# UKPostCodeValidator API

## Overview

The UKPostCodeValidator API is a Flask-based service that provide endpoint for validating and formatting UK postcodes. It uses the UKPostcodeValidator library to perform these operations.

## Getting Started

Make sure you have Python installed on your system.

Clone the project:
```bash
  git clone https://github.com/MichelAlvim/UKPostCodeValidator.git
```

Go to the project directory
```bash
  cd UKPostCodeValidator
```

Install the required dependencies by running the following command in your project directory:
```bash
  pip install -r requirements.txt
```

## Run the Application: 
 Run:   
```bash
  python app.py
```

Access the API:
    Open your web browser and go to http://127.0.0.1:5000.

## API Endpoints

Validate and Format Postcode
* Endpoint: /validate_postcode
* Method: POST
* Example Request:
    ```json
    {
        "postcode": "D n551PT"
    }
* Example Response:
    ```json
    {
        "is_valid": true,
        "formatted_postcode": "DN55 1PT"
    }

## Note
* The API runs on http://127.0.0.1:5000.
* Ensure that you include the correct payload with the "postcode" parameter in your requests.

## Authors

- [@MichelAlvim](https://github.com/MichelAlvim)
