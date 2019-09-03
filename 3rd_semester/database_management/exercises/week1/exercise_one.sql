-- just trying out comments
DROP TABLE IF EXISTS coffees;
CREATE TABLE coffees (
    name varchar(100),
    manufacturer varchar(200),
    PRIMARY KEY (name)
);

DROP TABLE IF EXISTS coffeehouses;
CREATE TABLE coffeehouses (
    name varchar(100),
    address varchar(200),
    license varchar(50),
    PRIMARY KEY (name)
);

DROP TABLE IF EXISTS sells;
CREATE TABLE sells (
    coffeehouse varchar(100) REFERENCES coffeehouses(name),
    coffee varchar(200) REFERENCES coffees(name),
    price REAL, 
    PRIMARY KEY (coffeehouse, coffee)
);

