-- Insert sample locations
-- @block
INSERT INTO Locations (street_address, city, state, zip_code, country) VALUES
('123 Main St', 'New York', 'NY', '10001', 'USA'),
('456 Elm St', 'San Francisco', 'CA', '94107', 'USA'),
('789 Oak St', 'Chicago', 'IL', '60616', 'USA'),
('100 Oak St', 'Chicago', 'IL', '60616', 'USA');

-- Insert sample apartments
-- @block
INSERT INTO Apartments (square_footage, bedrooms, bathrooms, location_id) VALUES
(800, 2, 1, 1),
(1200, 1, 1, 2),
(600, 3, 1, 3),
(800, 1, 1, 4);

-- Insert sample users
-- @block
INSERT INTO Users (name, email, phone_number) VALUES
('Alice', 'alice@example.com', '123-456-7890'),
('Bob', 'bob@example.com', '234-567-8901'),
('Charlie', 'charlie@example.com', '345-678-9012');

-- Insert sample listings
-- @block
INSERT INTO Listings (user_id, apartment_id, title, price, start_date, end_date, status) VALUES
(1, 1, "Cozy 2 Bedroom Apartment", 1000, '2025-04-01', '2025-10-01', 'active'),
(2, 2, "Luxury Studio", 2000, '2025-05-01', '2025-11-01', 'active'),
(3, 3, "Spacious 3 Bedroom House", 3000, '2025-06-01', '2025-12-01', 'active'),
(3, 4, "1 Bedroom Room", 3001, '2025-06-01', '2025-12-01', 'active');




-- Query to remove all listings from all tables
-- @block
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE Apartments;
TRUNCATE TABLE Listings;
TRUNCATE TABLE Locations;
TRUNCATE TABLE Messages;
TRUNCATE TABLE Saved_Listings;
TRUNCATE TABLE Users;
SET FOREIGN_KEY_CHECKS = 1;


-- Query to delete all tables
-- @block
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE Apartments;
DROP TABLE Listings;
DROP TABLE Locations;
DROP TABLE Messages;
DROP TABLE Saved_Listings;
DROP TABLE Users;
SET FOREIGN_KEY_CHECKS = 1;
