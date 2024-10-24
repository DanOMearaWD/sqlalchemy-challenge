# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
from flask import Flask, jsonify
from datetime import datetime, timedelta


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
#print(Base.classes.keys())
station = Base.classes.station
measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    measurement_most_recent_date = session.query(measurement).order_by(desc(measurement.date)).first().date
    twelve_months_ago = datetime.strptime(measurement_most_recent_date, '%Y-%m-%d') - timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    precipitation_data_12mo = session.query(measurement.date, measurement.prcp)\
        .filter(measurement.date >= twelve_months_ago)\
        .order_by(measurement.date)\
        .all()
    
    # Convert query results to a dictionary
    precipitation_dict = {date: prcp for date, prcp in precipitation_data_12mo}
    return jsonify(precipitation_dict)











session.close()
if __name__ == '__main__':
    app.run(debug=True)