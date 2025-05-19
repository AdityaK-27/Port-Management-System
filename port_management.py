import mysql.connector as a

con = a.connect(host="localhost", user="root", passwd="Ajay@1978", database="PortManagment")

def AddShips():
    SN = input("Enter Ship Name:")
    SNo = input("Enter Ship Number:")
    D = input("Enter Date of Arrival:")
    T = input("Enter Time of Arrival:")
    C = input("Enter Cargo Type:")
    SD = input("Enter Ship Dimensions (Length,Width,Depth):")
    B = input("Enter Berth (Alpha/Beta/Charlie/Delta):")
    PN = input("Enter Pilot Name:")
    data1 = (SN, SNo, D, C, SD, B)
    data2 = (SN, SNo, D, T, C, SD, B, PN)
    sql1 = 'INSERT INTO Ships VALUES (%s, %s, %s, %s, %s, %s)'
    sql2 = 'INSERT INTO Arrival VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    c = con.cursor()
    c.execute(sql1, data1)
    c.execute(sql2, data2)
    con.commit()
    print(">--------------------------------------------------------------------<")
    print("Data Entered Successfully")
    main()

def ShipArrival():
    SN = input("Enter Ship Name:")
    SNo = input("Enter Ship Number:")
    D = input("Enter Date of Arrival:")
    T = input("Enter Time of Arrival:")
    C = input("Enter Cargo Type:")
    SD = input("Enter Ship Dimensions (Length,Width,Depth):")
    B = input("Enter Berth (Alpha/Beta/Charlie/Delta):")
    PN = input("Enter Pilot Name:")
    data1 = (SN, SNo, D, T, C, SD, B, PN)
    data2 = (SN, SNo, D, C, SD, B)
    sql1 = 'INSERT INTO Arrival VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    sql2 = 'INSERT INTO Ships VALUES (%s, %s, %s, %s, %s, %s)'
    c = con.cursor()
    c.execute(sql1, data1)
    c.execute(sql2, data2)
    con.commit()
    print(">--------------------------------------------------------------------<")
    print("Ship Entered to:", B)
    main()

def FindShip():
    SN = input("Enter Ship Name:")
    a = "SELECT Berth FROM Ships WHERE ShipName = %s"
    data = (SN,)
    c = con.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    print(SN, "is assigned to Berth", myresult[0])
    main()

def DispShip():
    SN = input("Enter Ship Name:")
    a = "SELECT * FROM Ships WHERE ShipName = %s"
    data = (SN,)
    c = con.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    for i in myresult:
        print(i, end="|")
    main()

def ShipDeparture():
    SN = input("Enter Ship Name:")
    SNo = input("Enter Ship Number:")
    D = input("Enter Date of Departure:")
    T = input("Enter Time of Departure:")
    C = input("Enter Cargo Type:")
    SD = input("Enter Ship Dimensions (Length,Width,Depth):")
    B = input("Enter Berth (Alpha/Beta/Charlie/Delta):")
    PN = input("Enter PilotName:")
    data1 = (SN, SNo, D, T, C, SD, B, PN)
    data2 = (SN,)
    sql1 = 'INSERT INTO Departure VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    sql2 = 'DELETE FROM Ships WHERE ShipName = %s'
    c = con.cursor()
    c.execute(sql1, data1)
    c.execute(sql2, data2)
    con.commit()
    print(">--------------------------------------------------------------------<")
    print("Ship Left from", B)
    main()

def AllShips():
    a = "SELECT * FROM Ships"
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    for i in myresult:
        print("Ship Name:", i[0])
        print("Ship Number:", i[1])
        print("Date of Arrival:", i[2])
        print("Cargo Type:", i[3])
        print("Ship Dimensions:", i[4])
        print("Berth:", i[5])
        print(">----------------------------------------------------------------<")
    main()

def main():
    print("""
>-------------------------------------------------------------------<
                         PORT MANAGEMENT
    1. Add Ships
    2. Ship Arrival
    3. Find a Ship
    4. Display Ship's Details
    5. Ship Departure
    6. Display All Ships on Port
    """)
    choice = input("Enter Task Number:")
    print(">--------------------------------------------------------------------<")
    if choice == '1':
        AddShips()
    elif choice == '2':
        ShipArrival()
    elif choice == '3':
        FindShip()
    elif choice == '4':
        DispShip()
    elif choice == '5':
        ShipDeparture()
    elif choice == '6':
        AllShips()
    else:
        print("Wrong Choice")
        main()

def Password():
    ps = input("Enter Password:")
    if ps == "123Ships":
        main()
    else:
        print("Wrong Password")
        Password()

Password()
