from database import get_db_connection
import datetime


def basic_listings_query():
    """
    Return the basic SELECT query for listings,
    joining Apartments and Locations.
    """
    return """
    SELECT l.*, a.*, loc.*
    FROM Listings l
    LEFT JOIN Apartments a ON l.apartment_id = a.apartment_id
    LEFT JOIN Locations loc ON a.location_id = loc.location_id
    WHERE 1=1
    """

def apply_apartments_filters(query, params, filters):
    """
    Apply filters from the Apartments table:
    - bedrooms, bathrooms, square_footage
    """
    if filters.get('bedrooms'):
        query += " AND a.bedrooms = %s"
        params.append(filters['bedrooms'])
    if filters.get('bathrooms'):
        query += " AND a.bathrooms = %s"
        params.append(filters['bathrooms'])
    if filters.get('square_footage'):
        query += " AND a.square_footage = %s"
        params.append(filters['square_footage'])
    return query, params

def apply_listings_filters(query, params, filters):
    """
    Apply filters from the Listings table:
    - price, start_date, end_date, status, etc.
    """
    if filters.get('price'):
        query += " AND l.price = %s"
        params.append(filters['price'])
    if filters.get('start_date'):
        query += " AND l.start_date = %s"
        params.append(filters['start_date'])
    if filters.get('end_date'):
        query += " AND l.end_date = %s"
        params.append(filters['end_date'])
    if filters.get('status'):
        query += " AND l.status = %s"
        params.append(filters['status'])
    return query, params

def apply_location_filters(query, params, filters):
    """
    Apply filters from the Locations table:
    - street_address, city, state, etc.
    """
    if filters.get('street_address'):
        query += " AND loc.street_address LIKE %s"
        params.append(f"%{filters['street_address']}%")
    return query, params


def get_listings(filters):
    """
    Get listings from the database based on the provided filters.

    Filters include:
      - Apartments: bedrooms, bathrooms, square_footage
      - Listings: price, start_date, end_date, status
      - Locations: street_address, city, state, zip_code, country

    Args:
        filters (dict): Dictionary containing filters for the query.
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # create base query
    query = basic_listings_query()
    params = []

    # apply filters and add to query as needed
    query, params = apply_apartments_filters(query, params, filters)
    query, params = apply_listings_filters(query, params, filters)
    query, params = apply_location_filters(query, params, filters)

    query += " GROUP BY l.listing_id ORDER BY l.created_at DESC LIMIT 100"

    cursor.execute(query, params)
    listings = cursor.fetchall()

    cursor.close()
    conn.close()

    return listings



def create_listing(listing_data):
    """
    Create a new listing in the database along with the associated apartment and location.

    Args:
        listing_data (dict): Dictionary containing listing information.
            Expected keys include:
              - Location data: street_address, city, state, zip_code, country
              - Apartment data: bedrooms, bathrooms, square_footage
              - Listing data: title, price, description, start_date, end_date

    Returns:
        dict: Information about the created listing including new IDs for listing, apartment, and location.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # insert into locations tabe
        street_address = listing_data.get('street_address')
        city = listing_data.get('city')
        state = listing_data.get('state')
        zip_code = listing_data.get('zip_code')
        country = listing_data.get('country')
        
        location_query = """
            INSERT INTO Locations (street_address, city, state, zip_code, country)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(location_query, (street_address, city, state, zip_code, country))
        location_id = cursor.lastrowid
        
        # insert into Apartments table
        bedrooms = listing_data.get('bedrooms')
        bathrooms = listing_data.get('bathrooms')
        square_footage = listing_data.get('square_footage')
        
        apartment_query = """
            INSERT INTO Apartments (bedrooms, bathrooms, square_footage, location_id)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(apartment_query, (bedrooms, bathrooms, square_footage, location_id))
        apartment_id = cursor.lastrowid
        
        # insert into Listings table
        title = listing_data.get('title')
        price = listing_data.get('price')
        description = listing_data.get('description')
        start_date = listing_data.get('start_date')
        end_date = listing_data.get('end_date')
        
        # convert string dates to date objects if necessary.
        if isinstance(start_date, str):
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        if isinstance(end_date, str):
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        
        user_id = 100 # HARDCODED FOR NOW

        listing_query = """
            INSERT INTO Listings (user_id, title, price, description, start_date, end_date, apartment_id, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
        """
        cursor.execute(listing_query, (user_id, title, price, description, start_date, end_date, apartment_id))
        listing_id = cursor.lastrowid
        
        # commit the transaction if all insertions are successful.
        conn.commit()

        cursor.close()
        conn.close()
        
        return {
            'user_id': user_id,
            'listing_id': listing_id,
            'apartment_id': apartment_id,
            'location_id': location_id,
            'message': 'Listing created successfully'
        }
    
    except Exception as e:
        # rollback the transaction if any insertion fails.
        if 'conn' in locals():
            conn.rollback()
            cursor.close()
            conn.close()
        raise Exception(f"Error creating listing: {str(e)}")