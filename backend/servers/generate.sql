
-- @block
CREATE TABLE IF NOT EXISTS Users(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- @block
CREATE TABLE IF NOT EXISTS Listings(
    listing_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    apartment_id INT NOT NULL,
    title TEXT NOT NULL,
    price BIGINT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status ENUM('active', 'inactive') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- @block
CREATE TABLE IF NOT EXISTS Apartments(
    apartment_id INT PRIMARY KEY AUTO_INCREMENT,
    square_footage BIGINT NOT NULL,
    bedrooms INT NOT NULL,
    bathrooms INT NOT NULL,
    location_id INT NOT NULL
);

-- @block 
CREATE TABLE IF NOT EXISTS Locations( 
    location_id INT PRIMARY KEY AUTO_INCREMENT,
    street_address VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    zip_code VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL
);

-- @block
CREATE TABLE IF NOT EXISTS Saved_Listings(
    user_id INT NOT NULL,
    listing_id INT NOT NULL,
    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- @block
CREATE TABLE IF NOT EXISTS Messages(
    message_id INT PRIMARY KEY AUTO_INCREMENT,
    sender_id INT NOT NULL,
    receiver_id INT NOT NULL,
    listing_id INT NOT NULL,
    message TEXT NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
