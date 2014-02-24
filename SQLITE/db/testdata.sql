BEGIN TRANSACTION;

CREATE TABLE Cars(Id integer PRIMARY KEY, Name text, Cost integer);

INSERT INTO Cars VALUES(1,'Audi',52642);

INSERT INTO Cars VALUES(2,'Mercedes',57127);

INSERT INTO Cars VALUES(3,'Skoda',9000);

INSERT INTO Cars VALUES(4,'Volvo',29000);

INSERT INTO Cars VALUES(5,'Bentley',350000);

INSERT INTO Cars VALUES(6,'Citroen',21000);

INSERT INTO Cars VALUES(7,'Hummer',41400);

INSERT INTO Cars VALUES(8,'Volkswagen',21600);

COMMIT;

BEGIN TRANSACTION;

CREATE TABLE Orders(Id integer PRIMARY KEY, OrderPrice integer CHECK(OrderPrice>0), Customer text);

INSERT INTO Orders(OrderPrice, Customer) VALUES(1200, "Williamson");

INSERT INTO Orders(OrderPrice, Customer) VALUES(200, "Robertson");

INSERT INTO Orders(OrderPrice, Customer) VALUES(40, "Robertson");

INSERT INTO Orders(OrderPrice, Customer) VALUES(1640, "Smith");

INSERT INTO Orders(OrderPrice, Customer) VALUES(100, "Robertson");

INSERT INTO Orders(OrderPrice, Customer) VALUES(50, "Williamson");

INSERT INTO Orders(OrderPrice, Customer) VALUES(150, "Smith");

INSERT INTO Orders(OrderPrice, Customer) VALUES(250, "Smith");

INSERT INTO Orders(OrderPrice, Customer) VALUES(840, "Brown");

INSERT INTO Orders(OrderPrice, Customer) VALUES(440, "Black");

INSERT INTO Orders(OrderPrice, Customer) VALUES(20, "Brown");

COMMIT;

BEGIN TRANSACTION;

CREATE TABLE Friends(Id integer PRIMARY KEY, Name text UNIQUE NOT NULL, Sex text CHECK(Sex IN ('M', 'F')));

INSERT INTO Friends VALUES(1,'Jane', 'F');

INSERT INTO Friends VALUES(2,'Thomas', 'M');

INSERT INTO Friends VALUES(3,'Franklin', 'M');

INSERT INTO Friends VALUES(4,'Elisabeth', 'F');

INSERT INTO Friends VALUES(5,'Mary', 'F');

INSERT INTO Friends VALUES(6,'Lucy', 'F');

INSERT INTO Friends VALUES(7,'Jack', 'M');

COMMIT;

BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS Customers(CustomerId integer PRIMARY KEY, Name text);

INSERT INTO Customers(Name) VALUES('Paul Novak');

INSERT INTO Customers(Name) VALUES('Terry Neils');

INSERT INTO Customers(Name) VALUES('Jack Fonda');

INSERT INTO Customers(Name) VALUES('Tom Willis');


CREATE TABLE IF NOT EXISTS Reservations(Id integer PRIMARY KEY, CustomerId integer, Day text);

INSERT INTO Reservations(CustomerId, Day) VALUES(1, '2009-22-11');

INSERT INTO Reservations(CustomerId, Day) VALUES(2, '2009-28-11');

INSERT INTO Reservations(CustomerId, Day) VALUES(2, '2009-29-11');

INSERT INTO Reservations(CustomerId, Day) VALUES(1, '2009-29-11');

INSERT INTO Reservations(CustomerId, Day) VALUES(3, '2009-02-12');

COMMIT;

BEGIN TRANSACTION;

CREATE TABLE Names(Id integer, Name text);

INSERT INTO Names VALUES(1,'Tom');

INSERT INTO Names VALUES(2,'Lucy');

INSERT INTO Names VALUES(3,'Frank');

INSERT INTO Names VALUES(4,'Jane');

INSERT INTO Names VALUES(5,'Robert');

COMMIT;

BEGIN TRANSACTION;

CREATE TABLE Books(Id integer PRIMARY KEY, Title text, Author text, Isbn text default 'not available');

INSERT INTO Books VALUES(1,'War and Peace','Leo Tolstoy','978-0345472403');

INSERT INTO Books VALUES(2,'The Brothers Karamazov','Fyodor Dostoyevsky','978-0486437910');

INSERT INTO Books VALUES(3,'Crime and Punishment','Fyodor Dostoyevsky','978-1840224306');

COMMIT;

