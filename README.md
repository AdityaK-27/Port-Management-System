# 🚢 Port Management System

A terminal-based **Port Management System** built using **Python** and **MySQL**. This project simulates operations at a port such as managing ship arrivals, departures, berth assignments, and maintaining a live ship register. Developed as part of a Class XII Informatics Practices project, it also demonstrates backend-database integration and record management using SQL.

---

## 📌 Project Objectives

* ✅ Reduce manual paperwork at ports
* ✅ Digitize and secure ship entry/exit logs
* ✅ Enable quick search and berth tracking
* ✅ Create a system that is easy to use and understand
* ✅ Demonstrate backend integration of Python with SQL

---

## ⚙️ Features

* 🛳 **Add Ship**: Add ship details (name, number, cargo, dimensions, pilot, etc.)
* 📥 **Ship Arrival**: Logs a ship's entry and stores arrival data in `Arrival` and `Ships`
* 📤 **Ship Departure**: Removes ship from active register and logs data in `Departure`
* 🔍 **Find Ship**: Search a ship and find its assigned berth
* 📄 **Display Ship Details**: View all data for a particular ship
* 📋 **Display All Ships**: View all ships currently docked at the port
* 🔒 **Password Protection**: Simple password check before accessing system

---

## 🛠️ Tech Stack

| Tool                   | Description                           |
| ---------------------- | ------------------------------------- |
| Python 3.x             | Core programming language             |
| MySQL                  | Relational database management        |
| MySQL Workbench        | GUI for managing database and queries |
| mysql-connector-python | Python package to connect to MySQL    |

---

## 🗃️ Database Schema (Defined in `tables.sql`)

This project uses three tables:
```sql
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

```
## 📦 Folder Structure
```
Port-Management-System/
├── port_management.py      # Main Python program
├── tables.sql              # SQL script to create database & tables
├── requirements.txt        # Python package requirement
└── README.md               # Project documentation
```
## 🚀 How to Run the Project
🔧 Step 1: Clone the Repository
git clone https://github.com/YOUR_USERNAME/Port-Management-System.git
cd Port-Management-System

🔧 Step 2: Install Required Packages
pip install -r requirements.txt

🔧 Step 3: Set Up the Database
Open MySQL Workbench
Open a new SQL tab and run the contents of tables.sql
This creates the PortManagment database with all 3 required tables

🔧 Step 4: Run the Application
python port_management.py

## 🔐 Password to Access System:
123Ships

## 🧪 Sample Run
```
>-------------------------------------------------------------------<
                         PORT MANAGEMENT
    1. Add Ships
    2. Ship Arrival
    3. Find a Ship
    4. Display Ship's Details
    5. Ship Departure
    6. Display All Ships on Port
>--------------------------------------------------------------------<
```
## 🔮 Future Enhancements
🚦 Berth availability check before assignment

🖼️ GUI version using Tkinter or Flask

📊 Dashboard showing ship stats and analytics

👤 Admin and user role-based login

📦 Export data to CSV/Excel

☁️ Host the database on cloud (like AWS RDS)

## 👨‍💻 Author
Aditya Kankarwal
