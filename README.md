# SQLAlchemy Challenge: Weather API

## Description

The Weather API is a Flask application that provides access to weather data from a SQLite database. It allows users to retrieve precipitation and temperature observations from various weather stations in Hawaii. This API offers endpoints for accessing recent weather data, including temperature observations for the most active stations over the past year.

## API Endpoints

- **`/api/v1.0/precipitation`**: Returns precipitation data for the last 12 months.
- **`/api/v1.0/stations`**: Returns a list of weather stations.
- **`/api/v1.0/tobs`**: Returns temperature observations for the most active station over the last 12 months.
- **`/api/v1.0/<start>`**: Returns the minimum, average, and maximum temperatures for dates greater than or equal to the start date.
- **`/api/v1.0/<start>/<end>`**: Returns the minimum, average, and maximum temperatures for the date range between start and end dates.

## Project Structure

The project is organized into the following directories and files:

- **SurfsUp/**
  - **app.py**: Main application file to run the Flask API.
  - **climate_starter.ipynb**: Jupyter Notebook for initial data exploration and analysis.
- **Resources/**
  - **hawaii.sqlite**: SQLite database containing weather data.
  - **hawaii_measurements.csv**: CSV file with measurement data.
  - **hawaii_stations.csv**: CSV file with station information.

## Technologies Used

- **Flask**: A web framework for building the API.
- **SQLAlchemy**: An ORM for interacting with the SQLite database.
- **SQLite**: A lightweight database for storing weather data.
- **Jupyter Notebook**: An interactive environment for data exploration and analysis.
- **Pandas**: A data manipulation library for handling structured data.
- **Matplotlib**: A plotting library for visualizing data.
