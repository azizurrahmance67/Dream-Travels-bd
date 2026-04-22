import sqlite3

def init_sqlite_db():
    # database.db ফাইলের সাথে কানেক্ট করা
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # ১. Buses Table তৈরি (আপনার SQL কোড অনুযায়ী)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Buses (
            BusID INTEGER PRIMARY KEY AUTOINCREMENT,
            BusName TEXT,
            RouteFrom TEXT,
            RouteTo TEXT,
            DepartureTime TEXT,
            ArrivalTime TEXT,
            TotalSeats INTEGER,
            Price REAL
        )
    ''')

    # ২. Bookings Table তৈরি (আপনার SQL কোড অনুযায়ী)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Bookings (
            BookingID INTEGER PRIMARY KEY AUTOINCREMENT,
            PassengerName TEXT,
            PassengerPhone TEXT,
            BusID INTEGER,
            SeatNumbers TEXT,
            TravelDate TEXT,
            TotalFare REAL,
            BookingTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (BusID) REFERENCES Buses(BusID)
        )
    ''')

    # ৩. আগের ডাটাগুলো ইনসার্ট করা (যাতে ওয়েবসাইট খালি না দেখায়)
    # প্রথমে চেক করছি ডাটা অলরেডি আছে কি না
    cursor.execute("SELECT COUNT(*) FROM Buses")
    if cursor.fetchone()[0] == 0:
        bus_data = [
            (' AC_Coach-03', 'Dhaka', 'Chittagong', '08:00:00', '14:00:00', 36, 1200.00),
            ('Coach-ctg01', 'Dhaka', 'Chittagong', '08:30:00', '14:30:00', 40, 800.00),
            ('Coach-47', 'Dhaka', 'Chittagong', '09:00:00', '15:00:00', 41, 800.00),
            ('Coach-dc32', 'Dhaka', 'Chittagong', '10:00:00', '16:00:00', 40, 800.00)
        ]
        cursor.executemany('''
            INSERT INTO Buses (BusName, RouteFrom, RouteTo, DepartureTime, ArrivalTime, TotalSeats, Price)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', bus_data)
        print("Initial bus data inserted!")

    conn.commit()
    conn.close()
    print("Database Initialized Successfully with original SQL structure!")

if __name__ == '__main__':
    init_sqlite_db()