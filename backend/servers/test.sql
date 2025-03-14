
-- @block
SELECT * FROM Locations 
WHERE (street_address, city, state, zip_code, country) IN 
(
    ('123 Main St', 'New York', 'NY', '10001', 'USA'),
    ('456 Elm St', 'San Francisco', 'CA', '94107', 'USA'),
    ('789 Oak St', 'Chicago', 'IL', '60616', 'USA'),
    ('100 Oak St', 'Chicago', 'IL', '60616', 'USA')
);
