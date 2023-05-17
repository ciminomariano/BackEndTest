# Backend Test

This project aims to load data from Yahoo Finance APIs into a MySQL database and identify dividends for the symbol "PETR4.SA". It also includes an API that provides the summarized amount of dividends per year based on the symbol and year filters.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Validation](#validation)
- [Contributing](#contributing)
- [License](#license)

## Description

The project consists of a backend application that interacts with Yahoo Finance APIs to fetch dividend data for the given symbol. It uses Django, a Python web framework, along with a MySQL database to store the retrieved data. Additionally, it provides an API endpoint to retrieve the summarized dividend amounts per year.

## Installation

To install and run the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/ciminomariano/BackEndTest.git`
2. Navigate to the project directory: `cd BackEndTest`
3. Create a virtual environment: `python3 -m venv env`
4. Activate the virtual environment:
   - On macOS and Linux: `source env/bin/activate`
   - On Windows: `.\env\Scripts\activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Set up the MySQL database:
   - Create a MySQL database for the project.
   - Configure the database connection in the `settings.py` file.
7. Run database migrations: `python manage.py migrate`

## Usage

To use the project:

1. Start the development server: `python manage.py runserver`
2. Access the API endpoint: `http://localhost:8000/api/dividends/download/` (Use Post Method)
   This endpoint will download the dividend obtained from yahoo
3. Access the API endpoint: `http://localhost:8000/api/dividends/<symbol>/<year>`
   - Replace `<symbol>` with the desired symbol (e.g., PETR4.SA).
   - Replace `<year>` with the desired year (e.g., 2022).
4. The API response will contain the summarized amount of dividends for the specified symbol and year.

## API Documentation

The API provides a single endpoint to retrieve the summarized amount of dividends per year for a given symbol and year.

### Endpoint

GET /api/dividends/<symbol>/<year>

yaml
Copy code

### Parameters

- `<symbol>` (required): The symbol for the desired stock (e.g., PETR4.SA).
- `<year>` (required): The year for which the dividend data is requested (e.g., 2022).

### Response

The API response will be in JSON format and will contain the summarized amount of dividends for the specified symbol and year.

Example response:

```json
{
  "symbol": "PETR4.SA",
  "year": 2022,
  "dividend_sum": 1234.56
}
Validation
To validate the numbers presented by the API, you can visit the following link: Investidor Petrobras - Dividends and JCP. Compare the dividend data obtained from the API with the information provided on the website to ensure accuracy.

