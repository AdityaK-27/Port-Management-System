-- DROP old tables if they exist (optional, if you're starting fresh)
DROP TABLE IF EXISTS Departure;
DROP TABLE IF EXISTS Arrival;
DROP TABLE IF EXISTS Ships;

-- Table to store all ships currently at port
CREATE TABLE Ships (
    ShipName VARCHAR(50),
    ShipNumber VARCHAR(20),
    DateOfArrival DATE,
    CargoType VARCHAR(50),
    ShipDimensions VARCHAR(50),
    Berth VARCHAR(20)
);

-- Table to log all arrivals, with estimated departure time
CREATE TABLE Arrival (
    ShipName VARCHAR(50),
    ShipNumber VARCHAR(20),
    DateOfArrival DATE,
    TimeOfArrival TIME,
    CargoType VARCHAR(50),
    ShipDimensions VARCHAR(50),
    Berth VARCHAR(20),
    PilotName VARCHAR(50),
    EstimatedDepartureTime TIME
);

-- Table to log all departures
CREATE TABLE Departure (
    ShipName VARCHAR(50),
    ShipNumber VARCHAR(20),
    DateOfDeparture DATE,
    TimeOfDeparture TIME,
    CargoType VARCHAR(50),
    ShipDimensions VARCHAR(50),
    Berth VARCHAR(20),
    PilotName VARCHAR(50)
);
