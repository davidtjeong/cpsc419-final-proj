
-- @block
SELECT * FROM Locations 
WHERE (street_address, city, state, zip_code, country) IN 
(
    ('123 Main St', 'New York', 'NY', '10001', 'USA'),
    ('456 Elm St', 'San Francisco', 'CA', '94107', 'USA'),
    ('789 Oak St', 'Chicago', 'IL', '60616', 'USA'),
    ('100 Oak St', 'Chicago', 'IL', '60616', 'USA'),
);

-- Query to see if the example entry has successfully been added to the database
-- @block
SELECT * FROM Listings 
WHERE (title, price) IN
(
    ("Test Listing", 1000)
)

-- Query to delete the example entry that was added to database
-- @block
