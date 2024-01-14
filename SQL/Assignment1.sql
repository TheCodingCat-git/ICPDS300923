-- Table 1: SalesPeople
CREATE TABLE SalesPeople (
    Snum INT PRIMARY KEY,
    Sname VARCHAR(255) UNIQUE,
    City VARCHAR(255),
    Comm DECIMAL(5, 2)
);

-- Table 2: Customers
CREATE TABLE Customers (
    Cnum INT PRIMARY KEY,
    Cname VARCHAR(255),
    City VARCHAR(255) NOT NULL,
    Snum INT,
    FOREIGN KEY (Snum) REFERENCES SalesPeople(Snum)
);

-- Table 3: Orders
CREATE TABLE Orders (
    Onum INT PRIMARY KEY,
    Amt DECIMAL(8, 2),
    Odate DATE,
    Cnum INT,
    Snum INT,
    FOREIGN KEY (Cnum) REFERENCES Customers(Cnum),
    FOREIGN KEY (Snum) REFERENCES SalesPeople(Snum)
);


-- Insert data into Table 1: SalesPeople
INSERT INTO SalesPeople (Snum, Sname, City, Comm) VALUES
(1001, 'Peel', 'London', 0.12),
(1002, 'Serres', 'Sanjose', 0.13),
(1004, 'Motika', 'London', 0.11),
(1007, 'Rifkin', 'Barcelona', 0.15),
(1003, 'Axelrod', 'Newyork', 0.10);

-- Insert data into Table 2: Customers
INSERT INTO Customers (Cnum, Cname, City, Snum) VALUES
(2001, 'Hoffman', 'London', 1001),
(2002, 'Giovanni', 'Rome', 1003),
(2003, 'Liu', 'Sanjose', 1002),
(2004, 'Grass', 'Berlin', 1002),
(2006, 'Clemens', 'London', 1001),
(2008, 'Cisneros', 'Sanjose', 1007),
(2007, 'Pereira', 'Rome', 1004);

-- Insert data into Table 3: Orders
INSERT INTO Orders (Onum, Amt, Odate, Cnum, Snum) VALUES
(3001, 18.69, '03-10-1990', 2008, 1007),
(3003, 767.19, '03-10-1990', 2001, 1001),
(3002, 1900.10, '03-10-1990', 2007, 1004),
(3005, 5160.45, '03-10-1990', 2003, 1002),
(3006, 1098.16, '03-10-1990', 2008, 1007),
(3009, 1713.23, '04-10-1990', 2002, 1003),
(3007, 75.75, '04-10-1990', 2004, 1002),
(3008, 4273.00, '05-10-1990', 2006, 1001),
(3010, 1309.95, '06-10-1990', 2004, 1002),
(3011, 9891.88, '06-10-1990', 2006, 1001);

-- 1.Count the number of Salespersons whose names begin with 'a' or 'A'
SELECT COUNT(*)
FROM SalesPeople
WHERE UPPER(SUBSTRING(Sname, 1, 1)) = 'A';

-- 2.Display Salespersons whose all orders are worth more than Rs. 2000
SELECT S.Snum, S.Sname, S.City, S.Comm
FROM SalesPeople S
WHERE S.Snum NOT IN (
    SELECT O.Snum
    FROM Orders O
    GROUP BY O.Snum
    HAVING MAX(O.Amt) <= 2000
);

-- 3.Count the number of Salespersons belonging to New York
SELECT COUNT(*)
FROM SalesPeople
WHERE City = 'Newyork';

-- 4.Display the number of Salespeople belonging to London and Paris
SELECT City, COUNT(*) AS NumberOfSalespeople
FROM SalesPeople
WHERE City IN ('London', 'Paris')
GROUP BY City;

-- 5.Display the number of orders taken by each Salesperson and their date of orders
SELECT S.Snum, S.Sname, O.Odate, COUNT(*) AS NumberOfOrders
FROM SalesPeople S
JOIN Orders O ON S.Snum = O.Snum
GROUP BY S.Snum, S.Sname, O.Odate
ORDER BY S.Snum, O.Odate;


